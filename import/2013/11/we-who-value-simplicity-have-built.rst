|  James Hague wrote a `great
  post <http://prog21.dadgum.com/139.html>`__ about the emergent nature
  of complexity in computers. (emphasis added by me)

   The 8086 “AAA” instruction seemed like a good idea at the time. In
   the 1970s there was still a case to be made for operating on
   binary-coded decimal values, with two digits per byte. What’s the
   advantage of BCD? Large values can be easily displayed without
   multi-byte division or multiplication. “ASCII Adjust After Addition,”
   or AAA, was committed to the x86 hardware and 30+ years later it’s
   still there, emulated in microcode, in every i7 processor.  

..

   ...

   The UNIX \ ``ls``\  utility seemed like a good idea at the time. It’s
   the poster child for the UNIX way: a small tool that does exactly one
   thing well. Here that thing is to display a list of filenames. But
   deciding exactly what filenames to display and in what format led to
   the addition of over 35 command-line switches. Now the man page for
   the BSD version of \ ``ls``\  bears the shame of this footnote: “To
   maintain backward compatibility, the relationships between the many
   options are quite complex.” 

..

   None of these examples are what caused modern computers to be
   incomprehensible. None of them are what caused SDKs to ship with 200
   page overview documents to give some clue where to start with the
   other thousands of pages of API description.  

   But all the little bits of complexity, all those cases where
   indecision caused one option that probably wasn’t even needed in the
   first place to be replaced by two options, all those bad choices that
   were never remedied for fear of someone somewhere having to change a
   line of code…they slowly accreted until it all got out of control,
   and we got comfortable with systems that were impossible to
   understand.  

..

   We did this. We who claim to value simplicity are the guilty party.
   See, all those little design decisions actually matter, and there
   were places where we could have stopped and said “no, don’t do this.”
   And even if we were lazy and didn’t do the right thing when changes
   were easy, before there were thousands of users, we still could have
   gone back and fixed things later. But we didn’t. 

| The example of ls is my favorite, but it is the starkest difference
  between the intended simplicity and the complex nightmare that
  emerged. We see this pattern over and over again, and at times I'm
  beginning to think the "UNIX Philosophy" itself is to blame. **Our
  focus on small parts is causing us to miss the forest for the
  trees. **
| **
  **\ Thoughts?
