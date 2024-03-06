#### Software Performance Testing: Concepts, Design, and Analysis (Shen, JJ)
      Latency is less than or equal to the response time of a request, since the response time is what it takes to get a full response for a request, and it includes request processing time at the server-side. We will discuss more on latency and response time throughout the rest of the book.

      Bandwidth is the transmission capacity, while throughput is the actual amount of data transmitted in a unit of time for a specific case. So, bandwidth is the maximum throughput of a communication path.

      Components Performance Impacting Factors Queueing               External: Browser # of requests to a particular server for an action Stalled/Blocked External: Network Network configuration DNS lookup          External: DNS service Connection time      External: Network Network latency Time to first byte     Internal: Software design;    Deployment architecture,  configuration & environment. External: Network Server processing speed; Server request load; Network latency Content download External: Network Network bandwidth

      The next table summarizes these factors and the major impacted performance indicators, respectively. Factors Major impacted performance indicators Algorithm complexity Response time Concurrency Throughput, # of concurrent users, Response time Structural limitation Throughput, # of concurrent users

      To be more specific, the major goals of performance testing are: (1)  To examine if the system meets the performance requirements in terms of performance indicators. (2)  To determine request baseline response time with a regular load below the capacity of the system. (3)  To examine system behaviors with expected load, and to find if there is any performance bottleneck with the application or system. (4)  To find out the capacity of the system, the maximum throughput without response time degradation. (5)  To evaluate the maximum number of concurrent users the system can support. (6)  To examine system behaviors when the load exceeds the capacity of the system. (7)  To evaluate the impact of hardware resources on software performance. (8)  To determine if the system can scale larger with additional resources.

      A performance benchmark of a software application is the standard or point of reference of a specific performance aspect of the application, and it serves as the baseline for comparison.

      Standard deviation is defined as the square root of the variance, it’s a measure of the extent of deviation of samples from the average value and the spread of data in a distribution. By definition, the standard deviation is:

      Percentile rank or percent rank is the percentage of values less than or equal to a specific value in a distribution. The percentile is the value a certain percentage of values are less than or equal to. So, a percentile is a value associated with a specific percentile rank, in other words, a percentile is a value in a dataset below which a percentage of data samples fall.

      A probability distribution for discrete variables is represented with a probability mass function, while a probability distribution for continuous variables is represented with a probability density function.

      Nonlinear functions are functions that are not linear

      Little’s law states that, under steady state condition, that is, for a stable system, the average number of items in a system equals the average rate at which an item arrives at the system multiplied by the average time an item spends in the system.

      From the server’s point of view, if incoming requests are placed in a queue and handled by a queueing scheduling process, then the request arriving pattern to the queue represents the distribution of think time between requests. The time between request arrivals can be represented by an exponential distribution, and the number of request arrivals in a specific time interval follows the Poisson distribution.

      The following is a list of the common ones: (a)  Constant think time (b)  Uniform random think time (c)   Gaussian random think time (d)  Poisson random think time

      We adopt a multiple-sigma rule, which defines the relationship between the number of concurrent users a system can support and the expected distribution of peak numbers of concurrent users at the effective capacity load level:

      specified, as listed in the following table. Design Parameters Required 1 Request distribution 2 User groups with request probabilities x 3 Concurrent time interval x 4 Effective capacity 5 Number of virtual users in each group x Table 5.6: Performance testing load design parameters

