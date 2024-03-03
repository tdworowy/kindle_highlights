#### TCP/IP Illustrated, Volume 1 (Addison-Wesley Professional Computing Series) (R., Fall Kevin)
      Chunks coming from different sources or senders can be mixed together and pulled apart later, which is called multiplexing.

      In statistical multiplexing, traffic is mixed together based on the arrival statistics or timing pattern of the traffic.

      a datagram is a special type of packet in which all the identifying information of the source and final destination resides inside the packet itself (instead of in the packet switches).

      Fate sharing suggests placing all the necessary state to maintain an active communication association (e.g., virtual connection) at the same location with the communicating endpoints.

      The end-to-end argument tends to support a design with a “dumb” network and “smart” systems connected to the network

      With best-effort delivery, the network does not expend much effort to ensure that data is delivered without errors or gaps.

      With layering, each layer is responsible for a different facet of the communications.

      A router, by definition, has two or more network interfaces (because it connects two or more networks). Any system with multiple interfaces is called multihomed.

      There are three types of IP addresses, and the type affects how forwarding is performed: unicast (destined for a single host), broadcast (destined for all hosts on a given network), and multicast (destined for a set of hosts that belong to a multicast group).

      The Internet Control Message Protocol (ICMP) is an adjunct to IP, and we label it as a layer 3.5 protocol.

      The Internet Group Management Protocol (IGMP) is another protocol adjunct to IPv4.

      Datagram Congestion Control Protocol (DCCP),

      Stream Control Transmission Protocol (SCTP),

      This notion is the basis for the so-called Metcalfe’s Law, which states roughly that the value of a computer network is proportional to the square of the number of connected endpoints (e.g., users or devices).

      Some organizations that depend on Internet access for their continued operations attach to the Internet using more than one provider (called multihoming) in order to provide for redundancy in case of failure, or for other reasons.

      Today, IP addresses serve as both identifiers (essentially a form of name) and locators (an address understood by the routing system) for a network interface attached to the Internet. Providing a separation would allow the network protocol implementation to function even if the underlying IP address changes. Protocols that provide this separation are sometimes called identifier/locator separating or id/loc split protocols.

      Shim6 introduces a “shim” network-layer protocol that separates the “upper-layer protocol identifier” used by the transport protocols from the IP address.

      The IP address is used to identify and locate network interfaces on devices throughout the Internet system (unicast addresses). It may also be used for identifying more than one such interface (multicast, broadcast, or anycast addresses

      (called provider-independent or PI addresses). Numerically adjacent address prefixes (PA addresses) can be aggregated to save routing table space and improve scalability of the Internet.

      IPv6 unicast addresses differ somewhat from IPv4 addresses. Most important, IPv6 addresses have a scope concept, for both unicast and multicast addresses, that specifically indicates where an address is valid. Typical scopes include node-local, link-local, and global. Link-local addresses are often created based on a standard prefix in combination with an IID that can be based on addresses provided by lower-layer protocols (such as hardware/MAC addresses) or random values. This approach aids in autoconfiguration of IPv6 addresses.

