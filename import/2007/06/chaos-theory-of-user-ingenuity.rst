There is just no telling what those crazy users are going to do. As a
`recent
post <http://worsethanfailure.com/Articles/Assisted-Processicide.aspx>`__
at `Worse Than Failure <http://worsethanfailure.com/>`__ makes us
realize, they can simply do some impressively unpredictable things. The
case in question has bank tellers using the Windows Task Manager
(ctrl+alt+del) to manually kill a process for an annoying dialog their
employers had the developers make un-cancellable as an error checking
precaution. I am simultaneously dumbfounded at their incompitence for
thinking it fine to repeatedly hard kill processes as a form of
annoyance reduction and my sheer amazement that the users knew enough to
even try it in the first place.
The lesson can be applied in a lot of places. We need to do more than
predict what the user will do: we need to make our software robust
enough to stand up to the random environmental attacks it will take from
the users' strange and completely unpredictable behavior. The user could
be clicking on our links or importing our packages (end user versus
developer) and inevitably they will do what you did not account for.
Account for the unforeseeable.
Account for End User Ingenuity
Software is annoying and the most annoying things will be avoided. The
ways we find to work around limitations, real or perceived, are huge.
That is exactly what the bank tellers were trying to do. The dialog in
question made them double check money counts on large amounts, but they
trusted themselves and each other enough to learn how and pass on the
technique of subverting the required dialog to save just a few seconds
every few transactions. Yes, it didn't not even come up on a typical
basis, so don't expect frequency to estimate likelyhood of tampering.
The user might put up with an annoying main menu for years, but abuse a
glitch to skip a step in a process they only use every few weeks.
Probably the single most effective way to combat dangerous ingenuity of
end users is the feedback mechanism. Let the user subvert through you,
not around you. Enable responsive adaptation to their needs, and tweak
the hell out of the interface to shave off those milliseconds.
Milliseconds add up when you're on your feet all day.
Account for Developer Ingenuity
We can take this story and adapt it to ourselves. We know there are
things we do to software that only for-pay websites would show you. No
one is more abusive to software than those who create it, and when we
deal with the internals we only have more strings to pull. Whether you
develop libraries consumed by other developers, or want to avoid abusing
the libraries you use, there are steps you can take to keeping usage on
the path.
Here, our single greatest ally is reduction. Take away optional
parameters no one has asked for yet. Don't implement a function that has
no use case. Eliminate type checking to allow proper ingenuity through
duck typing, while being prepared to properly accommodate common
patterns that arise, which you never foresaw. Give the other developers
constraints by giving them less to work with, but let the pieces they
have flex into shapes they need, so you can take their feedback and
adapt the code to officially support every unofficial dirty deed they
bend it over for.
Account for Your Ingenuity
Who uses your software more than you do? Maybe the most dangerous person
to watch out for is yourself. No one has access to pushing the limits of
the software more than you do. The users can find ways to subvert your
interfaces. Other developers can exploit oversights in the API. You, on
the other hand, can bend the entire thing to your will. If you think a
high math function would be useful in all the places you happen to use
the special file format library you develop over on Google Projects,
don't add it right away. Ask yourself if it really belongs there, if
anyone else will you use, or you would accept the patch coming from
someone else and without yourself wanting the feature. As much as the
users and other developers can take advantage of your software, you need
to look over your own shoulder more than anyone, but there are a lot
more of them than there are of you (hopefully!), so don't let your guard
down from their side, either.
