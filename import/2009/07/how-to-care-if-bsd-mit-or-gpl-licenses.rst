| The two recent posts about some individuals' `choice of
  GPL <http://zedshaw.com/blog/2009-07-13.html>`__ versus others'
  `preference for BSD <http://zedshaw.com/blog/2009-07-15.html>`__ and
  MIT style licensing has caused a lot of `debate and
  response <http://twitter.com/#search?q=zed%20shaw>`__. I've seen
  everything as an interesting combination of very important topics
  being taken far too seriously and far too personally. All involved
  need to take a few steps back.
| For the uninitiated and as a clarifier for the initiated, we're
  dealing with (basically) three categories of licensing when someone
  releases software (and/or its code):

#. Closed Source. Easiest to explain, because you just get nothing.
#. GPL. If you get the software, you get the source code, you get to
   change it, and anything you combine it with must be under the same
   terms.
#. MIT and BSD. If you get the software, you might get the source code,
   you get to change it, and you have no obligations about anything else
   you combine it with.

| The situation gets stickier when we look at those combinations and the
  transitions between them.
| Use GPL code with Closed Source code
| So long as you don't distribute your software this is fine. It is a
  perfectly OK thing to do for software running servers or only running
  in-house. However, if you want to distribute your software to end
  users, the terms of GPL code require that the GPL also applies to your
  own code, so you've got to give that code away, rather than keep it
  closed. Further, you have to let the users modify and redistribute it.
| Returning modifications upstream?
| Go ahead. As the owner of the closed source, if you decide to take
  portions that have modified the GPL code and return that to the
  project as a thank you, it is your right. You don't have to release
  your entire project's code to do this. Similarly, if you want to
  release other portions of your code for use, it is likely required to
  be GPL, itself.
| Use MIT/BSD code with Closed Source code
| This happens a lot, in the same kind of situation above, but also in
  distributed software, because that is OK. In some cases, a notice that
  you use the code is required, but you aren't required to put your own
  code under any particular rules or license.
| Returning modifications upstream?
| Just like GPL, this is fine. However, you have more freedom about
  releasing other components of your code under any license you see fit.
| Use GPL code with MIT/BSD code
| Oh, no! Now you have a problem, because the release of your own code
  under MIT and BSD style licensing is forbidden if you include or link
  it (the terms can be fuzzy with modern runtimes) with GPL code. You
  probably just can't use any GPL code if your own is MIT/BSD style.
| Use MIT/BSD code with GPL code
| Sure, go ahead. The GPL is fairly receptive. If you release an
  application under the GPL and it requires or includes MIT/BSD style
  licensed libraries, that is just fine.
| Conclusions
| If you're a closed source, server side or in-house project, you dont'
  have much to worry about. You aren't distributing, so little of this
  matters to you. If you're a closed source, distributed product, then
  GPL is off limits for you. As the lead of an open source project, you
  still need to worry about GPL code. Either it can limit how people can
  use your code, by forcing it to become GPL, or you could face limited
  use by making the decision yourself. In short, while its an acceptable
  license for its uses, it happens to be most limiting under these
  factors.
| If you release some GPL code, I probably can't use it. Period. End of
  story (ignoring these commentaries about the story). Now, maybe you
  don't care if I can't use it, but isn't that why you're releasing it?
  The GPL is meant to protect us, but who and what does it protect us
  from? I can't release it in a closed source product, and I don't want
  to, but you're also keeping honest, open source enthusiastic
  developers from using your project. You aren't limiting us for
  technical or legal reasons, but only for our choice of another
  license. A GPL licensee can say anything about everyone having a
  freedom to choose their license, and this is true, but you can't
  escape your own choice specifically limits who else can interoperate
  based entirely on if they agree with you.
