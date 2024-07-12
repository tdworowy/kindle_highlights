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

