We learn to recognize a bad bit of code quickly as our code-fu grows.
Arbitrary side-effects smell badly and crazy one-liners frustrate us. It
becomes easier to identify what lines of a codebase you might want to
clean up to improve the overall quality of the work.

.. container::

.. container::

   There is a line between codebaess with bad code in them and bad
   codebases. When do we learn to recognize this and what are the signs
   that the problem is far reaching, not localized? A bad codebase is an
   expensive codebase. It is difficult to work with and difficult to
   collaborate with others on. Identifying what makes a codebase bad is
   key to knowing when, where, and why to improve it. Improving the
   overall code quality reduces the overall code cost. I'm thinking
   about software in economic terms these days, and I'm hoping we can
   turn the recession to our favor by pushing the mantra Bad Code is
   Expensive Code.

.. container::

.. container::

   Costs of code come from three actions. Adding features costs, fixing
   bugs costs, and understanding costs. Adding features is an obvious
   source of code cost, and every time you want to expand a products
   abilities you're going to pay appropriately. Fixing bugs is both
   obvious and subtle. Where its obvious that you need to fix bugs you
   see, it can be very subtle when costs are added that you can't
   actually detect (more on this later). Understanding the code, to most
   minds, might be entire subtle and never obvious. New developers,
   existing developers moving to new areas, and users trying to
   understand the behavior emerging from the collection of code all need
   to understand these things and the most expensive to understand it
   the less likely they will.

.. container::

.. container::

   I feel no need to expand on the cost of adding to a codebase. What
   will hit us are the subtle points. Bugs' cost explode against the
   subtle misunderstandings, leading to the conclusion that a lack of
   understanding the code is the single greatest source of increasing
   its cost. This is through the partial obvious needs to understand the
   code and the more subtle costs they add to being able to fix bugs,
   and even to properly expand the feature set. The problems manifest as
   the actual bugs in the software.

.. container::

.. container::

   The sign of a bad codebase is a difficult to debug codebase.

.. container::

.. container::

   Now we only need to know the causes of difficult debugging to know
   the signs of a bad codebase.

.. container::

.. container::

   Does the codebase lack tests? No tests mean you can't be sure any
   change breaks more than you intended to fix. Locating the source of a
   problem is hugely expensive when you're manually verifying
   correctness, instead of via automated testing. There are fantastic
   techniques of binary debugging, narrowing a changeset range down to
   the extra change that introduced a bug. This is so expensive with
   manual testing that it might as well be impossible, while with tests
   its one of the greatest debugging tools you could ever have at your
   disposal: It can automatically tell you exactly what code caused your
   bug. It can debug for you, but only in a codebase that started out
   good.

.. container::

.. container::

   Does the codebase lack documentation? If your understanding of the
   code comes mostly from trial and error or asking other developers,
   then you lack documentation or enough clear code to self-document.
   Every time you add a feature or fix a bug, you're debugging more than
   the code, but your understanding of how it functions. Clear code,
   concise comments, and good documentation let you focus on the
   breakage of the code, and not the breakage of your understanding of
   its design.

.. container::

.. container::

   Does the codebase grow or shrink? We might think a growing codebase
   is a generally universally good sign, but its not so. A shrinking
   codebase can be a great sign. It means two things. Firstly, it means
   an increase in the quality when the amount of code reduces while
   maintaining or increasing the value (not to be confused with cost) of
   the code. For example, if you can make a function clearer but finding
   more concise ways of expressing the same ideas, you reduce how much
   code there is to understand to get the same job done. A shrinking
   codebase also tells you that the code is understandable enough to be
   refactored, which is a little deceptive. The better quality of your
   code, the easier it becomes to improve the quality even futher.

.. container::

.. container::

   Take this as a three point test. How do your current projects score?
