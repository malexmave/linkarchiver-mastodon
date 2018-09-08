from mastodon import Mastodon, streaming
import config
from bs4 import BeautifulSoup
import requests
from pprint import pprint

class LinkStreamListener(streaming.StreamListener):
    def _archive_url(self, url):
        print(url)
        res = requests.get('https://web.archive.org/save/{}'.format(url),
                           headers={'user-agent':'@linkarchiver@botsin.space mastodon bot'})
        print("https://web.archive.org" + res.headers['Content-Location'])

    def on_update(self, status):
        soup = BeautifulSoup(status['content'], features='html.parser')
        print('Received toot:', status['content'])
        print("Extracted links:")
        for link in soup.find_all('a'):
            classes = link.get('class')
            if classes is not None:
                if 'mention' in classes:
                    continue
            url = link.get('href')
            if url.startswith('http'):
                self._archive_url(url)
        print('')

    def on_notification(self, notification):
        if notification['type'] == 'follow':
            account = notification['account']['acct']
            print('New follow by', account)
            dct = api.follows(account)
            if dct['acct'] == account:
                print("Followed back!")
            else:
                print("Something is off here.")
                pprint(dct)

api = Mastodon(config.CLIENT_ID, config.CLIENT_SECRET, config.ACCESS_TOKEN, api_base_url=config.BASE_URL)

listener = LinkStreamListener()

api.stream_user(listener)

