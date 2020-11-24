| |image0|\ This until-recently-lonely module only houses two
  alternative collection types, deque and defaultdict, but promises
  useful things today and more to come. Anytime we have a good place to
  put things, we find more things to put there. With the new defaultdict
  type, collections is finally more than just that thing you use to get
  a deque: its a full fledged utility library. More optimized collection
  types (chains, B-Trees, and bags, anyone?) are sure to come, so keep
  your eye here every new Python release changelog, and maybe you'll get
  an early Christmas present.

| Here is a quick rundown of what is offered today, using possibly silly
  examples.

::

   d = deque()
   d.extend(xrange(10))
   while d:
     print d.popleft()

| 
| What you see here is that deque acts like a list but has mirror
  versions of many end-modifying operations, like append, extend, and
  pop, which operate on the 'left' side. A list is far less efficient
  with insertion and popping from anywhere but the end of the list. This
  makes deque great for First-In-First-Out structures, where a list is
  more suited for a First-In-Last-Out setup.

::

   dd = collections.defaultdict(lambda: None)
   dd['a'] = 1
   dd['b'] = 2
   print dd['c'] or 3

| 
| Here we automatically handle a non-existant key with a default value,
  None. A factory callable is used, so that we can actually return
  different values, but we don't get the key. One interesting use is
  itertools.count().next as the factory, which means every missing key
  is automatically filled with an automatically incrementing integer.

.. |image0| image:: http://www.gemfix.com/images/stones/garnet_green/demantoid_18.jpg
   :target: http://www.gemfix.com/images/stones/garnet_green/demantoid_18.jpg
