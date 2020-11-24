Developers from both
`Opera <http://ajaxian.com/archives/3d-canvas-in-opera>`__ and
`Mozilla <http://blog.vlad1.com/2007/11/26/canvas-3d-gl-power-web-style/>`__
have recently blogged about 3D rendering contexts for the canvas
element, confirming my `year-old
predictions <http://ironfroggy-code.blogspot.com/2007/01/friday-night-link-up.html#item6>`__.
Of course, the news is a bit saddened by the decision from Opera to
support a new, non-GL-based API. I understand the desire for something
more high level, but putting well known GL functions underneath is a
perfectly acceptable idea. One side or a third party needs to provide a
compatibility layer, or they need to decide on one of these APIs. I
really hope OpenGL ES makes the win here. This also ties into the
`OpenGL
APIs <http://code.google.com/android/reference/android/opengl/package-summary.html>`__
on Android, accessable through WebKit, so it only makes sense that
Firefox, Opera, and all the WebKit-based browsers should standardize,
before Redmond releases DirectX 1.0 Web Edition Premium.
For Users This Means...
We're going to see some fun web applications taking advantage of this,
but there isn't a lot we'll see that we didn't have with Flash, for
years now. I think some of the most interesting effects will come when
we can use a canvas as a 3D texture and can render DOM elements into the
canvas. When we reach this, we'll see lots of page effects, from folding
elements to crumpled elements being deleted to rotating text and
interface units.
We're going to see a lot of ugly abuse.
For Developers This Means...
Just one more thing to wait years before specialists are expected, and
again you need to be a jack of all trades. Now you need to understand
some code, a little database theory, CSS styling, artistic design,
business layout, and 3D modeling and texturing. Have fun with it.
