#### UNIX and Linux System Administration Handbook (Evi, Nemeth)
      Be conservative in what you send and liberal in what you receive. (This tenet is also known as Postel’s Law, named in honor of Jon Postel, who served as Editor of the RFC series from 1969 until his death in 1998.) Be liberal in who you hire, but fire early. Don’t use weasel words. Undergraduates are the secret superpower. You can never use too much red ink. You don’t really understand something until you’ve implemented it. It’s always time for sushi. Be willing to try something twice. Always use sudo.

      By and large, the differences among Linux distributions are not cosmically significant. In fact, it is something of a mystery why so many different distributions exist, each claiming “easy installation” and “a massive software library” as its distinguishing features. It’s hard to avoid the conclusion that people just like to make new Linux distributions.

      Traditional BIOS assumes that the boot device starts with a record called the MBR (Master Boot Record). The MBR includes both a first-stage boot loader (aka “boot block”) and a primitive disk partitioning table. The amount of space available for the boot loader is so small (less than 512 bytes) that it’s not able to do much other than load and run a second-stage boot loader.

      The anti-systemd camp argues that the UNIX philosophy is to keep system components small, simple, and modular. A component as fundamental as init, they say, should not have monolithic control over so many of the OS’s other subsystems. systemd not only breeds complexity, but also introduces potential security weaknesses and muddies the distinction between the OS platform and the services that run on top of it.

      systemd is not a single daemon but a collection of programs, daemons, libraries, technologies, and kernel components. A post on the systemd blog at 0pointer.de/blog notes that a full build of the project generates 69 different binaries. Think of it as a scrumptious buffet at which you are forced to consume everything.

      An entity that is managed by systemd is known generically as a unit. More specifically, a unit can be “a service, a socket, a device, a mount point, an automount point, a swap file or partition, a startup target, a watched filesystem path, a timer controlled and supervised by systemd, a resource management slice, a group of externally created processes, or a wormhole into an alternate universe.” OK, we made up the part about the alternate universe (the rest is from the systemd.unit man page), but that still covers a lot of territory.

      You can disable setuid and setgid execution on individual filesystems by specifying the nosuid option to mount. It’s a good idea to use this option on filesystems that contain users’ home directories or that are mounted from less trustworthy administrative domains.

      Like PAM, Kerberos deals with authentication rather than access control per se. But whereas PAM is an authentication framework, Kerberos is a specific authentication method. At sites that use Kerberos, PAM and Kerberos generally work together, PAM being the wrapper and Kerberos the actual implementation.

      Given the world’s wide range of computing environments and the mixed success of efforts to advance the standard model, kernel maintainers have been reluctant to act as mediators in the larger debate over access control. In the Linux world, the situation came to a head in 2001, when the U.S. National Security Agency proposed to integrate its Security-Enhanced Linux (SELinux) system into the kernel as a standard facility.

      The fd subdirectory represents open files in the form of symbolic links.

      Instead of reaching for umount -f when a filesystem you’re trying to unmount turns out to be busy, run the fuser command to find out which processes hold references to that filesystem. fuser -c mountpoint prints the PID of every process that’s using a file or directory on that filesystem, plus a series of letter codes that show the nature of the activity.

      All directories have at least two hard links: the link from the parent directory and the link from the special file called . inside the directory itself.

      PXE acts like a miniature OS that sits in a ROM on your network card. It exposes its network capabilities through a standardized API for the system BIOS to use. This cooperation makes it possible for a single boot loader to netboot any PXE-enabled PC without having to supply special drivers for each network card.

      Commercial identity management systems combine several key UNIX concepts into a warm and fuzzy GUI replete with marketing jargon.

      A cloud server is just one member of a herd, and to treat it otherwise is to ignore a basic fact of cloud computing: cloud systems are ephemeral, and they can fail at any time. Plan for that failure and you’ll be more successful at running a resilient infrastructure.

      UNIX is often criticized for being inconsistent, and indeed it is. Just take a look at a directory of log files

      As a packet travels down the protocol stack (from TCP or UDP transport to IP to Ethernet to the physical wire) in preparation for being sent, each protocol adds its own header information. Each protocol’s finished packet becomes the payload part of the packet generated by the next protocol. This nesting is known as encapsulation. On the receiving machine, the encapsulation is reversed as the packet travels back up the protocol stack.

      IPv4 fragmentation problems can be insidious. Although path MTU discovery should automatically resolve MTU conflicts, an administrator must occasionally intervene. If you are using a tunneled architecture for a virtual private network, for example, you should look at the size of the packets that are traversing the tunnel. They are often 1,500 bytes to start with, but once the tunneling header is added, they become 1,540 bytes or so and must be fragmented. Setting the MTU of the link to a smaller value averts fragmentation and increases the overall performance of the tunneled network. Consult the ifconfig or ip-link man page to see how to set an interface’s MTU.

      Microsoft has largely succeeded in convincing the world that every computer needs its own built-in firewall. However, that’s not really true. In fact, machine-specific firewalls can lead to no end of inconsistent behavior and mysterious network problems if they are not managed in synchrony with site-wide standards.

