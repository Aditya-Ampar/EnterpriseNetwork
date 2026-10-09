from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink


from CongestionTest import run_test
def create_network():

    net = Mininet(
            switch=OVSSwitch,
            link=TCLink
            )

    #Controller
    net.addController(
            'c0',
            controller=Controller
            )

    #Switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    #Hosts
    h1 = net.addHost('h1', ip='10.0.0.1/24')
    h2 = net.addHost('h2', ip='10.0.0.2/24')
    h3 = net.addHost('h3', ip='10.0.0.3/24')   

    #Access Links

    net.addLink(h1, s1, bw=100)
    net.addLink(h2, s1, bw=100)
    net.addLink(h3, s2, bw=200)

    net.addLink(s1, s2, bw=200)

    net.start()

    print()
    print("=====================================")
    print("         BOTTLENECK NETWORK")
    print("h1------------100 Mbps -----------s1")
    print("h2------------100 Mbps -----------s1")
    print("                                     |")
    print("                                     s2---------------100 Mbps -----------h3")
    print("=====================================")
    print()
    

    run_test(h1, h2, h3)

    CLI(net)
    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
