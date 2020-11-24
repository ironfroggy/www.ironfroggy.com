I was messing around with the use of yield as an expression, the new
feature in Python 2.5, and I got a little tripped in small cases of
order with how you need to iterate over the generator and when you call
send(), etc. I just thought I would post this example to make anyone
passively reading aware of the ordering.
``>>> def g():...     print 1...     print 2, (yield)...     print 3...>>> gen = g()>>> gen.next()12>>> gen.send(0)03Traceback (most recent call last):  File "", line 1, in StopIteration>>>``
