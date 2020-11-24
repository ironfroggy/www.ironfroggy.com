I am toying with a small package for working with and developing pure
functions in Python. An important part of this is allowing the pure
functions you write to use as much of the standard library as possible,
while remaining pure. What functions in the standard library could you
call pure? Builtin types, the entire math library, the itertools module,
etc. are on my list, but I don't want to miss things. Any suggestions?
So far I have a decorator that ensures a function A) only takes
immutables and known-pure functions as arguments, and B) ensures any
global names used within the function are pure functions. It is
primitive, but a start. I hope to take this further with some actual
uses, such as create working processes locally and remotely and pushing
pure functions to them. This also has interesting potential for
optimizing large computations, like executing functions before they are
called when the potential arguments are known.
Pure functions are interesting and might be a nice addition to our
Python toolkits.
