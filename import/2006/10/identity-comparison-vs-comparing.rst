| An explaination of the virtues of foo is not None over foo != None
  lead to an explaination of identity comparison with the is operator. A
  fellow equated this to, roughly, id(a.x) == id(b.x), which I told him
  was roughly correct but probably not actually correct. It only took a
  little bit of through to see how uncorrect it was.
| The following code creates a simple class with one property descriptor
  (read-only). It solves the requirements that with to instances of this
  class, a and b, id(a.x)==id(b.x) can be true while a.x is not b.x! How
  does this happen?

::

   class foo(object):
     x = property(lambda s: id(s))
   a = foo()
   b = foo()
   assert id(a.x) == id(b.x)
   assert a.x is not b.x

| 
| How on earth does this code prove what it does? a.x and b.x are
  created on the fly, passed to the id function, and then destroyed with
  no references left. Because they are both created in the right order
  with the id(a.x)==id(b.x) expression, they just happen to get the same
  memory addresses, which in CPython is used for the id function's
  result. This leads to misleading results, so don't rely on them in
  such ways. Identification is what it is, and you shouldn't try to
  break it down.
