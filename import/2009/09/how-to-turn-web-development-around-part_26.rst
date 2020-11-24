When I complained about the problem, I promptly outlined some ideas
about solving it, vaguely. Now, I want to narrow that outline into
systems I actually use. I do most of my work with Django, some hobby
time is spent with App Engine and Twisted, and I enjoy Amazon Web
Services, so I'm thinking from these perspectives when I approach this.
Parts one and two were broad, but some of this might only apply to fewer
of you. Either ignore those or adapt to whatever you use.
Django's cache layer sucks. Simply stated and simply true. Any time I
decide I can cache something, I should ask myself if I could have built
it before I even had the request in the first place. Doing that with the
template caches simply isn't possible. It should be possible and it
should be the first path you take, instead of forcing us to go out of
our way to do the better thing. Anything I might want to cache, I also
might want to be sure I'm not doing in more place than once, and forcing
them inline in my templates does not help this. The template caches
imply a copy-and-paste method of reuse when a cached portion is used in
more place than one. When I define a cache block, I name it and I
specify a set of keys. This is exactly the information, that when
changed, I should just generate that block as a static snippet to be
inserted. If it weren't for the lacking in reuse mechanics, I would
advocate parsing all your templates for cache blocks and pre-generating
them. Instead, we need to pull the cached contents out of the normal
templates and use the existing names and keys to find the generated
snippets.
On the more basic level, there are some abstractions that need to be
injected into Django-proper to really be useful, by means of what they
would standardize. We have no current means of standardizing our cache
keys in a way that different applications can cooperate about what data
is where and how to get it. Even the types that are taken for granted in
Django have no useful standards. If they did, I would be able to drop a
QuerySet object into the cache in a way that another query can find to
reuse. And, when memcached is by far the most likely cache backend to be
used, we would be providing a mechanism that abstracted away its
limitations in entry size, allowing us to trust dropping our QuerySet in
safely.
Denormalization should be normal. I have revision tracking in a document
system, and from a normalization perspective it makes sense that each
version hold a foreign key to either its previous or next version, but
not both. From a practicality perspective, if I have one version I want
to know the previous and next versions without doing a new query. Our
Resources might offer a solution, by giving us some place outside of our
model to allow denormalized data. I could generate a record of my
documents with all the revision information queried and built and stored
in one flat record, while keeping my base model clean.
Queuing work should be as accessible as doing work. There is little or
nothing inhibiting a developing from dropping one little query or action
into an existing operation. I've recently built a weighted sort to
replace our basic date and time based order for posts. This means
generating scores for all the posts and updating those when posts or
votes change. Now, whenever we calculate scores we account for the age
of all votes and the relative scores and age of all posts and votes
together. In other words, this is something I'd prefer not to add to the
cost of a user actually posting content or voting on something. It would
have been extremely easy for me to call one generate_scores() function,
but it takes thought, planning, and infrastructure to have this done
after the request is handled.
Borrowing from existing Python canon makes sense, so I think
multiprocessing is a candidate for use here, in one form or another.
multiprocessing.Pool.apply_async() without a result returned fits the
bill for an interface to call some function at another time, possibly in
another process. Any function that works when passed through
multiprocessing into another process should also work when queued up for
execution at some later time, so borrowing here reusing existing
semantics developers should be familiar with.

