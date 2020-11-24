| Continuing discussions in #twisted about the benefits and complaints
  of my deferargs drove me to add more things and release pretty often
  today. This is `version
  0.4 <cheeseshop.python.org/pypi/DeferArgs/0.4>`__. New is tests and
  ability to move the functionality to the callsite, so you can do this:

::

   def printArgs(*args, **kwargs):
       print args
       print kwargs
   deferargs(printArgs)(10, defer.succeed(20))

| 
| Also, and I don't know how useful this will be, you can not define
  specially handled argument types, such as lists that might contain
  deferreds. These are optional, and not enabled by default. Lists are
  the only special type handled so far. Use it as follows:

::

   @deferargs([list])
   def printList(l):
       print l
   printList([1,2, defer.succeed(3)])

| 
| I might add dictionaries, sets, and tuples to the next release.

.. container:: tag_list

   Filed in:
   `programming <http://del.icio.us/ironfroggy/programming>`__\ `python <http://del.icio.us/ironfroggy/python>`__\ `twisted <http://del.icio.us/ironfroggy/twisted>`__
