title: "Nevow: Post-Render Injection of LiveFragments"
publish_time: !!timestamp '2006-01-28 23:01:00'
status: published
type: post
rnder: jinja2
template: post.j2
tags:
- web
- programming
- python
--- 

In part of my current project, I've tried to make things very spiffy
and use that nice AJAX stuff we all hear so much about. I do this
through the wonderful Nevow, which makes much of the work a breeze.
Some of the things I wanted to do, however, it isn't there on yet, so
I had some more work on. Here is a story.

Nevow has a concept of a LiveFragment, which is a piece of a dynamic
webpage that can be placed into a LivePage and attached to a counter
class in JavaScript. The Python and JavaScript classes on either side
of the pool are able to call methods between one-another, to
facilitate anything you want that can be done in either language. All
of this works through the transport system of the LivePage to
communicate back and forth. Some recent changes allow easier
post-render initialization of new LiveFragments, but it isn't perfect
yet.

This is how is basically works, and some of this may change soon, as
Nevow is a work in progress.

First, we need to take our LiveFragment on the server-side and convert
it to something we can pass over to the browser in a remote call.
We'll just render the fragment into XML, which makes sense. This is
called flattening and is done when Nevow fragments are rendered
anyway. We do this after creating and setting up the new LiveFragment.
In this context, we are adding the new fragment as a child fragment of
the current one.

This assumes you already know how to use LiveFragments, and write the
jsClass to go along with it.

::

   f = MyLiveFragment()
   f.setFragmentParent(self)
   html = flat.flatten(tags.span(xmlns="http://www.w3.org/1999/xhtml")[flat.flatten(f)])
   d = self.callRemote('addChild', html)
   d.addErrback(lambda m: logmsg("Error adding child: %s" % m))

Now, we need to handle this on the client-side with a JavaScript
function implementing this ``addChild`` method of our jsClass.

::

   MyModule.MyClass.method(
       'addChild',
       function (self, html) {
           posting_list = Nevow.Athena.NodeByAttribute(self.node, 'class', 'list_node');
           posts = Array();
           var runtime = Divmod.Runtime.theRuntime;
           
           for (var p=0; p<posting_list.childNodes.length; p++) {
               posts.push(posting_list.childNodes[p]);
           }
           runtime.setNodeContent(posting_list, post_html);
           for (var p=0; p<posts.length; p++) {
                posting_list.appendChild(posts[p]);
           }
       });

Now, this is the meat of the deal, so I'll go over it in a piece by
piece. The first thing we do is find the node we're going to add a
child to. In this case, for some extra excitement, we're going to
insert the new child at the beginning, instead of just tacking it on
the end. It turns out this isn't the easiest thing in the world, but
it isn't difficult by a long shot. We create a new array, ``children``
and iterate over the nodes, adding them each to this array. At this
point, we use ``Divmod.Runtime.theRuntime.setNodeContent()`` to
replace all the children of the node with just our new one. Now, we
iterate over the list we made and append them all, in order, back to
the node. This inserts our new node before any of the others. When we
insert the new node with ``setNodeContent``, it is parsed internally
and this process requires it is XHTML 1.0 and that the namespace is
declared as such. However, the node you flatten is actually prepended
first with a script element, in this case, which initializes the
component on in the browser, when it all gets added to the document.
This will cause some errors parsing, so we wrap the whole thing up in
its own span tag and give it the right namespace. Keep this in mind
when working out any DOM logic, that you're LiveFragment's root node
will be the childnode of this wrapping span. Of course, you can use
any type of element to wrap it together, as long as its one top-level
node of the XHTML 1.0 namespace.

To summerize, we flatten our LiveFragment. We wrap the script node and
the live fragment up in something of the XHTML 1.0 namespace. This is
passed in a remote call to a javascript function. The javascript
generates a DOM from this and inserts it on the client-side, and the
script node initializes the fragment for us. After this, the
LiveFragment and its widget can make remote calls back and forth as
normal.

This technique is very useful in creating dynamic pages. In my case,
I'm using it to allow new postings to a page to appear immediately,
and for those postings to be immediately editable through an embedded
LiveForm. It can be used for a lot of things, and helps seperate your
logic and design.

I don't know if this will be helpful to anyone, but hopefully so.

Please let me know of any errors.
