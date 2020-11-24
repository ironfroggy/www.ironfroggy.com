| I spent my Sunday afternoon familiarizing myself with a tool who's
  `Getting
  Started <http://vagrantup.com/docs/getting-started/index.html>`__ page
  has been sitting in my `Evernote <http://evernote.com/>`__ tickle file
  for a couple weeks. This is one of those many projects that fall under
  the ever widening category of "Stuff I Wanted To Do, But Am Glad
  Someone Else Did It So I Can Just Use It And Get On To The Next
  Thing." If you use virtual machines as part of your development
  process, or want to, and especially if you already use the excellent
  `VirtualBoxVirtualBox <http://virtualbox.org/>`__, then
  `Vagrant <http://vagrantup.com/>`__ is certainly worth looking at.

The Setup (for Vagrant 0.2)
~~~~~~~~~~~~~~~~~~~~~~~~~~~

| 

.. container::

   Now, the docs might need some updating and they seem to assume you're
   already a Ruby user, so they're missing a few dependancies that such
   a person would just happen to alread have. This is what I did, as an
   Ubuntu user who didn't even have Ruby installed. I'm also adding
   Virtualbox's Karmic repository to provide VBox 3.1, which Vagrant
   requires.

| 

   sudo apt-get install rubygems libxslt-dev openssl-ruby

   .. container::

      sudo gem install vagrant

   sudo bash -c 'echo "deb
   http://download.virtualbox.org/virtualbox/debian karmic non-free" >>
   /etc/apt/sources.list'

| 

.. container::

   My machine installed Vagrant to /var/lib/gems/1.8/ so I added
   /var/lib/gems/1.8/bin/ to $PATH.

| 
| Each Vagrant box you build should have its own directory for
  configuration and should be run from their, so you can create a test
  project now.

   .. container::

      mkdir test-vagrant && cd test-vagrant

| 

.. container::

   Also, there are reports of issues on *some* 64-bit machines and I
   couldn't get the base image to run, but the Ubuntu Karmic image is
   running fine for me, so this got me started with my first Vagrant
   box:

..

   .. container::

      vagrant-box add karmic
      http://files.vagrantup.com/contrib/karmic.box

   .. container::

      vagrant init

   .. container::

      vagrant up

The Point, What Is?
~~~~~~~~~~~~~~~~~~~

| Why do this? What is the value in being able to quickly build, run,
  and clone virtual machines? Here are a few ways I'm already using them
  and will use them (more) with a tool like Vagrant to make it nicer.

-  Keeping a definitive base of my development environment. I always
   have an image of a machine that I consider my minimum requirements
   for whatever project I might be working on. This is an Ubuntu image
   with all the tools I use, my vimrc and my virtualenv/pip shortcuts,
   etc. When I start a new project, I clone this image and add to it.
-  Making my specific environments reproducible. This one I have tried
   and can now start doing seriously with Vagrant. For any project, I
   can maintain a script to build a development environment on top of my
   base. The benefits are two part. First, I can keep a clean record of
   what is required to work with a project. Second, when a change is
   made to my base, I can rebuild my development environment for **all**
   of my projects instantly. (Well, I can issue the command instantly,
   but I'll probably each lunch before its done!)
-  VirtualBox images can be portable. It might even be possible to move
   suspended images, but I'm not completely sure about this, yet. If it
   turns out to be something I can do, I'll be able to suspend a project
   on my desktop, running the box off a USB key, and then resume it on
   my laptop in the park. Even if I can't do this, I can still build
   identical environments on multiple machines, for myself or for other
   developers.
-  Replicating production and building local staging setups, machine the
   setups I have at Linode and EC2, will become something I can do with
   a minimal effort. I'm going to save a lot of time deploying to clones
   of my production machines running right here under my desk.

.. container::

.. container::

   UPDATES:

.. container::

   April 5, 2010 - Added links to Vagrant and VirtualBox websites. Added
   step to include repository for VirtualBox 3.1
