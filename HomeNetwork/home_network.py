from mininet.net import Mininet 
from mininet.node import Host, OVSSwitch, Controller
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def create_network():
    net = Mininet(
            switch=OVSSwitch,
            link=TCLink
            )

    c0 = net.addController(
        'c0',
        controller=Controller
    )
    
    #Router
    r1 = net.addHost(
            'r1',
            ip='192.168.1.1/24'
            )

    #Switch
    s1 = net.addSwitch('s1')

    #End devices

    h1 = net.addHost(
            'h1',
            ip='192.168.1.10/24',
            defaultRoute='via 192.168.1.1'
            )
    h2 = net.addHost(
            'h2',
            ip='192.168.1.20/24',
            defaultRoute='via 192.168.1.1'
            )
    h3 = net.addHost(
            'h3',
            ip='192.168.1.30/24',
            defaultRoute='via 192.168.1.1'
            )


    # Router <----> Switch

    net.addLink(r1,s1, bw=100)

    # Switch <----> Devices

    net.addLink(h1, s1, bw=100)
    net.addLink(h2, s1, bw=100)
    net.addLink(h3, s1, bw=100)

    net.start()

    print("\n== Home Network ==")
    print("Router: 192.168.1.1")
    print("PC    : 192.168.1.10")
    print("Laptop: 192.168.1.20")
    print("Phone : 192.168.1.30")
    print("==================\n")

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
