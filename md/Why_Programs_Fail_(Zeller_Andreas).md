#### Why Programs Fail (Zeller, Andreas)
      Not every defect results in an infection, and not every infection results in a failure. Thus, having no failures does not imply having no defects. This is the curse of testing, as pointed out by Dijkstra. Testing can only show the presence of defects, but never their absence.

      The wording of the previous example thus becomes clearer: The defect caused an infection, which caused a failure—and when we saw the failure we tracked the infection, and finally found and fixed the defect.

      Testing is the process of executing a program with the intent of producing some problem.

      The rule of thumb is: The friendlier an interface is to humans, the less friendly it is to computers.

      Overall, the general principle of breaking a dependence is known as the dependence inversion principle, which can be summarized as depending on abstractions rather than details. Whenever you have some component A depending on some component B, and you want to break this dependence, you perform the following: 1. Introduce an abstract superclass B’, and make B a subclass of B‘. 2. Set up A such that it depends on the abstract B’ rather than on the concrete B. 3. Introduce alternate subclasses of B’ that can be used with A such that B is no longer required.

      Have others test. Testing for unknown problems is a destructive process. By all means, one must try to uncover a weakness in the program. As people in general prefer being constructive to ripping things apart, this is a difficult psychological situation for most. In particular, it makes an author unsuited to test his or her own code. Therefore, always have someone independent test your program, and be open to criticism.

      Schroedinbug (MIT: from the Schrödinger’s cat thought experiment in quantum physics): A design or implementation bug in a program that does not manifest until someone reading source code or using the program in an unusual way notices that it never should have worked, at which point the program promptly stops working for everybody until fixed.

      Perfection is achieved not when you have nothing more to add, but when there is nothing left to take away. –(attributed to) ANTOINE DE SAINT-EXUPÉRY

      static techniques predict approximations of a program’s future; dynamic analysis remembers approximations of a program’s past.

      Something impossible occurred, and the only solid information is that it really did occur. So we must think backwards from the result to discover the reasons.

