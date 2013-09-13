# commitbot

Commitbot is an XMPP bot that notifies multi-user chat rooms (MUCs) of
git repository commits.

It uses the [GitHub](http://www.github.com) post-receive web hook to
get push notifications of repository changes.

## License

This code is copyright (c) 2008 by Jack Moffitt <jack@metajack.im> and
is available under the [GPLv3](http://www.gnu.org/licenses/gpl.html).
See `LICENSE.txt` for details.

## Dependencies

* [Twisted](http://www.twistedmatrix.com) 8.1.x or later
* [Wokkel](http://wokkel.ik.nu) 0.4 or later
* [simplejson](http://pypi.python.org/pypi/simplejson)

Note that on Ubuntu/Debian systems Twisted is split into various
pieces.  You will want:

* python-twisted-words
* python-twisted-names

in addition to the normal Twisted package.

## Usage

Copy `commitbot.tac.example` to `commitbot.tac` changing the jabber_id,
password, room, and bot_name to something appropriate.  Then
launch it with `twistd`.

    twistd -y commitbot.tac

Finally, add `http://your-server-IP:8888` (or whichever port you set in the
commitbot.tac) as a WebHook to your GitHub-Repository. Congratulations,
you are all set up now.