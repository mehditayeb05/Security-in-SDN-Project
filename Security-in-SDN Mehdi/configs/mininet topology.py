from mininet.net import Mininet
from mininet.topo import Topo
from mininet.node import RemoteController

class CustomTopo(Topo):
    def build(self):
        s1 = self.addSwitch('s1')
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        h3 = self.addHost('h3')
        self.addLink(h1, s1)
        self.addLink(h2, s1)
        self.addLink(h3, s1)

net = Mininet(topo=CustomTopo(), controller=RemoteController)
net.start()
net.pingAll()
net.stop()

