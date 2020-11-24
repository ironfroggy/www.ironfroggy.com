Just let `these
guys <http://code.google.com/p/python-multiprocessing/>`__ do it for
you.

.. container::

.. container::

   My hats off to them for this contribution to the community. It is
   much appreciated and will find use quickly, I'm sure. I know I have
   some room for it in my toolbox. Hopefully, the changes will be taken
   back to the 2.6 line so that any bugfixes that come will help stock
   Python and the backport.

.. container::

.. container::

   So, if you don't follow 2.6/3.0 development you might not be aware of
   multiprocessing, the evolution of integrating the pyprocessing module
   into the standard library. It was cleaned up and improved as part of
   its inclusion, so its really nice to have the result available to the
   larger Python user base that is still on 2.5 and 2.4. Although some
   edge cases might still need to be covered, the work is stable
   quickly.

.. container::

.. container::

   Here's an overview incase you don't know, so hopefully you can see if
   it would be useful for any of your own purposes. I think, starting
   out, there is more potential for this backport than the original
   multiprocessing module. Thus, I hope this introduction is found
   useful by a few people.

.. container::

.. container::

   .. container::

      >>> from multiprocessing import Process, Pipe

   .. container::

      >>>

   .. container::

      >>> def f(conn):

   .. container::

      ...     conn.send([42, None, 'hello'])

   .. container::

      ...     conn.close()

   .. container::

      ...

   .. container::

      >>> parent_conn, child_conn = Pipe()

   .. container::

      >>> p = Process(target=f, args=(child_conn,))

   .. container::

      >>> p.start()

   .. container::

      >>> print parent_conn.recv()   # prints "[42, None, 'hello']"

   .. container::

      [42, None, 'hello']

   .. container::

      >>> p.join()

   .. container::

   .. container::

      This is an example from the multiprocessing docs, utilizing its
      Pipe abstraction. The original idea was emulating the threading
      model. The provisions are basic, but give you what you need to
      coordinate other Python interpreters. Aside from pipes, there are
      also queues, locks, and worker pools provided. If you're working
      on a multicore system with a problem that can be broken up for
      multiple workers, you can stop complaining about the GIL and
      dispatch your work out to child processes. Its a great solution
      and this makes it a lot easier, giving the anti-thread crowd a
      nice boost in validation and ease-of-convincing. That's a good
      thing for all of us, because it means software that takes
      advantage of our new machines and more people who can write that
      software without the problems threading always gave us. Of course,
      some problems, like locks, can be problematic in the wrong
      situation, so don't think I'm calling anything a silver bullet.
      The point is, it improves. Nothing perfects, and I know that.
