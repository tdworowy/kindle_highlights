#### Software Performance Testing: Concepts, Design, and Analysis (Shen, JJ)
      Latency is less than or equal to the response time of a request, since the response time is what it takes to get a full response for a request, and it includes request processing time at the server-side. We will discuss more on latency and response time throughout the rest of the book.

      Bandwidth is the transmission capacity, while throughput is the actual amount of data transmitted in a unit of time for a specific case. So, bandwidth is the maximum throughput of a communication path.

      Components Performance Impacting Factors Queueing               External: Browser # of requests to a particular server for an action Stalled/Blocked External: Network Network configuration DNS lookup          External: DNS service Connection time      External: Network Network latency Time to first byte     Internal: Software design;    Deployment architecture,  configuration & environment. External: Network Server processing speed; Server request load; Network latency Content download External: Network Network bandwidth

      The next table summarizes these factors and the major impacted performance indicators, respectively. Factors Major impacted performance indicators Algorithm complexity Response time Concurrency Throughput, # of concurrent users, Response time Structural limitation Throughput, # of concurrent users

      To be more specific, the major goals of performance testing are: (1)  To examine if the system meets the performance requirements in terms of performance indicators. (2)  To determine request baseline response time with a regular load below the capacity of the system. (3)  To examine system behaviors with expected load, and to find if there is any performance bottleneck with the application or system. (4)  To find out the capacity of the system, the maximum throughput without response time degradation. (5)  To evaluate the maximum number of concurrent users the system can support. (6)  To examine system behaviors when the load exceeds the capacity of the system. (7)  To evaluate the impact of hardware resources on software performance. (8)  To determine if the system can scale larger with additional resources.

      A performance benchmark of a software application is the standard or point of reference of a specific performance aspect of the application, and it serves as the baseline for comparison.

