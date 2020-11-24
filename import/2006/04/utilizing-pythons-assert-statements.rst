Some recent discussions around the 'net have been tossing around the
ideas about static typing in python, briding static and dynamic typing
in C++-like languages, and similar concepts of making static-typing more
dynamic or dynamic languages more optimized in static-typing ways.
Particularly, I was sparked by Michael Feather's `"Set of Tests"
article <http://www.artima.com/weblogs/viewpost.jsp?thread=156197>`__.
There are different ways we might look into bringing those concepts to
Python, and I rolled a few of them around in my head. My final mental
landing was "Can we utilize the assert statement to inform the compiler
about these tests that are absolute?". Of course, you probably can see
how this is a lot like what assert does now, with the only difference
being between run-time and compile-time being the target of the rules.
This leads us to looking for where an assert could be compile-time
verified and then used to optimize code. The most basic compile-time
assert I can think of us "assert builtin is builtin", which would be a
contract that the name 'builtin' will continue to be bound to the
default builtin object, and won't be changed. This means we can do
"assert isinstance is isinstance" and the compiler can make assumptions
it could not before: that when it sees the name isinstance, it knows
exactly what it is before runtime. This opens up other expressions that
use these known names and promise other things to the compiler. We could
do things like "assert isinstance(l, sequence)" or "assert len(l)==3",
which would create a pair of contracts that l was some kind of 3 element
sequence, and the compiler could make it a tuple for optimization.
