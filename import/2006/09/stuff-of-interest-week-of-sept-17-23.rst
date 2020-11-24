Wow! It has been almost two weeks since my last post, and I was doing so
well. Unfortunately, i got quite sick and then had an unexpected trip
out of state (read: I forgot about it until the day before!) and now
feel ill, yet again. But, determination brings me back. I was planning
to post this on the 23rd of September, but the 6th of October is close
enough. Regular posting will continue starting tomorrow.

--------------

This is the first in my weekly post of interesting links around the web.
These are articles, websites, services, photos, and anything that else
that I want to bring up on my blog, but can't use an entire post for.
Being on any aggregation sites makes you think harder on each post and
puts some weight on you against those little posts, at least in my mind.
Hopefully, you'll enjoy whatever I post here. Maybe you'll find a useful
site, or learn something you wouldn't otherwise.
Really Smart Stuff
Ross Jekel, over on the Python 3000 mailing list, supported the
existance of the GIL (Global Interpreter Lock) in a very clear
paragraph). This came from a thread (yet again) about the possible
removal of the GIL for Python 3.0, which will almost definately not
happen. Instead, the most weight seems to be toward improving the
effectiveness and productivity of multi-process or
multi-interpreter-in-one-process communication to offset call between
interpreter boundries. Awesome stuff if it happens!
After some initial surprise when I learned about it, I'm now okay with a
GIL or even single threaded python (with async I/O if necessary). In my
opinion threaded programs with one big shared data space (like
CPython's) are fundamentally untestable and unverifiable, and the GIL
was the best solution to reduce risk in that area. I am happy the GIL
exists because it forces me to come up designs for programs and systems
that are easier to write, more predictable both in terms of correctness
and performance, and easier to maintain and scale. I think there would
be significant backlash in the Python development community the first
time an intermittent race condition or a deadlock occurs in the CPython
interpretor after years of relying on it as a predictable, reliable
platform.
Really Cool Stuff
|image0|\ In my effort to professionalize my blog, snazzy it up a
little, and a general interest in having cool things to look at, I found
stock.xchang, a free stock photo exchange website. There are great
photos available there, and when I get my camera working again, I will
definately be contributing to the collection.
|image1|\ Sometimes you just gotta say "Wow." I had a little trouble
with the prototype applet running sluggish and buggy, but watching the
demo video is just amazing. The software will extract 2D shapes into 3D
models and allow you to extrude, cut, reshape, and just do some amazing
things with an interface so simple that a kid could, and has, use it.
Makes me want a touchscreen all the more, so I can have extra fun
playing with this.
Really Quick Stuff
`JavaScript Scope (and this) Explained in
Detail <http://digital-web.com/articles/scope_in_javascript/>`__
`ParenScript - Lisp to JavaScript
translator <http://parenscript.org/>`__

.. |image0| image:: http://photos1.blogger.com/blogger/1723/1190/320/stock_xchng.gif
   :target: http://photos1.blogger.com/blogger/1723/1190/1600/stock_xchng.gif
.. |image1| image:: http://photos1.blogger.com/blogger/1723/1190/320/teddy-photo.jpg
   :target: http://photos1.blogger.com/blogger/1723/1190/1600/teddy-photo.jpg
