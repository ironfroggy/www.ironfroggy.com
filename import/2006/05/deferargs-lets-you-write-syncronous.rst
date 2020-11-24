| So a little side project for my own uses provided a simple decorator
  that lets me write a function I can pass deferreds and regular
  arguments to, and have the function return a deferred that fires when
  all of its deferred arguments are ready and the function has processed
  them. Some example usage:

::

   @deferargs
   def printArgs(*args, **kwargs):
       print "Positional Arguments: ", ", ".join(args)
       print "Keyword Arguments: ", ", ".join("%r=%s"%(k,v) for (k,v) in kwargs.items())

   printArgs("foobar", baz=someNetworkRequest())

| 
| Really basic, but it can prove useful for a large portion of Twisted
  code you might write. I'm planning to add some semi-evil way to do
  something that looks a lot like a try/except/finally block but is
  actually (obviously) not, and works with any errbacks from deferreds
  within the try-like block of code. The reaction has been interesting.
  I've had some people stand up for the idea, which is similar to

::

   defgen

| , and others who think it is a bad idiom that is dangerous to
  encourage.
| Using this kind of abstraction over asyncronous code, you do have to
  be careful to remember what is asyncronous and take consideration that
  your code won't run until all deferred arguments are ready, even if
  some parts could be run with only some of the arguments. In those
  cases, however, you should just break up the function, and I'd like to
  note that you can make the same mistakes using deferreds and the like
  directly, so I don't really see it as an issue.
| If you want to do any error handling for the moment, you need to
  attach errbacks to the deferred from the function call. I want to work
  in my semi-evil error handling soon, because my goal here is to hide
  the fact that there are deferreds as much as possible, but for now
  this is just fine, and I've already had use of it myself.
| You can get it from the Cheeseshop, so check it out
  `there <http://cheeseshop.python.org/pypi/DeferArgs/0.1>`__ now and
  place any comments about it here.

.. container:: tag_list

   Filed in:
   `twisted <http://del.icio.us/ironfroggy/twisted>`__\ `python <http://del.icio.us/ironfroggy/python>`__
