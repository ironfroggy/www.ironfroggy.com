| How much does it suck to transfer a few hundred photos from your
  camera, only to afterwards notice the date on the camera was wrong?
  So, here I go looking for an EXIF batch updating program, and the
  pickings are much slimmer than I would expect. Of course, writing my
  own seems like a pretty viable option and the EXIF.py module would be
  grand to apply here, save for one problem: It was written in 2002 and
  it still doesn't write back to the image.
| What's a dad with hundreds of family photos to do? Fix it. Talked with
  someone else interested in this and came up with three options to move
  forward.

#. Replace the entire module with a ctypes wrapping over the libexif
   library.
#. Jam EXIF writing into the existing module by invoking the exif
   command-line utility.
#. Reverse engineer the EXIF format from the modules parsing functions
   and properly implement writing into the library.

| Cross-platform support is great, but I'm having a crappy time trying
  to cross-compile the exif utility to windows, I can't find binaries
  for it, and that is some sand in my pants. Then again, I really
  wouldn't use it on Windows, so I can defer the search for the command
  line utility on Windows until later. For ease of implementation, this
  will probably be the route taken. I'll post the results here later,
  but I probably won't send patches to the maintainer, because the
  methods I'll use won't match well there. The current library isn't
  really designed well for this, so I think a redesign would be needed
  to do it in a really good way.
| If anyone knows that this is futile and a solution already exists,
  please `let me
  know <mailto:ironfroggy+blog_exif_writing_in_python@gmail.com>`__.

| 
