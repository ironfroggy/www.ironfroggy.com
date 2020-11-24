There is a question I often see from Python newbies: How to use the
contents of a string as a variable name. In other words, to dynamically
create a variable based on some runtime-found name. A lot of these users
come from more static backgrounds and have heard the benefits of dynamic
languages. I have to wonder if these are signs of their over-eagerness
to exploit that dynamic nature.
exec "%s = %d" % (raw_input(), input())

.. container::

   Example of dynamic variable names in action. To a pythoner, obviously
   not pythonic.

d = {}
d[raw_input()] = int(raw_input())

.. container::

   Less bad. This is why dictionaries exist, so we use them. Also, we
   remove the potentially dangerous and frivolous use of input() in
   favor of int(raw_input()).

There are a lot of things that different programming languages are good
for and things they are bad for. There are times when their negative
points can be exploited, of course. There are far more times when their
positive points can be exploited, and turned into disaster. Pointers in
C, for example, are useful in the cases where they are used properly and
smartly, but terrible when wielded by the wrong hand with evil or
ignorant intent. The same can be true for a lot of a dynamic language's
features.
People trying to avoid knowing the names and number of variables they
have, create classes on the fly with runtime information, and build and
evaluate python code in strings are looking at the flexibility of the
language and really want to use that for their own good. The problem is
that great power requires great responsibility, as we all know. What
most of us don't realize, is that great responsibility requires great
wisdom, and we can't buy, read, or request on IRC for wisdom. That means
the great power that lures these new comers to the language is
inevitably what will always keep them from fully experiencing the gifts
it bestows. This is not a flaw or a unique attribute of the language, of
any language, or of anything at all which benefits mankind and requires
knowledge. Just don't exert yourself. Don't do anything for the sake of
paradigms or languages or buzzwords. Solutions are neutral, so solve
them for solution's sake, not implementation's sake.
[foo() for i in range(10)]

.. container::

   An obvious abuse of a list comprehension as a for loop one-liner. (We
   know this, because the resulting list is thrown away.)

What I find the most odd is the reactions these individuals give when
you tell them what they are doing wrong, and what to do instead. If they
want dynamic variable names, we tell them to use a dictionary; they
complain about the inefficiency of hash table lookups versus variable
names (from a C perspective, often). The simple thing I cannot
understand with this is how they expect the dynamic variables work, if
not a hash table. If they think they work like C stack locals, yet can
be dynamic, why would they think that magical technique would not be
applied to dictionaries. In other words, if they recognize they achieve
the same end, why do they think they are such wildly different routes?
Update: I added some examples the day after initially posting this.
