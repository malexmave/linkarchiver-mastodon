Link Archiver @ Mastodon
========================

[@LinkArchiver@botsin.space](https://botsin.space/@linkarchiver) is a Mastodon bot that will archive all links posted by people it follows and archive them using the [Internet Archive Wayback Machine](https://archive.org/web/). This bot was inspired by the (now defunct) [@LinkArchiver twitter bot](https://github.com/thisisparker/linkarchiver). Since Mastodon still has a working streaming API, I decided to build a simple clone of the Archiver for Mastodon.

If you want the bot to follow you, simply follow it, and it will follow back. You can then (optionally) unfollow it again. If you want it to no longer follow you, simply block it (and optionally unblock it again), and you're done.

The code is pretty bare-bones right now and lacks some of the more advanced features the original bot had. It is also only using the streaming API right now, so any tweets sent while the bot isn't online will not be archived. It goes without saying that you should not depend on this bot for anything serious, right?

The code is licensed AGPL.

If you want to run your own version, you'll need to get a Client ID, Client Secret and an access token. See [this tutorial](https://gist.github.com/aparrish/661fca5ce7b4882a8c6823db12d42d26) on how to do this.
