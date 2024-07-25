#### A Philosophy of Software Design, 2nd Edition (Ousterhout, John K. )
      The most fundamental problem in computer science is problem decomposition: how to take a complex problem and divide it up into pieces that can be solved independently.

      Writing computer software is one of the purest creative activities in the history of the human race. Programmers aren’t bound by practical limitations such as the laws of physics; we can create exciting virtual worlds with behaviors that could never exist in the real world. Programming doesn’t require great physical skill or coordination, like ballet or basketball. All programming requires is a creative mind and the ability to organize your thoughts.

      The first approach is to eliminate complexity by making code simpler and more obvious. For example, complexity can be reduced by eliminating special cases or using identifiers in a consistent fashion.

      The second approach to complexity is to encapsulate it, so that programmers can work on a system without being exposed to all of its complexity at once. This approach is called modular design.

      Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system.

      The overall complexity of a system (C) is determined by the complexity of each part p (cp) weighted by the fraction of time developers spend working on that part (tp). Isolating complexity in a place where it will never be seen is almost as good as eliminating the complexity entirely.

      Change amplification: The first symptom of complexity is that a seemingly simple change requires code modifications in many different places.

      Cognitive load: The second symptom of complexity is cognitive load, which refers to how much a developer needs to know in order to complete a task.

      Sometimes an approach that requires more lines of code is actually simpler, because it reduces cognitive load.

      Unknown unknowns: The third symptom of complexity is that it is not obvious which pieces of code must be modified to complete a task, or what information a developer must have to carry out the task successfully.

      An abstraction is a simplified view of an entity, which omits unimportant details.

      Unfortunately, the value of deep classes is not widely appreciated today. The conventional wisdom in programming is that classes should be small, not deep. Students are often taught that the most important thing in class design is to break up larger classes into smaller ones. The same advice is often given about methods: “Any method longer than N lines should be divided into multiple methods” (N can be as low as 10). This approach results in large numbers of shallow classes and methods, which add to overall system complexity.

      Information leakage is one of the most important red flags in software design. One of the best skills you can learn as a software designer is a high level of sensitivity to information leakage. If you encounter information leakage between classes, ask yourself “How can I reorganize these classes so that this particular piece of knowledge only affects a single class?”

      it is more important for a module to have a simple interface than a simple implementation.

      Pulling complexity down makes the most sense if (a) the complexity being pulled down is closely related to the class’s existing functionality, (b) pulling the complexity down will result in simplifications elsewhere in the application, and (c) pulling the complexity down simplifies the class’s interface. Remember that the goal is to minimize overall system complexity.

      One of the most fundamental questions in software design is this: given two pieces of functionality, should they be implemented together in the same place, or should their implementations be separated? This question applies at all levels in a system, such as functions, methods, classes, and services.

      length by itself is rarely a good reason for splitting up a method. In general, developers tend to break up methods too much. Splitting up a method introduces additional interfaces, which add to complexity.

      Each method should do one thing and do it completely.

      The exceptions thrown by a class are part of its interface; classes with lots of exceptions have complex interfaces, and they are shallower than classes with fewer exceptions.

      Overall, the best way to reduce bugs is to make software simpler.

      The overall idea behind comments is to capture information that was in the mind of the designer but couldn’t be represented in the code.

      If the information in a comment is already obvious from the code next to the comment, then the comment isn’t helpful. One example of this is when the comment uses the same words that make up the name of the thing it is describing.

      If you want code that presents good abstractions, you must document those abstractions with comments.

      If interface comments must also describe the implementation, then the class or method is shallow.

      The main goal of implementation comments is to help readers understand what the code is doing (not how it does it).

      When choosing a name, the goal is to create an image in the mind of the reader about the nature of the thing being named.

      Ideally, when you have finished with each change, the system will have the structure it would have had if you had designed it from the start with that change in mind. To achieve this goal, you must resist the

      If you’re not making the design better, you are probably making it worse.

      Another way of thinking about obviousness is in terms of information. If code is nonobvious, that usually means there is important information about the code that the reader does not have:

      One of the most important elements of good software design is separating what matters from what doesn’t matter.

      One way to emphasize is with prominence: important things should appear in places where they are more likely to be seen, such as interface documentation, names, or parameters to heavily used methods. Another way to emphasize is with repetition: key ideas appear over and over again.

      A third way to emphasize is with centrality. The things that matter the most should be at the heart of the system, where they determine the structure of things around them. One example is the interface for device drivers in operating systems; this is a central idea because hundreds or thousands of drivers will depend on it.

