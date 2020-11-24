I want to use Twisted.web for some projects, and I haven't used it in
years. I'm relearning and I feel like a novice all over again, as I
should, given the years that have passed since I have seriously looked
at any twisted code. I miss it, very much. Want to relearn or learn for
the first time? I can't stress enough the excellence of a quick pass
through the examples of `Twisted.web in 60
Seconds <http://twistedmatrix.com/documents/10.1.0/web/howto/web-in-60/index.html>`__.
Go through those immediately. Afterwards, I `read
up <http://twistedmatrix.com/~glyph/sphinx-preview-11.0pre1/projects/web/howto/twisted-templates.html>`__
on the new twisted.web.template, which is based on the Nevow templates I
worked with so long-feeling ago, and I'm pretty happy with what I see
there. I'm wondering how well it will produce HTML5 compliant markup,
not that it is very strict, but it looks pretty clear.

.. container::

.. container::

   My brain still thinks in asynchronous operations and I constantly
   have to unravel those thoughts and figure out how to express them,
   non-ideally, in a synchronous workflow. This is becoming tiring, and
   while I don't plan on leaving Django, I do plan on giving my brain a
   rest. Maybe I'll find a way to combine my two interests in the near
   future...

.. container::

.. container::

   This is the result of the hour I spent relearning last night.

.. container::

.. container::

   .. container::

      ``import time``

   ````

   .. container::

      ````

   ````

   .. container::

      from twisted.web.server import Site, NOT_DONE_YET

   .. container::

      from twisted.web.static import File

   .. container::

      from twisted.web.resource import Resource

   .. container::

   .. container::

      from twisted.internet import reactor

   .. container::

      from twisted.internet.defer import Deferred

   .. container::

   .. container::

      class ClockPage(Resource):

   .. container::

          isLeaf = True

   .. container::

          def render_GET(self, request):

   .. container::

              d = Deferred()

   .. container::

              @d.addCallback

   .. container::

              def \_(r):

   .. container::

                  request.write("<html><body>%s</body></html>" % (r,))

   .. container::

                  request.finish()

   .. container::

   .. container::

              def get_time(r):

   .. container::

                  d.callback(time.ctime())

   .. container::

   .. container::

              reactor.callLater(2, get_time, None)

   .. container::

              return NOT_DONE_YET

   .. container::

   .. container::

      resource = ClockPage()

   .. container::

      factory = Site(resource)

   .. container::

      reactor.listenTCP(8888, factory)

   .. container::

      ``reactor.run()``

.. container::


