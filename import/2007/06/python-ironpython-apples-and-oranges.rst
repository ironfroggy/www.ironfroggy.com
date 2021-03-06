| While Fuzzyman is over at the
  `voidspace <http://www.voidspace.org.uk/>`__, talking about how great
  it is that, in IronPython, `str and unicode are the same
  things <http://www.voidspace.org.uk/python/weblog/arch_d7_2007_06_09.shtml#e740>`__,
  I'm over here getting more worried every day about the segmentation of
  Python and IronPython.
| 

   IronPython is a new implementation of the Python ... maintaining full
   compatibility with the Python language.

.. container::

   From the\ \ `IronPython
   homepage <http://www.codeplex.com/Wiki/View.aspx?ProjectName=IronPython>`__\ \ .

   .. container::

      They should go ahead and drop that last qualify. I want to make
      something very clear, and that is that I absolutely hate writing
      this post. The IronPython project is really great, and I've been
      impressed by what it has done, and my Microsoft's embrace of the
      language. Admiration does not trump worry, in this case. A number
      of issues make IronPython simply not Python. I've been advocating
      this issue more and more recently, so it is about time I wrote at
      a moderate length about the issue.
      In IronPython, str is unicode
      Now, it may be true that Python plans to drop the current
      behavior, make str unicode, and add a separate type specifically
      for dealing with byte strings (See\ `PEP
      358 <http://www.python.org/dev/peps/pep-0358/>`__\ ). However,
      that is not the case yet, and jumping the gun and making str and
      unicode the same type is an absolutely incorrect non-solution.
      This is not just a matter of taste, but a situation where
      IronPython is absolutely wrong. I can make two arguments against
      this.
      IronPython does not encode or decode between str and unicode

| 
| One of the most important issues about dealing with unicode is the
  difference between unicode or unicode strings of text and encoding
  strings of text or bytestreams containing encoded text, which may be
  decoded into understandable unicode (Joel has `covered all
  this <http://www.joelonsoftware.com/articles/Unicode.html>`__).
  IronPython implicitly can not do this. A str with a non-ASCII "byte"
  cannot be encoded by Python, if you don't tell it the encoding being
  used. This is no flaw, it is the law. IronPython, having no str type,
  effectively, just assumes the bytes over 128 are taken as the
  corresponding codepoints. There is no encoding anywhere, in which this
  is the correct behavior. That's right. They just give you a known bad
  result, and let it go.
| When There Is No Bytestring, You Have to Look Elsewhere
| So what happens when you truly need to work with byte strings in
  IronPython, which pretends byte strings are unicode strings? Well, you
  have to look elsewhere. Of course, the entire .Net API is at your
  finger tips, so look no further than System.Byte and System.Array, of
  course. Sounds easy, but the danger here should be obvious. Any Python
  code assuming, correctly, that str is a byte string type, is subject
  to implosion within IronPython and any IronPython code "properly"
  handling byte data simply can't import outside IronPython at all.
| Language and Library
  Does syntax alone make a language? Maybe one day it could, but those
  days died out. Python is far more than its clean, beautiful syntax.
  The libraries that come in the standard library provide even more
  value. As a foundation for all the software built on top, these
  packages are fundamental to the success of Python. Yes, your code
  looks beautiful all on its own, but all on its own it does not have
  an\ \ `embedded
  database <http://docs.python.org/lib/module-sqlite3.html>`__\ \ ,\ \ `configuration
  parser <http://docs.python.org/lib/module-ConfigParser.html>`__\ \ ,
  and\ \ `mail <http://docs.python.org/lib/module-smtpd.html>`__\ \ and\ \ `web <http://docs.python.org/lib/module-SimpleHTTPServer.html>`__\ \ servers.
  Right there you have a basis for a huge number of applications,
  without even leaving the language's vanilla installation.
  IronPython does not include any of these, so if you write software
  using them, don't expect them to run on the .Net runtime, just because
  IronPython claims compatibility. You can probably access all the same
  facilities, but you have to do so through the .Net APIs of similar
  facilities. I am not even sure that the same facilities are provided
  there. The sad fact about a lot of this, is that many fo the libraries
  not included in IronPython actually work perfectly, if they would
  include them in the distribution, without change.
  Because of this, we have to resort to things I consider terrible, like
  two different Python scripts, both doing some basic HTTP downloads,
  and both being completely incompatible because they rely on entirely
  different APIs: IronPython through .Net APIs and the real Python
  through\ \ `urllib2 <http://docs.python.org/lib/module-urllib2.html>`__\ \ or\ \ `httplib <http://docs.python.org/lib/module-httplib.html>`__\ \ .
  Conclusion
| IronPython takes the syntax, but stops short of the language. The
  problem is one for both Python and IronPython lovers. In Python land,
  we're seeing what appears to be an influx of interest from the
  IronPython (also, via Silverlight) world, but all those new developers
  are creating completely incompatible code. IronPython advocates, on
  the other hand, look silly to think they are promoting the Python
  language, and are completely missing out on hundreds of great
  libraries, years of built up community, and synergy that isn't just a
  buzzword.
| I really want this to all work out. IronPython, can we get along?
