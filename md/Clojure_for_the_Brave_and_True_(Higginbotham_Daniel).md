#### Clojure for the Brave and True (Higginbotham, Daniel)
      Another way to look up a value in a map is to treat the map like a function with the key as its argument:

      Keywords can be used as functions that look up the corresponding value in a data structure.

      When should you use a list and when should you use a vector? A good rule of thumb is that if you need to easily add items to the beginning of a sequence or if you’re writing a macro, you should use a list. Otherwise, you should use a vector.

      It is better to have 100 functions operate on one data structure than 10 functions on 10 data structures. —Alan Perlis

      Clojure evaluates all function arguments recursively before passing them to the function.

      I think of abstractions as named collections of operations. If you can perform all of an abstraction’s operations on an object, then that object is an instance of the abstraction.

