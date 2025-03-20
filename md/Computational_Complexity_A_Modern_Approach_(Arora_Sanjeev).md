#### Computational Complexity: A Modern Approach (Arora, Sanjeev)
      the efficiency of an algorithm is to a considerable extent much more important than the technology used to execute it.

      But Chapters 19 and 20 show a surprising recent result giving strong evidence that randomness does not help speed up computation too much, in the sense that any probabilistic algorithm can be replaced with a deterministic algorithm (tossing no coins) that is almost as efficient.

      Claim 1.6 Define a single-tape Turing machine to be a TM that has only one read-write tape, that is used as input, work, and output tape. For every f : {0, 1}* → {0, 1} and time-constructible T : N → N, if f is computable in time T(n) by a TM M using k tapes, then it is computable in time 5kT(n)2 by a single-tape TM 

      Definition 1.12 (The class DTIME) Let T : N → N be some function. A language L is in DTIME(T(n)) iff there is a Turing machine that runs in time c · T(n) for some constant c > 0 and decides L.

      We say that a machine decides a language L ⊆ {0, 1}* if it computes the function fL : {0, 1}* → {0, 1}, where fL(x) = 1 , x ∈ L.

      A complexity class is a set of functions that can be computed within given resource bounds.

      Second, the running time is a function of the number of bits in the input.

      Most scientists believe the Church-Turing (CT) thesis, which states that every physically realizable computation device—whether it’s based on silicon, DNA, neurons or some other alien technology—can be simulated by a Turing machine. This implies that the set of computable problems would be no larger on any other computational model that on the Turing machine.

      However, when it comes to efficiently computable problems, the situation is less clear. The strong form of the CT thesis says that every physically realizable computation model can be simulated by a TM with polynomial overhead (in other words, t steps on the model can be simulated in tc steps on the TM, where c is a constant that depends upon the model). If true, it implies that the class P defined by the aliens will be the same as ours. However, this strong form is somewhat controversial, in particular because of models such as quantum computers (see Chapter 10), which do not appear to be efficiently simulatable on TMs.

      In 1931, Kurt Gödel shocked the mathematical world by showing that certain true statements about the natural numbers are inherently unprovable, thereby shattering an ambitious agenda set in 1900 by David Hilbert to base all of mathematics on solid axiomatic foundations. In 1936, Alonzo Church defined a model of computation called λ-calculus (which years later inspired the programming language LISP) and showed the existence of functions inherently uncomputable in this model [Chu36].

      In Section 2.1, we define a complexity class NP that aims to capture the set of problems whose solutions can be efficiently verified. By contrast, the class P of the previous chapter contains decision problems that can be efficiently solved.

      It turns out that the independent set problem is at least as hard as any other language in NP: If it has a polynomial-time algorithm then so do all the problems in NP. This fascinating property is called NP-hardness. Since most scientists conjecture that NP ≠ P, the fact that a language is NP-hard can be viewed as evidence that it cannot be decided in polynomial time.

