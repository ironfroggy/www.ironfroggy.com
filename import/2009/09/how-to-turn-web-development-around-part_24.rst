I did my best to outline the problem in Part 1. Now I have to stand up
and propose some kind of solution. Otherwise, I'm just complaining and
contributing nothing of real value.
Our frameworks make certain things easier. They don't provide tools to
help us with other things. For some other set of activities, they may
actually prohibit. The problem here is a combination. Django makes it
easy to query your database and wrap functionality up into re-usable
template tags. While I'm thankful for that, I am also realizing that
ease of one thing can prohibit another. When one path is made easier it
creates the perception of greater difficulty in other paths. I think
this is why, when our web frameworks give us all these tools to response
to a web request, we completely lack in everything we could do aside
from that request.
How can we make it easier to work outside the web request?
We need some idea of what working outside the web request means. We also
need to define these in terms that are useful when we do get around to
that request handling we've already got.
Going back to the tag cloud example, we look at the resources created
when we generate one. Aside the HTML snippet of the tag cloud itself, we
build the data used in the cloud, consisting of all the unique tags and
their counts. This is the kind of data that makes sense to store in your
cache, but this fails the normal cache use case. We don't want to loose
these generated resources when caches reset, so we need something less
ephemeral. Any decent key-value store would be a good solution here.
Unfortunately basic Django signals are lacking. Another means of
triggering the resource generation at the right times, with the right
parameters, has to be found. It makes sense to actually use existing
signals, which would add to a job queue.
The few remaining parts to give us easy mechanisms for inserting
snippets into templates or grabbing generated datasets in views are all
very simple. Together, the three layers come together to give us what
our frameworks are leaving out today. Resources, to store non-cheap
data. Jobs, to generate resources. Finally, Tools to acquire and use
those resources. If I were an egotistical man, I might try to coin my
own acronym and name this RJT.
I know this is nothing new. Rather than make the situation better, that
actually makes it worse. As any project grows and matures, the cut
corners need to be filled in. Everything here is eventually built, to
different variations and with probably a lot more forethought (or a lot
less, depending on the pressure.) The only difference is that large
scale applications need to divert more resources to pushing, instead of
pulling, whereas smaller scale applications simply should, because the
benefits exists in either case. We won't all need to grow at exponential
rates, but we should be doing better with whatever resources and
whatever work load our application is given, small or large.
