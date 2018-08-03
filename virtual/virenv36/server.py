from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory

class SimpleLogger(Protocol):
    def connectionMade(self):
        print('connecting'), self.transport.client

    def connectionLost(self, reason):
        print(self.transport.client)

    def dataReceived(self, data):
        print(data)


factory = Factory()
factory.protocol = SimpleLogger

reactor.listenTCP(8088, factory)
reactor.run()
