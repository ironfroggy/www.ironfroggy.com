title: "Recursion Bites with Complex Nevow Pages"
publish_time: !!timestamp '2006-01-29 23:01:00'
status: published
type: post
rnder: jinja2
template: post.j2
tags:
- python
- web
- nevow
--- 

There is a recently discovered issue with Nevow's Athena LivePages.
LiveFragment nesting fails if the nesting gets too deep, due to repeated
cloning of the contexts, including the full chain of parents back to the
root of the document. This was hitting the call depth limits in some
tests idnar was working on. I found this to be a little worrysome, as my
designs for the current project included some relatively deep nesting of
LiveFragments; at least, as deep as the tests that found the error.

Eventually, contexts are to be removed from nevow entirely, as I
understand it, but this is far down the road. A temporary solution was
needed, besides just not using so much nesting. I decided that instead
of redesigning the system I was building, I would fix the bug, and I
have. I posted Trac Ticket #602 along with a patch that fixes it.

Recursion is a very useful software construct, but sometimes it can bite
you in the end when you don't even expect it to. There is usually a way
around it, but I do wish there was a more explicit way in some language
to express a construct meant to avoid recursion. All I had to do was
traverse up the parent attributes and create a list of all the parents,
in order. I took each of these, and if the clone method was the same as
our own, so we know for sure how it works, I just manually clone it and
make it the parent of the clone of its original child. This way, no
recursion is ever needed between parents being cloned, unless a
different context class is being used, which also redefines the clone
method. If that becomes a problem, it should be fixable as easily.

This may seem a little hackish, but its a common enough issue that I am
really surprised there has never been a really good recursion
alternative in any language. I'm not sure what form this would take, but
in places it would be nice to say "this works like recursion, but
without recursing".
