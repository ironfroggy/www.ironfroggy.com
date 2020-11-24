| I've done my first Ludum Dare Jam now, and actually my first game jam
  of any kind. Wow! I am so happy to have finally done this. It was a
  super rewarding experience and I want to share that, and my game, with
  as many people as will listen.
| My game is `Patient Out Of
  Time <https://stonebird.itch.io/patient-out-of-time>`__. It is an
  apocalyptic moody shooter about a doctor salvaging power sources from
  robots in the wasteland to keep the life support of his last patient
  running as long as possible. The hospital staff have all left, and
  they are the only two survivors. Keeping this man alive is all this
  one doctor has to keep him going.
| It is a sad game, but it was also a *lot* of fun to make.

.. container:: separator

   |image0|

| 
| Here are some things I learned this time. I hope to learn more things
  the next Ludum Dare.

Little Steps Make Safe Steps
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container::

   I didn't have time for broken builds or half-built code I needed to
   fight my way back out of just to get the game running again. Every
   change I made had to be broken down into tiny, discrete non-breaking
   changes. Every step of way had to be playable. This kept the game
   constantly in a "technically releaseable" state, which kept stress
   about finishing the game off my back.

Refactoring Can Be Treading Water
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container::

   My habits as a developer tend towards building *systems*. Now, I get
   a lot of enjoyment out of this and preach the merits of systems as
   code design, but I'm trying to learn to cautiously apply this form of
   what is, some times, over thinking things. So, I did my best to
   permit myself to write "bad" code and move forward.

.. container::

.. container::

   I didn't have a lot of assets, so as I added them one by one through
   the process I never built any kind of asset management. That's what
   *old Calvin* would have done. You know, to "clean it up". Instead, I
   just added what I needed to make the new thing work, because spending
   time to change big things would do two negative things:

.. container::

.. container::

   First, it would violate the first rule: Little Steps Make Safe Steps.
   Refactoring is a great way to get lost in the weeds with a
   half-completed bit of work that'll take you hours just to get the
   feature set back to exactly where you started. *No thank you.*

Compromise When You Find a Dead End
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container::

   A lot of problems we come up against as software developments make
   the little voice in our heads say "Oh, I know, I'll just..." and
   then, hours later, we're still struggling with all the pitfalls and
   unforeseen problems with what we thought would be a totally simple
   solution.

.. container::

.. container::

   When you see this, don't forget that you can give up. And I mean that
   in a good way, because some times it just isn't worth it.

.. container::

.. container::

   As an example from *Patient Out Of Time*, I wanted to make the robots
   chasing you avoid the problem of "clumping" too close, which was
   common since they all just headed straight towards you. I started
   experimenting and thinking about different kind of flocking
   algorithms and coordination between the robots. It was all turning
   pretty complicated!

.. container::

.. container::

   Instead, I backed out of all that and just randomized all their
   speeds a little bit. Problem solved with one line.

Add a Little Bit Of Everything
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| I had 48 hours. Technically, I had 72 hours, because I'm doing the Jam
  and not the Compo. However, I do have to work on Monday! And I have a
  family, and I try to avoid burn out. So, really, my time to put into
  this was pretty limited. Still, watching the clock, I was sure to
  rotate my efforts between code and art and audio and design.
| Evenly distributing the effort across the different pieces that make
  the title contributed to that "always releaseable" goal. I didn't wait
  until the very end to figure out sound. I iterated on my art and
  animations interlaced with feature tweaks and bug fixes. Everything
  grew up together.
| This also meant I got practice and new experience with everything. I
  did some audio sample editing. I worked on my pixel art animation
  skills. My skills with the Love2D platform I've been using were
  improved a bit. Every muscle got a little exercise.

Have Fun
~~~~~~~~

I highly recommend trying out Ludum Dare some time. If you do, don't
take it too seriously. Have fun!

.. |image0| image:: https://4.bp.blogspot.com/-Al5zozW9Zcs/WX6FhsxxgpI/AAAAAAAAM_0/Jdu_tI7sO2YygYdNsf_6QzGcGiGn8NqeQCLcBGAs/s320/ldjam39-2.gif.gif
   :width: 320px
   :height: 249px
   :target: https://4.bp.blogspot.com/-Al5zozW9Zcs/WX6FhsxxgpI/AAAAAAAAM_0/Jdu_tI7sO2YygYdNsf_6QzGcGiGn8NqeQCLcBGAs/s1600/ldjam39-2.gif.gif
