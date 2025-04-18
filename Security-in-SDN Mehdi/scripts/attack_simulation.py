from mininet.net import Mininet
from mininet.topo import Topo
from mininet.util import dumpNodeConnections

class SimpleTopo(Topo):
    def build(self):
        # Créer des hôtes et des commutateurs
        h1 = self.addHost('h1')
        h2 = self.addHost('h2')
        s1 = self.addSwitch('s1')
        
        # Connecter les hôtes aux commutateurs
        self.addLink(h1, s1)
        self.addLink(h2, s1)

# Créer et démarrer Mininet
topo = SimpleTopo()
net = Mininet(topo)
net.start()

# Vérifier les connexions
dumpNodeConnections(net.hosts)

# Simuler une attaque DDoS
h1 = net.get('h1')
h2 = net.get('h2')

# Envoyer des paquets pour simuler une attaque
h1.cmd('ping -f %s' % h2.IP())

net.stop()
