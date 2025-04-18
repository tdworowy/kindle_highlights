#### Clojure for the Brave and True (Higginbotham, Daniel)
      Another way to look up a value in a map is to treat the map like a function with the key as its argument:

      Keywords can be used as functions that look up the corresponding value in a data structure.

      When should you use a list and when should you use a vector? A good rule of thumb is that if you need to easily add items to the beginning of a sequence or if you’re writing a macro, you should use a list. Otherwise, you should use a vector.

      It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures. —Alan Perlis

      Clojure evaluates all function arguments recursively before passing them to the function.

      I think of abstractions as named collections of operations. If you can perform all of an abstraction’s operations on an object, then that object is an instance of the abstraction.

      Another way to think about this is that reality is largely referentially transparent. If you think of gravity as a function, then gravitational force is the return value of calling that function on two objects. Therefore, the next time you’re in a programming interview, you can demonstrate your functional programming knowledge by knocking everything off your interviewer’s desk. (This also demonstrates that you know how to apply a function over a collection.)

      So Clojure is homoiconic: it represents abstract syntax trees using lists, and you write textual representations of lists when you write Clojure code. Because the code you write represents data structures that you’re used to manipulating and the evaluator consumes those data structures, it’s easy to reason about how to programmatically modify your program.

      You’ll then study the three goblins that harry every practitioner: reference cells, mutual exclusion, and dwarven berserkers. And you’ll learn three tools that will aid you: futures, promises, and delays.”

      cynical person might say that Java gives you enough rope to hang yourself, and if you find such a person, I hope you give them a hug.

