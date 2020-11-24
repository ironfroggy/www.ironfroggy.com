| James went along with the idea of moving away from CVS quicker than I
  thought and we put the plan into action last week. I put in the time
  to the project and started off with the default CVS replacement:
  Subversion. I really was looking forward to using it at work, until a
  friend made a subtle suggestion to look closer at the git project,
  which Linus Torvalds is heading as the version control system of
  choice for some little thing he's writing called Linux. Needless to
  say, I was skeptical, given the track record of the developer.
| Quicker than I realized, I was falling head over heals for the
  examples of git use I was seeing. I cooked up a latest stable for OS
  X, as the installer I found was 130MB from the 1MB source tarball.
  Universal binaries on a project that generates about 145 distinct
  executables is a real bitch. I whipped up a little script to name
  ``git`` and toss into ``$PATH``, while keeping all the ``git-*``
  executables and other files tucked away in ``/usr/local/git/``. I've
  cleaned that up and `released it <#git-osx-binaries>`__ for anyone
  else interested in a clean git install on OS X. I may be releasing
  more git related work in a the near future, if you read on.

For Development Sanity This Means...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 
| As a team grows out of a few developers and reaches nearly a handful,
  you need to start thinking more about development processes. Fixing a
  bug quick while in the middle of a half-finished change is a real
  problem, especially if you've commited already. Multiple developers
  working on separate projects can also be difficult to manage, if you
  don't think about things. These were among our concerns. Also among
  these concerns was the benefit of making the switch *before* bringing
  anyone else on board.
| We had seven CVS modules and I developed a script that imported each
  of them to a new git repository and them merged them in the same
  layout as we had by checking out all our modules into the same
  directory. Keeping them together was a good move, and we kept our
  whole history.
| Branching was one of the core driving motivators and I was thrown back
  when I found branching not doing what I expected in git. Branches in
  git are local, and although you may often push or pull between
  branches named the same on different repositories, they are not really
  related. I got to work on developing a set of branching tools, and I'm
  very happy with what I did in a small amount of time. The
  functionality is pretty complete. We can create, share, merge, and
  switch branches easily. I've even implemented automatic stashing and
  restoring of working copy changes that haven't been commited when
  switching between branches!

For Released Work This Means...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 
| The tools are proving fun to work on when some issue comes up where
  they could be improved. They began life as a set of shell scripts, but
  they will very likely evolve into Python scripts to facilitate their
  future improvement. They are also very likely to leave the repository
  which they themselves are in control of. That was a headache to get
  proper.
| When they are converted to Python I am going to release them. I really
  want to actually publish the git repository, but I need to figure out
  how to do that and if we can do it securely from work somehow. It
  would be nice to do that, such that the repository is always up to
  date with what we have. I'll probably mirror them to
  http://repo.or.cz/.
| I've also placed the git binaries for OS X in two bzip2 compressed
  tarballs. ``git-1.5.3-osx-intel.tar.bz2`` is everything you really
  need, placing only a single ``git`` executable into the path. You can
  grab
  `git-1.5.3-remote-osx-intel.tar.bz2 <http://www.ironfroggy.com/public/git-1.5.3-remote-osx-intel.tar.bz2>`__
  to expose the tools needed to access your local repository remotely,
  via ssh.

For SocialServe This Means...
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 
| The three current of us are now branching for our development happily.
  We've done hot fixes in the middle of larger branches, without
  disrupting our work. We've pulled bug fixes from the master branch
  into our own things, shared branches, merged them into the production
  line, and are generally having a really good experience.
| I think that, in the end, this really means more productivity. I'm
  able to be more flexable with my project, because I don't need to keep
  every commit in a state that can be pushed into production if James
  suddenly needs to fix something unrelated. Branch based development is
  great, and our scripts help manage them very well. I can't wait to
  release them.
