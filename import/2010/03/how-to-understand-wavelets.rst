.. container::

   I got acquainted with developing against the Google Wave Preview last
   week, and I'll be doing more of it this week. There are still many
   gaps in the documentation and in the public understanding of what
   exactly is going on in a lot of cases. This post is halfway between
   an introduction to Wave development and a story of my personal
   hurdles in my first experiments working with it.

.. container::

   One of the first things you'll find in the Wave documentation is a
   diagram I have reproduced here. \ **This diagram is wrong.**

.. container::

   |image0|

.. container::

   You're going to notice something when you look at this diagram and
   play around with Wave itself, the web client. You're going to realize
   you have no idea what the difference between a Wave and a Wavelet is.
   You don't seem to be able to even see the term "Wavelet"
   appear \ *anywhere* in the application! What's more, everything the
   API docs describe a Wavelet as is what the UI seems to call a Wave.
   This was really confusing to me and I know I'm not the only one
   confused.

.. container::

   It took me a little bit of time to get the perspective to understand
   what I missed. Correcting my diagram with that information produces
   this:

.. container::

.. container::

   |image1|

.. container::

   See what was missing there? The missing piece was the all-too-subtle
   connection, not between Wave and Wavelet, but between individual
   waves. The official documentation diagram places the waves in
   parallel and mislead me to look in the wrong mindset for the
   distinction between Wave and Wavelet in the presentation context.

.. container::

   So how does this pan out in the user interface of Wave? Private
   replies. A private reply to any blip/reply will create a new Wavelet
   with two participants: the creator of the blip you reply to and
   yourself. (Actually, you can create a single-participant child
   wavelet if you reply to yourself privately.)

.. container::

   I'd like to try some experiments and see if and how the interface
   would present setups like a child wavelet with completely different
   participants from the parent wavelet. I'm investigating the use of
   these as sort of hidden data channels in a Wave. For example, the
   Robot I am developing might store some auxiliary data about the waves
   it gets used in via private replies to itself. 

.. container::

   Now, since I'm probably going to be spending a good bit more time
   with Google Wave in the weeks to come, I expect to document more of
   the things I'll learn along the way. If you're interested, let me
   know what you're doing or thinking about doing with Wave.

.. |image0| image:: http://docs.google.com/drawings/image?id=sR6-gW8dl44pAZnwzGq9KyQ&w=400&h=400&rev=74&ac=1
.. |image1| image:: http://docs.google.com/drawings/image?id=sDY6uxvDotqJuRw5hFMLf2w&w=400&h=400&rev=49&ac=1

