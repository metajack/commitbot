from twisted.python import log
from twisted.web import resource
from twisted.words.xish import domish
from wokkel.subprotocols import XMPPHandler
from wokkel.xmppim import AvailablePresence, Presence

import simplejson as json


NS_MUC = 'http://jabber.org/protocol/muc'
NS_XHTML_IM = 'http://jabber.org/protocols/xhtml-im'
NS_XHTML_W3C = 'http://www.w3.org/1999/xhtml'

class CommitBot(XMPPHandler):

    def __init__(self, room, nick):
        XMPPHandler.__init__(self)

        self.room = room
        self.nick = nick

    def connectionMade(self):
        self.send(AvailablePresence())

        # add handlers

        # join room
        pres = Presence()
        pres['to'] = self.room + '/' + self.nick
        pres.addElement((NS_MUC, 'x'))
        self.send(pres)

    def notify(self, data):
        # build the messages
        text = []
        html = []
        link = r"<a href='%s' name='%s'>%s</a>"
        
        text.append('New commits in %s:\n' % data['repository']['url'])
        html.append("New commits in " \
                        "<a href='%s'>%s</a>:<br/>" % \
                        (data['repository']['url'],
                         data['repository']['name']))

        for c in data['commits']:
            text.append('%s | %s | %s\n' % (c['message'],
                                            c['author']['email'], 
                                            c['url']))
            ltxt = link % (c['url'], c['id'], c['id'][:7])
            html.append('%s | %s | %s<br />' % (c['message'],
                                                c['author']['email'],
                                                ltxt))
        msg = domish.Element((None, 'message'))
        msg['to'] = self.room
        msg['type'] = 'groupchat'
        msg.addElement('body', content=''.join(text))
        wrap = msg.addElement((NS_XHTML_IM, 'html'))
        body = wrap.addElement((NS_XHTML_W3C, 'body'))
        body.addRawXml(''.join(html))

        self.send(msg)


class WebHook(resource.Resource):
    isLeaf = True

    def __init__(self, bot):
        resource.Resource.__init__(self)
        self.bot = bot

    def render_GET(self, req):
        return "commitbot ready to rock!"

    def render_POST(self, req):
        data = json.loads(req.args['payload'][0])
        self.bot.notify(data)
        return ""
