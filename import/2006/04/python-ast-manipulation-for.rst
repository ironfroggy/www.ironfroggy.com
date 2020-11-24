| A lot of work has been going on with the Python AST and being able to
  manipulate it for more runtime uses. This is a generalized suggestion
  for something we could do in the Twisted community to utilize this.
  Given a simple function like this:
| 

::

      def processPage(url):
          d = getPage(url)
          d.addCallback(cb_processPage)
          d.addErrback(eb_processPage)
      def cb_processPage(page):
          print page
      def eb_processPage(error):
          print "Could not load page. Error: ", error

| 
| We write like that, but what we really mean, and just need to express
  in a more difficult manner, is:

::

      def processPage(url):
          try:
              print getPage(url)
          except LoadError, e:
              print "Could not load page. Error: ", e

| 
| What I want to know, is can we take the second example and process the
  AST branch to produce the first example? Lets step through and see how
  it would work. First of all, we need to know what is deferred. A
  simple way would be to check every function return and determine if it
  is a deferred, but there may be more efficent methods we can discover
  later. For any possibly deferred call, the expression it is a part of
  can be refactored out into its own function, as can the exception
  handler code. When a deferred is detected, the callbacks can be
  attached and if the operation is not deferred, the callbacks can be
  used directly. This might even bring about something slightly new:
  optionally deferred operations. Instead of using defer.succeed and
  such, returning a deferred could cause code to handle the deferred
  properly, which would otherwise act in a normal syncronous manner.
  Depending on just how the AST stuff progresses, maybe the returning of
  the deferred could trigger the inspection of the calling function to
  inject the deferred handling code, so only functions that ever get a
  deferred will need processing.
