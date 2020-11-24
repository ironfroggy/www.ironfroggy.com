.. container::

   This is probably taken as the concept for a horror novel by many, but
   bare with me as I am going somewhere productive with this line of
   thought. There are a number of valuable ideas in Django, even if they
   aren’t original. I think some of the concepts could be interesting if
   applied to Twisted. We can’t start over, but maybe we could bridge
   the gap.
   The Project
   A “Project” is a very vague concept that we all start when we’re
   doing something new, but in a system like Django it is a codified
   piece of the framework. What a project is, how it is structured, and
   where its boundaries lie are all documented carefully. This provides
   an obvious starting point and creates a wonderful sense of
   consistency from one project to the next.
   The Application
   Within a Django project one or more Django applications are combined,
   and each application provides a unit of reusable functionality. This
   might consist of DB models and views to aid in tagging objects,
   providing search indexes, or generating thumbnails from uploaded
   photos. Like the Project itself, the application is documented by
   Django in terms of its boundaries and structure.
   If Twisted Took A Page From the Django Book?
   I think we can make a case for borrowing these concepts and patterns.
   The running theme is breaking large things up into reusable chunks
   and defining the boundaries and interactions in ways that we can
   connect them largely via configuration. Can this work with Twisted? I
   think it can, in specific areas.
   We can probably borrow the Project unit directly, add a script to
   every project that runs twistd and loads commands, like the manage.py
   in Django. A standard settings module to configure a project is an
   obvious choice.
   At the next level we would configure smaller, reusable parts the
   project would bring together. Instead of a urls.py, we might define a
   ports.py, which we use to map the interfaces we listen on and the
   services that handle them.
   I think we can’t map “Application” to any one concept, but need a
   variety of types of reusable things. That is fine and Django does the
   same. We talk about apps all the time, but we also have Request
   Middleware, Context Middleware, etc. Twisted has a lot of room for
   configurable middleware.
   This is certainly something that deserves more thought.
