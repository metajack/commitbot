# commitbot

Commitbot is an XMPP bot that notifies multi-user chat rooms (MUCs) of
git repository commits.

It uses the [GitHub](http://www.github.com) post-receive web hook to
get push notifications of repository changes.

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

Copy `commitbot.tac.example` to `commitbot.tac` changing the JID,
password, room name, and room nickname to something appropriate.  Then
launch it with `twistd`.

    twistd -y commitbot.tac
