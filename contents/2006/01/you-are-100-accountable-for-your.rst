title: "You are 100% accountable for your source code"
publish_time: !!timestamp '2006-01-29 23:01:00'
status: published
type: post
rnder: jinja2
template: post.j2
tags:
- programming
---

`You are 100% accountable for your source
code <http://blogs.msdn.com/marcod/archive/2006/01/28/AccountableDesigner.aspx>`__:
"It is just amazing how the mainstream software development industry is
behind the times in comparison to other more advanced disciplines; the
below fragment by Mary Poppendieck summarizes what I am writing about."
Caught this through the feed of MSDN blogs and it hits a good point.
Specifically, every line counts and every line is one more line of
source you need to keep correct in relation to every change made
anywhere else in the code. Now, this has some other points to consider,
such as private constructs being a little less dependant on other code,
but on the whole it is a pretty true and simple statement. Keep your
source code lean, and don't add what you don't need, because every line
you write is another line you need to worry about when you make any
change anywhere. Of course, this is well known in most senses, and
nearly all techniques of intelligent code design revolves around keeping
all these increasing lines under control and protected from one another.
However, no matter how good we think we can deal with it, we can never
forget the simplest way to keep the code correct: `less
code <http://www.lesscode.org/>`__.
