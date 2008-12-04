from twisted.words.xish import domish
from wokkel.subprotocols import XMPPHandler
from wokkel.xmppim import AvailablePresence, Presence

NS_MUC = 'http://jabber.org/protocol/muc'

class CommitBot(XMPPHandler):

    def __init__(self, room, nick):
	XMPPHandler.__init__(self)

	self.room = room
	self.nick = nick
	self.joined = False

    def connectionMade(self):
	self.send(AvailablePresence())

	# add handlers

	# join room
	pres = Presence()
	pres['to'] = self.room + '/' + self.nick
	pres.addElement((NS_MUC, 'x'))

    
	
	
