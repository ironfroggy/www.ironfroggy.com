One of our greatest bragging rights is the lack of memory management in
our Python code and the wonder of garbage collection, so when we find a
way to get a memory leak in Python, it should be made well known. I
don't know if this is already known, or not. In actuality, these
situations are known as reference leaks, sometimes, and they are cases
where we forget to remove a reference to an object we don't want to keep
around anymore. The following session will cause this problem.
``Python 2.4.3 (#2, Oct  6 2006, 07:52:30)[GCC 4.0.3 (Ubuntu 4.0.3-1ubuntu5)] on linux2Type "help", "copyright", "credits" or "license" for more information.>>> def f():...     for i in xrange(100):...             yield i...     raise Exception("oh no!")...>>> [x for x in f()]Traceback (most recent call last): File "", line 1, in ? File "", line 4, in fException: oh no!>>> globals()['_[1]'][0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]>>>``
Now, there is a global that will sit around referencing a potentially
very large list and we won't be aware of it. However, it will be
overwritten if another list comprehension is run in the same scope,
which will be removed if the new LC is successful, and if we do our LCs
in functions, the local will be cleaned up on return or raise. Of
course, you can always just pass a generator expression to list() and
avoid the problem entirely.
Just keep an eye out, if you build global constants with list
comprehensions.
