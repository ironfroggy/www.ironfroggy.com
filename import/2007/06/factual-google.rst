| Google is building fact mining into the search engine. Coming across a
  `little
  article <http://www.bspcn.com/2007/06/22/5-things-you-probably-didnt-know-you-could-do-in-google-docs-spreadsheets/>`__
  over at The Best Article Every Day, I got wind that Google
  Spreadsheets can do lookup of certain
  `statistical <http://www.google.com/support/spreadsheets/bin/answer.py?answer=54199>`__
  and
  `financial <http://www.google.com/support/spreadsheets/bin/answer.py?answer=54198&query=google+finance&topic=&type=>`__
  information. You can have formulas that include things like the latest
  Microsoft stock quote or the boiling point of sodium. This seemed
  interesting, so I played with it a bit, but changing the formula
  quickly to play with it was awkward. "Can I just Google this stuff," I
  thought? Yes. Read on for my findings.

| The documentation for the Spreadsheet function, GoogleLookup, talks
  about *entities* and *attributes*. "Pluto" is an entity and "mass" is
  an attribute. As it turns out, you can just search for `"mass of
  Pluto" <http://www.google.com/search?hl=en&q=mass+of+pluto>`__ or
  `"birth rate in
  Canada" <http://www.google.com/search?hl=en&q=birth+rate+in+Canada>`__
  and are presented with a new type of search result.

|image0|

| We can see that Google seems to be pulling facts from the websites
  they index. They are structuring the information into subjects and
  properties about them. The feature has some large holes of missing
  functionality. "boiling point of sodium" gives a fact, but the system
  fails to parse any of the hits for "boiling point of mercury". The
  information we can get seems a little hit and miss. The community
  needs to put effort to document all of the entities and attributes.

| One interesting result is searching for "mass of Pluto" doesn't just
  give us a fact result, but what appears to be a Google calculator
  result. This means they are recognizing the mass in both value and
  units. We can even use "mass of Pluto" in any calculation we would
  give to Google calculator.

As the shift is made from taking finding relevant documents to just
giving us the information directly, we might wonder what the future of
the search engine is. I expect we'll see someone in the next year bring
Google to court for yet another lawsuite about what they can or cannot
scrape from their website. When you have a nice site with good
information, and Google just gives the users the data, you probably
worry about the affect on your traffic. If it does affect traffic, then
will the sites Google is grabbing the information from even remain
active? Where will they get facts from when their facts pulling
eliminates their sources?

.. |image0| image:: http://1.bp.blogspot.com/_wACg_J16I_8/Rn0FtstnayI/AAAAAAAAABw/D-7mAOFse9M/s400/googlefactresult.png
   :name: BLOGGER_PHOTO_ID_5079222237398526754
   :target: http://1.bp.blogspot.com/_wACg_J16I_8/Rn0FtstnayI/AAAAAAAAABw/D-7mAOFse9M/s1600-h/googlefactresult.png
