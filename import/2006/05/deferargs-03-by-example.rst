| DeferArgs 0.3, just a few hours after 0.2, is now released
  `here <http://cheeseshop.python.org/pypi/DeferArgs/0.3>`__. The only
  update is support for attemp/catch-all blocks without any @catch(type)
  handlers. In response to some people in #twisted@irc.freenode.net,
  here are examples that show what can be done more clearly.
| To write any function that can accept deferred arguments nicely:

::

   @deferargs
   def printArgs(*args, **kwargs):
       print args
       print kwargs

| 
| To add psuedo-exception handlers and a psuedo-finally block to a
  @deferargs decorated function:

::

   @deferargs
   def printArgs(*args, **kwargs):
       print args
       print kwargs
       print "This one is important! ", kwargs['important']
   @catch(KeyError)
   def onKeyError(e):
       print "There was no important kwarg!"
   @catch()
   def onAnyError(e):
       print "Crap!"
   @cleanup()
   def _(r):
       print "Every thing is done."

| 
| There is also a model for a psuedo-try block, which basically
  decorates just calls the function immediately when you define it and
  its catch/cleanup handlers:

::

   @attempt
   def this():
       assert False
   @cleanup
   def _(r)
       print "And thats it."
