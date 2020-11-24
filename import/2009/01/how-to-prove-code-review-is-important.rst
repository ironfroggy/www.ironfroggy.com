The infamous Zune 30GB failures were traced to a leapyear issue, and
apparently they use some code we can see in the Freescale codebase. Take
a look at the following sample of code, which determines the year from
the day number (counting from January 1, 1980). I don't know about you,
but the infinite loop is immediately obvious. On a leapyear, the main
loop continues when days = 366 and the incrementing is never reached,
because days > 366 fails.

.. container::

.. container::

   Am I naive to think that even a casual code review would have caught
   this in a moment?

   .. container::

   .. container::

      .. code:: alt2

         year = ORIGINYEAR; /* = 1980 */
         while (days > 365) {
              if (IsLeapYear(year))
              {
                  if (days > 366)
                  {
                      days -= 366;
                      year += 1;
                  }
              }
              else
              {
                  days -= 365;
                  year += 1;
              }
         }

**UPDATE:** Fixed formatting issues. It looked fine when I posted it,
honest!
