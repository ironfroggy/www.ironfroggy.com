This project may never become a serious thing, but it is fun. I intend
to write an introductory post on the project, but for now I just want to
post two code examples that should peek some interest.

.. container::

.. container::

   # counter.py

.. container::

   .. container::

      from trapdoor.extension import Extension, Factory

   .. container::

   .. container::

      class Counter(Extension):

   .. container::

   .. container::

          value = 0

   .. container::

   .. container::

          @Extension.method()

   .. container::

          @Extension.returns(int)

   .. container::

          def get(self):

   .. container::

              self._result = self.value

   .. container::

   .. container::

          @Extension.method()

   .. container::

          def incr(self):

   .. container::

              self.value += 1

   .. container::

   .. container::

      counter = Factory(Counter)

.. container::

.. container::

   and,

.. container::

.. container::

   // counterdemo.js

.. container::

   .. container::

      WindowManager.createWindow();

   .. container::

   .. container::

      document.write('<input id="a" />' +

   .. container::

      '<br />'+

   .. container::

      '<input onclick="window.t = window.t - 100;" name="faster"
      value="faster" type="button" />'+

   .. container::

      '<input onclick="window.t = window.t + 100;" name="slower"
      value="slower" type="button" />'+

   .. container::

      '<input id="t" />');

   .. container::

   .. container::

      var t = 500;

   .. container::

      var globalcounter = counter.create();

   .. container::

   .. container::

      function update() {

   .. container::

          $('#t').val(typeof globalcounter.get);

   .. container::

          $('#a').val(globalcounter.get());

   .. container::

          globalcounter.incr();

   .. container::

   .. container::

          window.setTimeout(update, t);

   .. container::

      }

   .. container::

   .. container::

      window.setTimeout(update, t);

.. container::

.. container::

   The result is a simple desktop app.
