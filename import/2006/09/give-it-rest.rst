| I'm wrapping up a REST layer to the service backend I've been
  developing for my still-unnamed-employer (find out when we launch,
  real soon now!). I had never developed a service under the "REST"
  acronym before, so my boss gave me a crash course, I read some things,
  I thought I got it. REST, a buzzword in its own right, is like
  stapling smoke to water when you try to define it. That isn't because
  its vague, its because most of the people who talk about it don't know
  what they're talking about.
| Maybe I'm one of them and I shouldn't be posting this.
| REST is Not:

-  HTTP
-  XML
-  RPC
-  A protocol, format, or even much of a specification

| Rest is:

-  An idea(l)
-  Agnostic on just about every specification associated with it

| Requests on a REST Service are:

-  Atomic. No request relies on any other made before or after it.
-  Self Authenticating. Every request must include any credentials. See
   point 1.
-  Self Describing. This is most commonly XML, and sometimes people
   think it must be, but it can be anything. We use JSON.

| Some of the most interesting things I've learned working with a REST
  service are the things that do not fit the model well. No model fits
  every need perfectly, and REST doesn't escape that fact, I'm afraid.
| In particular, you are not always transfering a state. There is a
  distinct difference between state transfer and a request to perform
  some operation upon a state. Unfortunately, any ways around some of
  the problems posed are directly rejected by the rules of REST.
| For example, say you want to provide as a service a simple counter.
  You expose PUT on /counter/foobar to register a new counter, and then
  GET on /counter/foobar will provide the current level of the counter.
  Following the rules of REST, how do you provide an interface to safely
  increment such a counter? We can not perform a GET and a PUT, because
  it violates that each request be self contained, and it will break
  when any other client of the service is incrementing at the same time.
  We need a single operation to alter the state, without performing a
  state transfer.
| The best thing you can do is use POST on a resource, and transfer a
  request to increment. It seems to violate the tenents of REST that the
  resource you POST will not actually reside at some permenant location,
  as they are throw-away requests. You either have to live with a
  not-exactly-REST interface (but, isn't that it works the important
  thing?) or actually keep requests around for some time. Maybe put them
  at some location, where they can be checked for review of their
  status.
| I don't know if this is helpful to anyone else writing REST services,
  but the information around isn't always accurate, so why should I
  worry if I am?
