# Introduction 
A Campus network is comprised of packet-transport services wired and wireless, traffic identification and control (security and application optimization),  traffic monitoring and management, and overall systems management and provisioning

### Service Level function that the organization provides
- Non-Stop High Availability services
- Access and Mobility services
- Application optimization and protection services
- Virtualization services
- security services
- Operational and management services

# Design Principle

Heirarchy, Modularity, Resiliency, Flexibility

## Heirarchy

- *Modularized* components assembled in **Heirarchial** and structural manner.

### Heirarchial Tiers
1. Core
2. Distribution
3. Access

**ACCESS**
> Place where end devices are connected eg: Printers, Wireless APs, PCs

| **Service Reqirements** | **Service Features** |
| ----------------------- | -------------------- |
| Discovery and Configuration Services | 802.1AF, CDP, LLDP, LLDP-MED |
| Security Services | IBNS (802.1X), (CISF): port security, DHCP
snooping, DAI, IPSG|
| Application Recognition Services | QoS marking, policing, queuing, deep packet
inspection NBAR, etc |
| Network Identity and Access | 802.1X, MAB, Web-Auth |
| Intelligent Network Control Services | PVST+, Rapid PVST+, EIGRP, OSPF, DTP,
PAgP/LACP, UDLD, FlexLink, Portfast,
UplinkFast, BackboneFast, LoopGuard,
BPDUGuard, Port Security, RootGuard |
| Physical Infrastructure Service | Power over Ethernet |

**DISTIBUTION**



**CORE**
> Must Provide Redundancy for near immediate data flow recovery in the event of any component faiure

> A network that requires routine config changes to the core device does not yet have the appropriate degree of design modularization
> More the changes affects core more it points towards seperation of core and Distribution

> A topology with a core is costlier mesier than the one with a core

***Mapping the Control and Data Plane to the Physicall Heirarchy***

