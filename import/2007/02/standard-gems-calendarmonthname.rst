This is part of a new series I want to keep up with. There are a lot of
hidden gems in the Python standard library, which gets larger all the
time. As the number of packages and modules grow, and the size of those
grow themselves, it becomes harder and harder for all of us to keep
everything in mind all the time. There are large parts of the standard
library I have never used or even looked at once, because its never been
needed by anything I have done. This means that when I do have a need
for these things, I don't know they exist. Perhaps one of the greatest
reasons for reinventing the wheel is simply ignorance of the wheel
existing in the first place! I see the same problem in others all the
time. This series, "Standard Gems", is an attempt to get things out
there that some people maybe have not seen or known of, and will later
find useful when the need sparks memory of the gem.
If you have any suggestions for gems, please `drop me a
line <mailto:ironfroggy@gmail.com>`__!

--------------

calendar.month_name
Ever needed to get the real name, even localized, of a month by its
number? 3 is "March" and 8 is "August", etc. Well, calendar.month_name
is a psuedo-sequence that gives just what you need! Try it out the next
time you need to display some date information.
Note: this is sequence-like, but it indexes from 1 to 12, so dont try 0
for January. This is moderately misleading, especially when it raises
IndexError on a bad number, rather than a KeyError.
