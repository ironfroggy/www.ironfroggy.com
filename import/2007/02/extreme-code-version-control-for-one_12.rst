Extreme Code - Version Control For One File
===========================================

| 
| You should start using version control systems when you only have a
  single file.
| You don't need a version control system until you have a large project
  and lots of collaborators.
| Two statements I've heard from individuals of great caliber, and it
  carried weight coming from individuals on both sides. Version control
  is important, and no developer worth their weight in USB keys will
  tell you to never user a VCS, but exactly when and where and why you
  should use them is not so agreed upon. The differences in opinion come
  from cultural, experience, and industry reasons. Many members of the
  free software community seem more exposed and ready to use CVS or
  Subversion, where version control is almost impossible to avoid when
  you need to collaborate across the world. Some individuals have horror
  stories about projects without version control, and others have never
  seen practical benefit in their time as developers. Yet, some simply
  work in areas of the industry that have less call, or less cultural
  motivation. Web designers rarely version control HTML and stylesheets,
  and game developers have a short code life cycle to begin with. Can we
  find the happy middle ground between always using version control and
  avoiding it like a ten ton plague? If we look at it from the two
  extremes, we just might.

Extremely Using Version Control
-------------------------------

| 
| You should create the repository to track and house your files before
  you even create the first file. There isn't any reason to wait, and
  you'll see the benefits immediately. The extra time spent creating the
  repository and tracking changesets when you only have a handful of
  files is still worth the benefit, because the benefit is not reduced
  in proportion to the number of files or the number of developers. You
  can have a small, single file and a single developer, and you'll still
  be better off with a VCS than without, I guarantee it!
| The use of a repository isn't a passive act. You can't just record a
  changeset when you feel like it, and treat the repository like a
  second-class tool. Committing is not what you do when the code seems
  OK, its something you plan ahead for and plan your work around. From
  an untouched state, you decide your plan of attack on a problem and
  work on that, and only that. When you record the changes, you need to
  be able to attribute them to a particular goal, to have the repository
  in a valid state with a logical progression. Before the patch, some
  bug existed, and after the patch, this bug was resolved. This is
  clear, logical, linear, and how the repository helps both remind you
  of the past and guide you to the future.
| As a single developer, you have just as much reason to make full use
  of version control as a team of hundreds of developers. The structure
  it gives you will lend well to your progression and not becoming lost
  in a sea of changing code. If among a hundred programmers, a mistake
  can be made and rollbacks or history needed, then a single programmer
  without peer review will obviously have their own share of problems
  with the code written months ago. When you know you have a large
  number of changes to make, and you are unsure of the progression, the
  freedom of working in a controlled branch will give you the peace of
  mind to just have at the code and swing it into gear.
| There might be larger benefits as the number of files and the number
  of developers increase, but version control is not something you
  should wait for. It is an essential component of any project, and
  should be employed from day one as part of your regular infrastructure
  of development. Collaboration is not the only, or even the best thing
  these systems have to offer. We've talked about the branching,
  structuring, and good habits that use of version control systems and
  regiments bestows on a developer, and they apply to each of us
  individually before as a group.

Avoid Using Version Control
---------------------------

| 
| Developing is hard work and when you're just getting started with
  something or working on your own, you don't need any added
  distractions. Bringing in tools like a version control system is just
  asking for trouble when you have all the big issues to deal with in a
  new project. You're so constantly changing your code and your
  structure that putting something between you and your fresh code is
  asking for nothing but trouble. You can also import the code into a
  repository down the road, when things get complex, more people are
  getting involved, or just when it feels right. The VCS is just one
  more thing to worry about and you have enough of those to handle all
  on your own with a brand new baby project.
| New developers, especially, should stay away from this kind of
  non-development detail. Version control might be important, but its
  not a detail the developer should have to care about, and even though
  you can't avoid that forever, when you're just getting your feet wet
  with the world of code, you need to expose yourself to a limited
  number of facets at a time. No budding programmer cares about version
  control when the code they are writing is so terrible they know
  they'll throw it away when they learn enough to have disdain for their
  own creations. Education and learning can't be jeoprodized by
  bothering students with trivial things.
| The original creation of version control systems, usually attributed
  to the VCS utility of UNIX systems, was intended to lock portions of
  the source while you worked on them, and existed solely as a
  coordination tool for multiple developers. So, obviously there is no
  point in their use if you're the only developer. No matter how
  complicated your project gets, if you are the only person writing the
  code, there is no confusion to be had, and you can rest easy. Open the
  files you need, edit the code as you need, and you'll be fine.

Discussion
----------

| 
| Spark some discussion. Make a comment. Play the Devil's Advocate and
  argue on the side you would not normally stand for. Fresh perspective
  is a good thing to have.
