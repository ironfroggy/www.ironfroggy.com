Previously I made a `little
preview <http://techblog.ironfroggy.com/2010/12/how-to-tease-everyone-on-christmas.html>`__
of something I'm announcing today, but it is a soft announcement as I've
had it on github for some time, but I haven't done anything with the
project.

.. container::

.. container::

   This is just a prototype, an experiment, and it is called Trapdoor. I
   don't remember why I named it Trapdoor.

.. container::

.. container::

   Trapdoor has a simple concept, along the lines of Mozilla Prism. I
   wanted to take things I use to build web applications and test how
   they could be applied to building desktop applications. This meant
   two things:

.. container::

.. container::

   1) I need to wrap up a web application in something that can be run
   locally.

.. container::

.. container::

   2) I need some way to extend a web application in ways that normally
   only desktop applications can provide.

.. container::

.. container::

   This has been done in the simplest way I could find, at the time, and
   is `available on github <https://github.com/ironfroggy/trapdoor>`__.

.. container::

.. container::

   ::

      extensions:

       - calculator.Calculator

      js:

       - calculator.js

      plugins:

       - trapdoor.contrib.windowmanager

.. container::

.. container::

   Applications are configured through this simply manifest, where they
   are given extensions, plugins, and javascript. Honestly, extensions
   and plugins can probably be merged. They are both defined by a Python
   class and the object exposes methods to the Javascript, which gets
   loaded and initialized by the runtime. The current version includes
   two plugins:

.. container::

.. container::

   trapdoor.contrib.windowmanager

.. container::

.. container::

   This is a basic plugin that provides a simple createWindow method,
   through which the Javascript can create new windows with (in the
   future) more control than the standard Javascript APIs would
   otherwise provide. One thing I'll be adding to this is a fullscreen
   API and other properties to control the window appearance, such as
   borders and which controls are visible.

.. container::

.. container::

   trapdoor.contrib.nodes

.. container::

.. container::

   This is my favorite of the two standard plugins. Each Node is an
   isolated Javascript runtime, in its own global space. The application
   is loaded in the first node, but it can create and initialize others,
   allowing it to run untrusted Javascript safely. If I continue
   development, I hope to use this to test ways to allow community
   additions to software without worrying about what they are running.
   This is similar to how extensions and user scripts work in Firefox
   and Chrome.

.. container::

.. container::

   Now, I don't know if more will come of this. I think, if it does, it
   should probably be evaluated if I should rewrite it based on Chromium
   and V8, rather than Qt and whatever Javascript engine it is running
   on. It is also lacking a solid use case, for me, that I can use to
   drive my desire to improve it. However, I had fun writing it for the
   thought experiment, and I do hope to do more with it in the near
   future.

.. container::

.. container::

   Please, fork it and tell me what you think.
