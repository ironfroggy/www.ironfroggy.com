Hashtrack.js 0.2 includes a number of bug fixes and enhancements, and
I'd like to start doing official releases that really show off what the
tool is capable of. I've been using this for a few years in projects
both personal and professional, and I always merge improvements back
into it. Hopefully, I can start making an effort to polish it up better,
because in this day and age we all are finding ourselves in need of
stateful web applications, and we need to handle this gracefully.

.. container::

.. container::

   Take a look at the `github
   repo <http://github.com/ironfroggy/hashtrack/>`__ for hashtrack if
   you like the sample code below, or take a look at the very sparse but
   `informative docs <http://ironfroggy.github.com/hashtrack/>`__.

.. container::

.. container::

   ::

       hashtrack.onhashvarchange("background", function (value) {
           $('body').css('background', value);
       }, true);

   ::

   ::

       -----

   ::

   ::

       <a href="#?background=green">Make the background green</a>
