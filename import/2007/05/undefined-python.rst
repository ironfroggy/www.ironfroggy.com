| `Will McGugan <http://www.willmcgugan.com/>`__ has a
  `post <http://www.willmcgugan.com/2007/05/11/the-smell-of-c/>`__ about
  the smell of languages, using an example of code from C that is
  actually completely undefined: no one knows what it should do. The
  code in question is this:

.. code:: c

   int main() { int i = 5; i = ++i + ++i; printf ("%d", i); }

| One of the commenters talks about how some constructs in Python can be
  undefined, but I
  `disagree <http://www.willmcgugan.com/2007/05/11/the-smell-of-c/#comment-1094>`__.
  My response is below.

.. container::

   There can certainly be some cases where you aren’t sure about things
   involved in Python, but nothing undefined in the sense that C can be.
   I can counter the examples given.

   “While a list is being sorted, the effect of attempting to mutate, or
   even inspect, the list is undefined.”

   - While the list is being sorted, any inspection or mutation could
   only be occuring in some other thread. Multiple threads are, by
   desogn, indeterminable.

   “Formfeed characters occurring elsewhere in the leading whitespace
   have an undefined effect (for instance, they may reset the space
   count to zero).”

   - This is caused by improper formatting of a text file. If the file
   is not formatted properly, you can’t expect magic its-OK-ness.

   “super is undefined for implicit lookups using statements or
   operators such as “super(C, self)[name]””

   - Undefined? I actually don’t agree. At least, not by the term
   “undefined” as used in this post. implicit lookups like this are
   looked up on the type of the object in question, which is the super
   builtin type, in this case. The methods are undefined in the sense
   that the type does not define them, so they don’t exist. You can’t
   look them up. This is not “undefined” as in not knowing the behavior.

   “If the transformed name is extremely long (longer than 255
   characters), implementation defined truncation may happen.”

   - This is about private name mangling. The mangled names should be
   considered an implementation detail, you should never use or try to
   create the names manually, so any implementation specific differences
   are completely irrelevant.

| 

| 
