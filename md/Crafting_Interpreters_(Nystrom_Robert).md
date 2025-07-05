#### Crafting Interpreters (Nystrom, Robert)
      Fairy tales are more than true: not because they tell us that dragons exist, but because they tell us that dragons can be beaten. ​— ​G.K. Chesterton by way of Neil Gaiman, Coraline

      A scanner (or lexer) takes in the linear stream of characters and chunks them together into a series of something more akin to “words”. In programming languages, each of these words is called a token.

      A parser takes the flat sequence of tokens and builds a tree structure that mirrors the nested nature of the grammar.

      The first bit of analysis that most languages do is called binding or resolution. For each identifier, we find out where that name is defined and wire the two together. This is where scope comes into play—the region of source code where a certain name can be used to refer to a certain declaration.

      Once we understand what the user’s program means, we are free to swap it out with a different program that has the same semantics but implements them more efficiently—we can optimize it.

      If you can’t resist poking your foot into that hole, some keywords to get you started are “constant propagation”, “common subexpression elimination”, “loop invariant code motion”, “global value numbering”, “strength reduction”, “scalar replacement of aggregates”, “dead code elimination”, and “loop unrolling”.

      Instead of instructions for some real chip, they produced code for a hypothetical, idealized machine. Wirth called this p-code for portable, but today, we generally call it bytecode because each instruction is often a single byte long.

      What’s the difference between a compiler and an interpreter? It turns out this is like asking the difference between a fruit and a vegetable. That seems like a binary either-or choice, but actually “fruit” is a botanical term and “vegetable” is culinary. One does not strictly imply the negation of the other. There are fruits that aren’t vegetables (apples) and vegetables that aren’t fruits (carrots), but also edible plants that are both fruits and vegetables, like tomatoes.

      An argument is an actual value you pass to a function when you call it. So a function call has an argument list. Sometimes you hear actual parameter used for these. A parameter is a variable that holds the value of the argument inside the body of the function. Thus, a function declaration has a parameter list. Others call these formal parameters or simply formals.

      This gets us to an important principle called maximal munch. When two lexical grammar rules can both match a chunk of code that the scanner is looking at, whichever one matches the most characters wins.

      The art, then, is finding accidental complexity that can be omitted—language features and interactions that don’t carry their weight by increasing the breadth or ease of using the language.
