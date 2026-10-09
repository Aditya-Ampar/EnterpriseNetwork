#!/usr/bin/env python3

from mininet.net import Mininet
from mininet.node import OVSSwitch, Controller, Host
from mininet.cli import CLI
from mininet.log import setLogLevel
from mininet.link import TCLink

def create_network():
    net = Mininet(
            switch=OVSSwitch,
            link=TCLink
            ) 
    
    #Controller
    net.addController('c0',controller=Controller)
    
    #Router
    r1 = net.addHost('r1')

    #Switches
    s1 = net.addSwitch('s1')
    s2 = net.addSwitch('s2')

    #Users Subnet

    h1 = net.addHost(
            'h1',
            ip='192.168.10.10/24',
            defaultRoute='via 192.168.10.1'
            )
    h2 = net.addHost(
            'h2',
            ip='192.168.10.20/24',
            defaultRoute='via 192.168.10.1'
            )

    #IoT Subnet

    h3 = net.addHost(
            'h3',
            ip='192.168.20.10/24',
            defaultRoute='via 192.168.20.1'
            )
    h4 = net.addHost(
            'h4',
            ip='192.168.20.20/24',
            defaultRoute='via 192.168.20.1'
            )

    #Router <---> Switches

    net.addLink(r1, s1, bw=100)
    net.addLink(r1, s2, bw=100)

    #Users

    net.addLink(h1, s1, bw=100)
    net.addLink(h2, s1, bw=100)

    #IoT

    net.addLink(h3, s2, bw=100)
    net.addLink(h4, s2, bw=100)

    net.start()

    #Configure Router Interfaces

    r1.cmd('ifconfig r1-eth0 192.168.10.1/24')
    r1.cmd('ifconfig r1-eth1 192.168.20.1/24')

    #Enable IPv4 forwarding

    r1.cmd('sysctl -w net.ipv4.ip_forward=1')

    print()
    print("==================================")
    print("        TWO SUBNET HOME NET")
    print("==================================")
    print("Users LAN : 192.168.10.0/24")
    print("IoT LAN   : 192.168.20.0/24")
    print("-----------------------------------")
    print("Router    : 192.168.10.1 / 192.168.20.1")
    print("PC        : 192.168.10.10")
    print("Laptop    : 192.168.10.20")
    print("Tv        : 192.168.20.10")
    print("IoT       : 192.168.20.20")
    print("==================================")
    print()

    CLI(net)

    net.stop()

if __name__ == '__main__':
    setLogLevel('info')
    create_network()
