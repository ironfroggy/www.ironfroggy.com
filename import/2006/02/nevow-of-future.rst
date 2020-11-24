I am not a core Nevow developer, but am only a developer who uses it. I
do talk a lot with the developers, and try to keep up with what is going
on there. So, I do know a bit about what is going on, and where things
are supposed to go. I know that contexts (a type of object passed around
that gives access to the current tag being rendered, remembers adapters
between interfaces, and does other stuff that isn't so good) is supposed
to go away, eventually, at some point, somehow. There is little talk of
how, when, and that sort of solid thinking on the subject.
So, for the heck of it, I'll propose a plan of action, and this is it.
Step #1
Fork it, so that all the refactoring can be done and if anyone needs a
backward compatible Nevow, it can still be around for them. There is
already xmantissa and xquotient, so it wouldn't be a stretch to add
xnevow. My other favorite is to just say that Athena is the new Nevow
(see Step #2)
Step #2
Pull everything out of the fork that Athena doesn't need, so things can
be focused. Refactor so that there is no difference between Page and
LivePage, and you can just make any page become live. At this point,
things can start to change and context can be factored out entirely. New
flatteners would be needed, of course, but those should be more or less
straight forward to adapt.
Step #3
Expand the templating system to be smart enough to handle both server-
and client-side work. I recommend a nevow:insert directive that defines
sub-templates to fill and insert the resulting node at some place, which
could replace nevow:pattern and also carry over for used in live pages
on the client. While we're at it, add in some good widgets to start
with, like containers and tabs and such.
Step #4
Create a fake nevow module that can map existing API calls to the new
stuff that would be in xnevow/athena. This would allow for easier
transitions to the new system.
I might try and convince the usefulness of this to an employeer and see
if some of my project time can be spent sprucing up athena in such a
way, depending on just how much this would take to be really useful, or
just usable. Then I could contribue something useful, and get some
moneys.
