| The signs are all over the place. I can count at least five
  implementations of Python today: CPython, CL-Python, Jython,
  IronPython, and PyPy. The use of the language is sky rocketting and
  set to grab real mind-share as the hype over Ruby subsides. Things are
  looking good for a favorite green snake and british comedy troop
  reference, aren't they? Trouble is on the horizon in the very
  ingredients that could push us into true success.
| Our community and our very language is in danger of segregation,
  unless we all do something about it and learn to get along.
| One of the most visible dangers (to me) is being ignored for various
  political, cultural, and non-technical reasons. IronPython's users are
  increasingly pushing IronPython-only recipes, libraries, and
  tutorials. No one is talking about the transition of the alternative
  implemenations to CPython 3.0 compatability. To make matters worse, we
  still can not define the language without refering to an
  implementation. This is very unlike the motivations that have made the
  language and its community so great.
| Although it has had measured success in a lot of areas, there is a lot
  of negative sentiment around IronPython, which is often seen as
  traiterous to a degree by the open source community members who are
  active with Python, and don't want to see it making bed-fellows with
  the Redmond empire. No one cares about getting Zope, Twisted, and lots
  of other popular projects to work with IronPython, or Jython and even
  PyPy, for that matter. The disconnect between the traditional Python
  community and the IronPython community means things like this are
  ignored, because no one on the traditional side cares and few on the
  IronPython side know better or consider the rammafications of their
  actions. We need to consider the language as a whole and understand
  the value of our many implemenations, especially those larger projects
  with a community responsibility. Of course, someone should step up to
  the challenge.
| The seperate between the pythons will only grow when 3.0 is released
  in a few years, pushing the other implementations behind in
  compatability by many years. This is something less easy to fix than
  most realize. The other projects simply dont have the resources that
  CPython does, and will fail to make the updates until many more years
  after 3.0 is the standard. There is a strong chance that this will
  lead to a fragmentation of the language, where IronPython might split
  off when it realizes that:

-  Most of its code is specific to IronPython anyway
-  It is already incompatible with most of the Python code that has
   migrated to 3.0
-  A major migration of the language to 3.0 will cost and gain as many
   users as any original changes they might make

| Obviously, I am naming lots of problems and few solutions. I wish I
  had more of the later and less of the former, but sometimes we are not
  so lucky. What few ideas I do have towards avoiding the problems are
  not well thought out, probably are missing vital information, or are
  simply stupid. I won't deny that I'm complaining more than helping,
  but the former often has to proceed the later. Maybe we have to have a
  period of whining about the problem before enough people realize that
  there even is a problem, before we have the right environment to start
  approaching it. We need to keep a handle on things, but the big
  dangers are still years down the road.
| Consolidation is the key to keeping our head on our collective
  shoulders. There is a lot of redundant work. There are module being
  maintained by at least three implementations and updates dont
  propogate often enough if there is cross over. In many cases, there
  isn't even enough cross over in the first place to cooperate on! Can
  you really consider IronPython a Python when you don't have os,
  pickle, or StringIO? Many of these missing pieces could be brought
  directly from CPython (licensing permitted, maybe someone can comment
  on any possible problems there). I believe (corrections are welcome)
  that PyPy does use many of the pure python modules from the CPython
  distribution. We can do better and sharing needs to become the norm,
  not the surprise.
| When I write a small library and I use StringIO, i really don't care
  if someone uses my module over CPython, Jython, IronPython, or PyPy.
  As a matter of fact, I'd love to see it used on all four! I have to
  inherently declare no support for IronPython, because I use a standard
  language module StringIO. People might forget but the stdlib is a part
  of the language as much as a for loop. If we had Python the language
  in its completeness and we had no libraries, we wouldn't have anything
  close to what we have today. Policies need to be put into place for
  cooperatively sharing between the implementations all the pure python
  modules that are possible. As long as they are being shared, they
  don't belong to any one implementation and should be more open to a
  joint management of their direction, including implementation
  specific, optional optimizations, such as using the CLR assemblies or
  Java classes that natively implement much of the functionality. We
  already have platform specific code branches, so this is not a
  stretch. The kind of sharing I call for will bring a lot of the work
  together so that overall we require less resources, yet produce more
  results.
| Non pure-python modules are something more of a problem. How does PyPy
  handle shared libraries, or IronPython while remaining a pure CLR
  solution? How does someone take advantage of .Net and Python without
  excluding the rest of the Python community? We have to make a lot of
  tough decisions, because no clear solution is on the horizon. We can
  look to RPython for a lot of advice, and just imagine if we had a
  conversion path from RPython to C# or directly to CLI bytecode. I
  don't want to have to rely on everything in pure python, until PyPy is
  more complete, but I don't want pygame to be stranded tied to C-land.
  The horizon might be empty, but we need to keep wandering towards it
  with high chins, just the same.
| A little, I wrote about the problems of culture between the
  traditional Python community members and those embracing and using
  IronPython. I did not expand on that much here, trying to be more
  balenced, but I'd like to expand on it in a future post. The more
  comments I can get about your opinions there, the more interesting the
  future post will be.
