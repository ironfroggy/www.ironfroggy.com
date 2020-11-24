Earlier I asked "\ `Why can't my websites get
along? <http://ironfroggy-code.blogspot.com/2006/03/why-cant-my-websites-get-along.html>`__\ "
and now I'm going to answer myself.
What I want them to do
The love triangle in question, to review, is GMail's contact list,
Amazon.com wish lists, and the Google Reader and the books listed in
some posts there.
Any books mentioned in posts through Google Reader (or on any page, for
that matter) should be flagged as being books, or the browser should be
able to just figure out that they are books. It shouldn't link them
directly to Amazon.com from the website, because maybe I like to by
through B&N, right? My browser should see these elements marked
(somehow) as being book titles, and make them into links to the books
entries at Amazon (or Barnes & Noble). To take this a step further, the
book sites might publish some kind of services feed, that lists services
available to some particular resouce. So, when you ask it "What can you
do withA Tale of Two Cities?" it will say "I can add it to your wish
list. I can add it to your shopping cart. I can sell it to you
immediately." and etc. Where should these commands show up? Well, that's
up to the browser, really. It could be in a right click context menu, or
an expanding dialog when clicking the element associated with the book,
or maybe in a smart sidebar populated with all the books (and other
intelligently utilized resources) found on the current page.
In this example, I tell my browser "I want to add this to my wish list."
and it does what the service feed tells it to do, and requests some
resource that is known to handle the action it wants for the target in
question. Amazon.com will handle this request by adding the book to my
wishlist, and it doesn't even have to show me a page about it. It should
tell the browser about the success of the command, but that doesn't have
to be anything Human Readable, does it? My browser might display a
little checkmark or something next to the books name, even in other
pages three months later.
Some point in the future, after I have lots of nifty books on my wish
list, I'll want to send it out to friends in family. It is my birthday,
after all. At Amazon.com, I click on the "My Wish List" link and I view
my books and I click on "Send this list to someone" because I want
everyone to buy me things. The page I navigate to will have a form,
where it wants a list of email addresses and a message to send along
with the list. The emails is what interests us. Somehow, they need to
communicate that this particular input on the form is a list of email
addresses. This might be some new attribute for input or form elements,
but it doesn't really matter. What matters is that the client will see
this and know I am going to entire e-mail addresses. It could do a lot
of different things with this information, of course. It might give me a
drop-down list of known emails, and those might come from a number of
places. It might have different address book protocols implemented, or
might pull e-mails straight from GMail webpages. In any case, it will
acquire them the best way it knows, and I'll have this list anywhere I
need it, including to send out my Wish List.
And then, everyone buys me stuff.
What pieces are missing
I've gone over a few things we need to accomplish to be able to combine
services and information freely like we should have been doing years
ago. Service feeds are an important concept that is only very lightly
being touched on yet. In this case, I am talking about some Web Service
that you can ask about other web services available. You would give it
something it knows about, like a book ISBN or title, and it would tell
you what it can do with that resource. It would return a list of
commands, by name and the URLs to execute those commands. Maybe your
browser would look
tohttp://www.amazon.com/services/servicesfor?title=Prefactoring to get
an XML document that has the information it needs. Does anyone reading
know if there is a current format or specification to deal with that
kind of data specifically? These services should all be considered
something the client would perform on our behalf, maybe without us
seeing. That means the results of the requests should be
status-oriented, and don't need to be webpages at all. If they want to
say "There is a webpage here about this request I just completed, too"
then that is fine. The final component involves the data we need to put
into all of these webservices, and how much about what it wants we and
our webclients know, so as to better equip us to provide that
information. Again, is there something in the works towards this goal?
