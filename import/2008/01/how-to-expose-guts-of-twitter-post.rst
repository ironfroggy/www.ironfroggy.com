Twitter does a lot of queuing. I mean, a lot. We know other people have
a need for some good queuing, so much that Amazon even released Amazon
Queue Service, not so long ago. There has never really been a common
queue server, and maybe that is because its so simple that no one has
really had the need to push one hard into the public eye. At least, as
public as our eyes are.
Enter Starling, the internal queue system of Twitter, recently released
to the public. Written in Ruby, and I don't even mind! Pointed there by
my ever-pointing buddy, David Novakovic, Starling does nothing
absolutely remarkable, but someone has to get the light. What is
interesting is their choices. Starling uses the MemCached protocol, so
your clients are probably already prepared to use it, they just need to
treat the queues a little different from the mappings. The typical
MemCached get-operation now removes the item from the queue. The keys
function is identifiers for the queues. I don't think it could have been
simpler. I'm planning to look at setting up Starling for testing on my
linux servers and my Macbook, and to try and find something interesting
in the way of using it. I have some plans I could utilize it in, and
maybe bring it to the office later.
Now that Starling has some attention and gives us something of a
standard for queue protocols (I love reusing protocols!), if anyone has
different needs or just wants to scratch an itch in their language of
choice, lets make the smart move and take the same protocol route.
Queues may be a small thing, but its the same things we really need to
agree on more. Anyone up for a MemCached-protocol to Amazon Queue
Service bridge?
