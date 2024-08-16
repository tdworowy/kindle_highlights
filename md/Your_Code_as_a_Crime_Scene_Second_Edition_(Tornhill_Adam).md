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

