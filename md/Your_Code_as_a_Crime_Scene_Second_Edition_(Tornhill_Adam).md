#### Your Code as a Crime Scene, Second Edition (Tornhill, Adam)
      Software is a socio-technical construct, where team dynamics, deadlines, personal preferences, skills, and organizational values leave their mark on a codebase and its history.

      In a surprisingly short time, we’ve moved from lighting fires in our caves to reasoning about multicores and CPU caches in cubicles. Yet, we handle modern technology with the same biological tools our prehistoric ancestors used for basic survival. That’s why taming complexity in software must start with how we think. Programming needs to be aligned with the way our brain works.

      Building software at scale might be the most challenging task humanity ever attempted. Accidental complexity—code that is more complicated than the problem calls for—adds to the challenge. Such code becomes expensive to maintain, bug-ridden, and hard to change.

      Complex code is only a problem if we need to deal with it. Maybe our most complex piece of code has been stable for years, works wonderfully in production, and no one needs to modify it. Does it really make a difference whether it’s complex? Well, you may have a potential time bomb waiting to go off, and it’s a long-term risk you need to be aware of. But large-scale codebases are full of unwarranted complexity. It’s unreasonable to address them all at once.

      This limitation isn’t specific to cyclomatic complexity but is a fundamental property of code metrics in general. No matter how accurate our metrics are—and there are better options than cyclomatic complexity out there—if we limit ourselves to a static view of the code, then we will never be able to prioritize the parts that really matter.

      Enclosure diagrams present an alternative visualization that cognitively scales well.

      This ratio represents a typical pattern, although at the higher end of the scale. In general, hotspots stretch across only 1 to 5 percent of the total codebase, yet that code is responsible for 25 to 75 percent of all bugs. You see, power laws are everywhere in software.

      The BitCoin hotspot data brings us to an important point: when investigating complexity trends, the interesting thing isn’t the numbers themselves but the shape of the evolutionary curve. The following figure summarizes the patterns you’re most likely to find in your code.

      However, remember that when looking at the current hotspots, we lack the original context. All mistakes look obvious in hindsight, but there could be multiple reasons why the code is as it is. Perhaps it was a strategic decision to build on top of a fragile base—a deliberate technical debt. Or, your former project manager made the hasty decision to deploy what was intended as a throw-away prototype into production. Now it’s your problem. (True story.)

      For a programmer, one of the most interesting cognitive concepts is working memory. Working memory is the mental workbench of the mind, enabling you to perceive, interpret, and manipulate information in your head. You engage working memory when doing crosswords, solving a sudoku puzzle, or—what we’re focusing on—trying to understand a piece of code. Working memory is vital to us programmers.

      methods within AbstractEntityPersister.java, a hotspot in

      The preceding example presents a selection of the methods within AbstractEntityPersister.java, a hotspot in Hibernate. Given that the hotspot has 5000 lines of code and is closing in on 400 methods, we can suspect the Abstract prefix is an oxymoron—we’re likely to find complex logic here. A true crime scene.

      LCOM4 captures connected graphs of function dependencies via shared data and call chains. Two functions belong to the same graph if a) they access the same data or b) one function invokes the other.

      The takeaway is that it doesn’t matter how simple and clean our code is if we implement the wrong system. When investigating hotspots, always question the feature set. Could parts of the code be removed? Great. Less code is always better.

      Bad names attract suffixes like lemonade draws wasps on a hot summer day. The immediate suspects are everything that ends with Manager, Util, or the dreaded Impl. Modules baptized like that are typically placeholders, but they end up housing core logic elements over time. You know they will hurt once you look inside.

      The Law of Demeter (LoD) is a design principle for object-oriented code, summed up beautifully in the maxim of “Don’t talk to strangers.” (See

      Violating the Law of Demeter creates a coding style reminiscent of Jack the Ripper: reach for the interiors and dig them out. (Disclaimer: no objects were harmed in this case study.)

      Still, software design does more than compensate; it enables. A good design allows us to reason about both problems and solutions so that we can refine our code, generalize to patterns, and adapt to new challenges from there.

      In the late 2010s, we finally got research numbers on the impact of technical debt. The numbers vary depending on which study you read. They all paint a pretty depressing picture: organizations waste 23 to 42 percent of developers’ time dealing with the consequences of technical debt and bad code in general (Software developer productivity loss due to technical debt [BMB19]).

      As a thought experiment, let’s consider what 42 percent waste implies. Say we have a department with 100 software engineers. If we waste 42 percent of their time, all else being equal, we end up with an output corresponding to just 58 developers, an efficiency loss that would be unacceptable in virtually any other context than software.

      Hyperbolic discounting is frequently used to explain the psychology of addiction. It’s also, coincidentally, the best explanation of why companies fail to manage technical debt: just like the addict, we trade our future well-being—a healthy codebase—for the lure of the next quick fix and short-term reward. Or, in the words of Mel Conway: “There’s never enough time to do something right, but there’s always enough time to do it over” (quote from How do committees invent? [Con68]).

      we need quality to go fast. Use that to your advantage.

      Finally, when discussing metrics and outcomes, we also need to touch on the DevOps Research & Assessment (DORA), which established the Four Key Metrics (FKM): change lead time, deployment frequency, mean time to restore, and change fail percentage.[50] In their research, the DORA team showed that these metrics are solid leading indicators for how the organization as a whole is doing.

      There are multiple reasons why we experience false memories. First, our memory is constructive, meaning the information we get after an event can shape how we recall the original situation. Our memory organizes the new information together with the old information, and we forget when we acquired each detail or insight.

      Given that a single verb variation was enough manipulation to bias an eyewitness, imagine how many false assumptions we might make during a regular day. When we program, we’re stuck with the same brain and its tendencies toward biases. Sure, in programming, you can go back and recheck the code. The problem is that we have to do that repeatedly—the sheer complexity of software makes it impossible to hold all of the information in our heads. That means our brain works with a simplified view, and as soon as we drop details, we risk missing something critical.

      In programming, version-control data lets us trace changes over a series of commits to detect patterns. One prominent pattern is called change coupling. Change coupling means that two (or more) modules evolve together over time. As such, change coupling implies a temporal dependency, which cannot be detected in code alone; a static snapshot of code lacks the evolutionary perspective.

      Another shortcoming with the measure is that we’re limited to the information contained in commits. We may miss important coupling relationships that occur between commits. The solution to this problem requires hooks into our IDE to record precise information on the order in which we interact with each piece of code. Tools like that are under active research.

      By the time you notice the symptoms of architectural decay and technical debt, it’s hard to reverse those trends. Doing an after-the-fact analysis is vital for proceeding with meaningful improvements, but essentially, these actions come too late. So why not make it a habit to perform regular analyses early and continuously?

      Code can decay fast, so sit down with the team and walk through the analyses on a weekly basis. This approach has several advantages: You spot structural decay immediately. You see the structural impact of each feature as you work with it. You make your evolving architecture visible to everyone on the team.

      The composite pictures won because individual imperfections were also evened out with each additional morphed photo. This is surprising since it makes beauty a negative concept, defined by what’s absent rather than what’s there. Beauty is the absence of ugliness.

      Beauty, being the absence of ugliness, translates well to our software world, too. Beautiful code has a consistent level of expression that’s easy to follow. Just as deviations from the mathematical average make a face less attractive, so does any coding construct that deviates from the main style of your application or introduces accidental barriers to understanding the code. Examples of such issues include special cases and the code smells covered in Chapter 6, ​Remediate Complicated Code​.

      So, beauty is about consistency and avoiding surprises. Fine. But what you consider a surprise depends on context. In the real world, you won’t be surprised to see an elephant at the zoo, but you’d probably rub your eyes if you saw one in your front yard (at least here in Sweden, where I live). Context matters in software, too.

      Package by component is one such pattern that I have seen work particularly well as an alternative to layers. I discuss the pattern in more depth in Software Design X-Rays: Fix Technical Debt with Behavioral Code Analysis [Tor18], but the gist of it is to slice your architecture into components that combine application logic with data-access logic inside the same building block. See the following figure.

      However, tactical forking offers another possible path.[66] With this pattern, you duplicate the codebase into a new, isolated component, and then start to remove all the code that isn’t needed. You flip the problem on its head. Tactical forks might be useful when your potential component has strong and inconsistent dependencies or as an optional path if you get stuck during the dependency breaking.

      Microservices are based on an old idea: keep each part small and orthogonal to others, and use a simple mechanism to glue everything together (for example, a message bus or an HTTP API). In fact, these are the same principles on which UNIX has built since the dawn of curly braces in code.

      I’m not sure how much the philosopher Friedrich Nietzsche knew about coding, but his classic observation that “if you gaze into the abyss, the abyss gazes also into you” clearly indicates that he had a good grasp on how our code influences us. In modern psychology, there’s a related phenomenon called the mere-exposure effect. The mere-exposure effect is the fact that we humans tend to develop a stronger preference the more often we see something. That something could be abstract symbols, human faces, or a particular coding style.

      Automated tests are still a relatively young discipline, and we, as a community, might not yet have captured all the patterns needed to ensure that our tests remain maintainable. Adding to that challenge, in many organizations, tests are still added as an afterthought, almost like a hidden architectural layer. In those situations, the systems often become hard to reason about and more painful to maintain than necessary.

      But architecture goes beyond structure, and we should treat architecture as a set of principles rather than a specific collection of modules. Let’s think of architecture as principles that help us reason through and navigate large-scale systems. Breaking these principles is expensive since it makes the system harder to understand. It introduces ugliness.

      Automated tests becoming mainstream is a promising trend. When we automate mundane tasks, we humans can focus on real testing, where we explore and evaluate the value of the features we deliver. Test automation also makes changes to the system more predictable. We get a safety net when modifying software, and we use the scripts to communicate knowledge and drive additional development. Test automation—at all levels—is a prerequisite for continuous delivery, allowing us to ship high-quality software daily.

      While we all know these benefits, we rarely discuss the risks and costs of test automation. Automated tests, particularly on the system level, are notoriously hard to get right. And when we fail, these tests become time sinks, halting all real progress.

      Test scripts are architecture, too—albeit an often neglected aspect. Like any architectural boundary, a good test system should encapsulate details and avoid depending on the internals of the code being tested. We want to refactor the implementation without affecting the tests themselves. If we get this wrong, we rip increasingly larger holes in the safety net that a test suite could provide.

      Now, you might think that I pulled out an extreme case with the Roslyn hotspot just to make my point. And you’d be correct. I did. But I did it for a reason. Over the past decade, I’ve probably analyzed 300-plus codebases. During all those analyses, I observed that we developers are fairly conscious of the DRY principle…in application code. When it comes to test code, well, not so much. Consequently, some of the worst technical debt I find tends to be in tests, similar to what we found in the Roslyn platform.

      The preceding figure presents a model from educational psychology. (See Understanding and solving word arithmetic problems [KG85].) We programmers face the same challenges as educators: we have to communicate knowledge to all the programmers who come to the code after we’ve left. That knowledge is built by an iterative process between two mental models: The situation model contains everything you know about the problem, together with your existing knowledge and problem-solving strategies. The system model is a precise specification of the solution—in this case, your code.

      This model of problem-solving lets us define what makes a good design: a good design is any solution where the two mental models are closely aligned. That kind of design is easier to understand because you can easily switch between the problem and the solution. Tests that are easy to understand form a fundamental building block by supporting rapid feedback.

      One of the most common planning mistakes is to scope your tasks to represent product features.

      Earlier in our fictional example about joining a new team, you fell prey to pluralistic ignorance. Pluralistic ignorance happens when everyone privately rejects a norm but thinks everyone else in the group supports it. Over time, pluralistic ignorance can lead to situations where a group follows rules that all of its members reject in private.

