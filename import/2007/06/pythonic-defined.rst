| `Introduction <#introduction>`__
| `Losing is Good <#losing>`__
| `Strings <#strings>`__
| `Dictionaries <#dictionaries>`__
| `Conclusion <#conclusion>`__
| 

Introduction
~~~~~~~~~~~~

| Veterans and novices alike of Python will hear the term "pythonic"
  thrown around, and even a number of the veterans don't know what it
  means. There are times I do not know what it means, but that doesn't
  mean I can define a pretty good idea of what "pythonic" really means.
  Now, it has been defined at times as being whatever the BDFL decides,
  but we'll pull that out of the picture. I want to talk about what the
  word means for us today, and how it applied to what we do in the real
  world.
| Languages have their strengths and their idioms (ways of doing
  things), and when you exploit those you embrace the heart of that
  language. You can often tell when a programmer writing in one language
  is actually more comfortable with another, because the code they right
  is telltale of the other language. Java developers are notorious for
  writing Java in every language they get their hands on. How can you
  write one language in another? The answer to that is exactly the
  opposite to understanding what a term like "pythonic" means. A
  programmer coming to Python from C might write everything in
  functions, and avoid classes, while a programmer coming from Java
  might refuse to ever use a function and often wants to create a
  separate module for *every single class*. These are the telltale
  influences of their comfort languages on their Python coding. The
  situation can occure between any migration between languages. Their
  following of those languages' idioms when they are writing Python is
  incorrect, but when writing those languages, it is embracing the
  language. Doing the same in Python, itself, is Pythonic.

In the Real World
-----------------

| You will not truly understand "pythonic" without seeing it and
  experiencing it in the real world. You'll know you understand it when
  you can reliably identify what is *not* pythonic. However, we can
  speed up your time to making those judgement calls through examples
  and talking about what makes them the way they are.
| 

Losing is Good
~~~~~~~~~~~~~~

| New comers to the language are often nervous about dynamic typing.
  Most don't really understand what it means, or why it can be a good
  thing. The most common new comer thoughts about dynamic typing is that
  you can assign any type of value to any variable. They like to think
  of them as void \* in C, which is a large mistake. Variables do not
  change type in Python. Instead, names have no type association at all
  and the objects they point to (reference) describe their own types.
  The nervousness and misunderstanding of dynamic typing leads to
  over-zealous employment of the isinstance() and type() as type
  checking facilities, even when the code is absolutely, perfectly valid
  without it.

   *If you code is correct if some section is removed, remove the
   section.*

| I think the best example of this has to be the dangerous desire to
  add, for example, isinstance(x, list) at the beginning of a function
  that expects an argument x to be a list. The programmer thinks safety
  has been added, by blocking the function from being called with
  anything not expected. What was accomplished is making the function
  slower, more brittle, and less pythonic. No longer can the function
  type a tuple, the keys of a dictionary, a generator, or an xrange
  object. New comers are not always aware of those things, or of how its
  so valuable to use them all interchangeably when the interface you
  need for each is the same subset: iteration.
| There are other cases where removing something actually gives you
  something. Make functions smaller, combine functions that do the same
  things and are named differently, and turn a class into a function
  where it does not add any properties or methods, such as a case where
  all the logic is in the \__init_\_ method. If you are having trouble
  catching an exception you don't know what to do with, don't catch it
  at all and let your caller deal with it. One of the best feelings you
  can get is cutting the lines of code in half, while simultaneously
  making the code gain new features and more speed.
| 

Strings
~~~~~~~

| Although the string may be the most common kind of data in a
  programming language, next to the integer, how they are handled
  between languages varies as wildly as David Hasslehoff's popularity
  between the States and Germany. A great many constructs with strings
  are good in one language and absolutely terrible in another. Some
  times the difference is only visual, and other times it has to do with
  the very nature of what a string is from language to language.

   *Immutable strings referenced by untyped names require completely
   different semantics than typed languages or those with mutable
   strings.*

| String concatenation, understanding of when to use string formatting,
  and grasping how string manipulations work are sometimes barriers
  faced by anyone not familiar with Python. I think we can break down
  the situation into a small set of rules to live by.

-  Connecting only two strings? Concatenation with the + operator is
   alright.
-  Connecting more than two strings? Use ''.join(iterable_of_strings),
   because Python can't optimize a chain of + on strings, as it does not
   know they are strings due to untyped names.
-  Are you using an empty string format, such as "%d" or "%r"? Then you
   are wastefully formatting where a simple call suffices, such as
   int(s) and repr(s), respectively.
-  Are you using a regular expression where the split, strip, or replace
   methods would suffice? Then do not use the regular expression.

Dictionaries
~~~~~~~~~~~~

| *Responding to a post at*\ `Blue Sky On
  Mars <http://www.blueskyonmars.com/2007/06/12/python-dictionaries-are-not-the-same-as-instances/>`__\ *,
  this section has been added to deal with the issue of classes and
  objects versus dictionaries.*
| You'll find dictionaries to be one of the most flexible and powerful
  concepts in Python. Much of the infrastructure of the language is
  actually built on top of them. We need to cover when you should use a
  dictionary and when you should not.
| A common error of those new to Python and languages with proper hash
  tables is to really over use when they are applied directly. People
  from C draw an obvious connection between a dictionary and a struct,
  and it makes sense. However, the connection only lasts for as long as
  its not applied as widespread as a struct is in C code. Dictionaries
  as general data structures are actually a very non-pythonic thing to
  do, despite the pythonic nature of dictionaries themselves. Python
  provides a rich, featureful object and class system, so abusing
  dictionaries is only lessening what power you have at your finger
  tips.

-  Type less.
   enemy.health is better than enemy["health"]
   enemy = Enemy(100, 50, 30) is better than enemy = {"health": 100,
   "attack": 50, "defense": 30}
-  Add methods, now or later.
   enemy.hit(player) is better than hit(enemy, player)
-  Default values, lazy computed values, and deprecation of values is
   not possible in a dictionary.

Time is Your Teacher
--------------------

| Nothing is going to teach you how to understand the real meaning of
  "pythonic" without experience and a lot of exposure to all kinds of
  Python code. Your best measure of your understanding of the concept is
  surely how well you can spot that code which is *not* pythonic, rather
  than that code which is. Code will begin to smell bad, and code smell
  is one of your most powerful tools as a developer, and one of the only
  tools, which can not be taught.
| Patience is your key.
