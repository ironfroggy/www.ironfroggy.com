| |image0|\ |image1|\ When you have a problem and you rush to
  colleagues, or strangers on IRC and mailing lists, you've got to
  present a problem they'll want to help you fix, and with all the
  information they need to fix it. You can't give them information they
  dont need, because any extra work filing through your unrelated code
  is going to reduce the chances anyone will put in the time to help
  you.
| We can state a few rules about seeking help with code.

#. Ask the question clearly and don't be ambiguous about your intentions
   and requirements.
#. If you need to include code, it needs to include all important
   context.
#. Present the problem without reference to out-of-context issues.

| Don't come in with a link to your entire body of code telling us it
  doesn't work. What doesn't work is asking for help like that. Besides
  telling us exactly how things don't work, and what they are doing
  compared to what you are expecting, you need to give us code that
  specifically and only demonstrates the problem directly at hand. This
  is our golden "Minimal Working Example", where "working" means that it
  works just enough to show us how its broken. You need to reproduce the
  situation causing your code to break, without showing us the
  environment your code is in when it breaks. That means taking code
  segments out of their modules and even out of the insides of
  functions, and surrounding them with just enough jumpstart to fail the
  same way it did in the original code.
| Before you even get around to asking your question, you might solve it
  simply by isolating the problem into your example. When you remove the
  problem code from everything else, you can remove the distractions of
  everything else going on around it. You might remove another part of
  the code to reduce things to the minimal example, and suddenly find
  the problem gone, identifying the removed code as the source of your
  problems. If you think isolating test cases sounds familiar, then you
  know enough that I shouldn't have to tell you these minimal working
  examples should already exist in the form of your unit test suites.
  When something goes wrong, you should have already had a test to catch
  it, and added one if you didn't. If the problem can be isolated now,
  keep it isolated for later.
| Remember what is important to your problem. If you can't figure out
  some particular pysqlite2 issue, and you're working with data your
  extracted from XML files grabbed from a remote server, you can bet the
  XML, HTTP, and all the logic to process it is not worth your time to
  show anyone. Your example only needs to show the data you have to push
  through SQL, and no one should need to see where its come from. If
  your components are more tightly woven, and separating them isn't
  possible or is even moderately difficult, then you have a serious
  design flaw and extracting the problem example has revealed away to
  clear up your code and likely solve many latent problems, all at once.
| Once proper testing, documentation, and isolation have let you up the
  creek without a paddle, thats where community support comes in. Come
  to us with the example that tells us right away what the problem is,
  what its doing, and the obvious thing you think it should have done,
  instead. We can all run this code and approach it from the same
  direction as yourself, so we know exactly what your problem is and
  where to approach the solution.

.. |image0| image:: http://1.bp.blogspot.com/_wACg_J16I_8/ReFakEMFpGI/AAAAAAAAABA/lDrVyJMXVWE/s400/693590_inside_the_flower_3.jpg
   :name: BLOGGER_PHOTO_ID_5035405434023158882
   :target: http://1.bp.blogspot.com/_wACg_J16I_8/ReFakEMFpGI/AAAAAAAAABA/lDrVyJMXVWE/s1600-h/693590_inside_the_flower_3.jpg
.. |image1| image:: http://1.bp.blogspot.com/_wACg_J16I_8/ReFakEMFpHI/AAAAAAAAABI/B728BUn3CHk/s400/605555_flower_arangementbouquet.jpg
   :name: BLOGGER_PHOTO_ID_5035405434023158898
   :target: http://1.bp.blogspot.com/_wACg_J16I_8/ReFakEMFpHI/AAAAAAAAABI/B728BUn3CHk/s1600-h/605555_flower_arangementbouquet.jpg
