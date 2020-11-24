.. container::

   This is the inaugural post in my Dead to Me! series\ \ `which I
   announced <http://techblog.ironfroggy.com/2014/10/dead-to-me.html>`__\ \ .
   I’m not gonna lie. I’m pretty proud of this one. To say Trapdoor was
   ahead of the times might be a stretch, but really only asmallstretch.

**
**

.. container::

   My project README explains

**
**

.. container::

   Trapdoor is a web-based desktop framework. Confused yet? The idea is
   to leverage how much energy is put into the web today and make
   developing a desktop applicationfunagain. Again? For the first time?

**
**

.. container::

   Trapdoor was an exploration of how to utilize web development
   skillsets to build desktop tools. I wanted to experiment with how
   this idea would play out and if it really made any sense. I was never
   planning Trapdoor to become are solution. I just wanted to play with
   the idea, but I do think I played with the idea pretty early on and
   that it was anextremelysuccessful experiment.

**
**

.. container::

   At the time I was still a KDE user and had been learning a little bit
   of Qt via the Python bindings PyQt4. I knew that Qt had a WebKit
   widget and quickly found that PyQt4 exposed this pretty easily.

**
**

.. container::

   This was a simple demo I built with Trapdoor. We have a web-app
   built, for this simple example, all in Javascript dumping a few
   simple controls to the DOM. The JS is responsible for window creation
   and gets access to the DOM in the new window, where it can construct
   an interface in HTML and use jQuery to wire it up.

**
**

.. container::

   What I was most proud of is that, recognizing this would only be
   useful if the desktop applications being built could do anything a
   normal desktop app could do, I made itreallyeasy to extend the
   Javascript APIs with new things.

**
**

.. container::

   The Calculator class defined in the above calculator.py file above
   and registered in the manifest is able to expose methods to the
   Javascript API it injects into the application. Otherwise, it is just
   regular everyday Python and can do anything and can use any Python
   libraries.

**
**

.. container::

   I only worked on Trapdoor for three days. Vaguely I recall wondering
   if I could write an extension that used PyOpenGL to render 3D
   graphics in my web-based desktop application, a good year before the
   WebGL spec landed and three and a half years before work would begin
   on Node Webkit. Trapdoor won’t be worked on by me and shouldn’t be
   picked up by anyone else, probably. It will continue to sit in my
   Github for a while, but it stay forever among my favorite personal
   projects.

`Check it out, if you’re
curious. <https://github.com/ironfroggy/trapdoor>`__
