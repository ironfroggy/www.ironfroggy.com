A new version of DeferArgs is available `at the
cheeseshop <http://cheeseshop.python.org/pypi/DeferArgs/0.2>`__.
New in 0.2 are the attempt, catch, and cleanup decorators. These mirror
the functionality of try, except, and finally. Any deferargs decorated
function can be followed immediately by any number of error handlers
decorated as @catch(ErrorType) or @catch() to catch all, with the same
semantics as except clauses if they were after a try block that
surrounded the code in the function. The catches can all be followed
with a cleanup decorated function, which will be called when everything
else is done, errors or not.
There is also a convinience decorator called attempt, which
automatically calls the function once a @catch() decorated handler is
defined (signifying that all error handlers for it are prepared). Of
course, calling it only really creates the deferred that fires when its
arguments are ready, so you dont have to expect it to run for real untl
after the attemp/catch/cleanup is completely defined.
As always, comments are welcome!
