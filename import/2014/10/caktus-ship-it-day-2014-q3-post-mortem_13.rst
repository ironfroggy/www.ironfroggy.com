| As of my `first hour playing
  around <http://techblog.ironfroggy.com/2014/10/caktus-ship-it-day-2014-q3-post-mortem.html>`__
  I was able to share and synchronize play of any MP3 between multiple
  users with a simple drag and drop interface. Things were going pretty
  well for my project, but I had some work to do getting from there to
  the collaborative playlist I had in mind.
| I was already just assuming we were only caring about one file,
  because that worked well to get things up and running fast. My next
  step was to remove that assumption and start keeping a list of songs.
  This was pretty easy, in fact. I started writing a simple list of
  songs as they were downloaded, each with a play button which performed
  the <audio> tag set and play that previously done automatically. Each
  user could now play any song that was shared and to restore the
  previous synchronized playing that happened when they only dealt with
  a single done I incorporated broadcast changeTrack messages. I added
  two other broadcasts, pause and play, which would allow any users to
  pause and play the songs on all users simultaneously.
| This was working well, and I had roughly scaled my previous prototype
  to a multi-song version. Unfortunately, this version was even more
  rough and bug-ridden than the first. Most importantly among its
  faults: I couldn't really predict the order different clients would
  receive each track, so the playlists wouldn't remain in the same order
  for everyone. I wasn't really ready to tackle the actual collaborative
  playlist problem. This is probably the most difficult problem the
  project will face. It is a lot harder because I'm determined to keep
  the entire thing peer-controlled with no central decided or
  coordinator.
| After banging my head on the simplest way I could provide this editing
  for the initial version, but coming up short, I realized it was a
  waste of my time. I didn't really need to do collaborative editing for
  a prototype, I just needed to make sure they all kept the same order.
| So I alphabetized the songs for all users.

The simplest solution to some problems is not to have them
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. container::

   At this stage I could play any song on the shared playlist and hear
   it on any connected machine. Things continued nicely.

.. container::

.. container::

   Implementing playlist progression was pretty easier. Along with
   progression I added highlights on the list to show which song was
   currently being played.

.. container::

.. container::

   I decided at this point to do a bit more seriously testing and
   increased my test set of songs I was drag and dropping from 3 to 8.

.. container::

.. container::

   I crashed Chrome. How I did that and how much of this work I had to
   completely throw out the window? Read Part 3 (Coming Soon) to find
   out.

.. container::

.. container::

   .. rubric:: Part 1:\ \ `Proof of Concept in Under an
      Hour <https://draft.blogger.com/>`__
      :name: part-1-proof-of-concept-in-under-an-hour

   .. rubric:: Part 2: Playlists and Reseeding Songs
      :name: part-2-playlists-and-reseeding-songs

   .. rubric:: Part 3: Two Steps Back and Three Steps Forward
      :name: part-3-two-steps-back-and-three-steps-forward
