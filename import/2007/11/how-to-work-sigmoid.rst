.. container::

   Software Development in Really Big Steps

   #. How To Work a Sigmoid
   #. `How To Work a Sigmoid - Part
      Two <http://techblog.ironfroggy.com/2009/07/how-to-work-sigmoid-part-two.html>`__

I've written about `my
use <http://ironfroggy-code.blogspot.com/2007/11/how-to-enjoy-week-of-fogbugz.html>`__
of `FogBugz <http://www.fogbugz.com/>`__, driven by their great `time
tracking and estimation
features. <http://www.joelonsoftware.com/items/2007/10/26.html>`__ Using
these, I've come across what I think is probably common and should be a
goal for estimating the time of a project.
There are two estimations of a project. When you start, you can make
some wild guess, pulled from the ether, weeks or months ahead of when
you think it will be complete. This is the number that is notoriously
and unequivically wrong. This kind of prediction is simply an invitation
to make a smart person look dumb, since so few of us realize that he
never was able to make that estimate. The larger the project, the
greater the exponent on your chances of being able to make this
estimate. This is not new to any of us.
The second estimate is the running estimate, compiled from the tasks the
project has been broken down into. Now, the pro of this running estimate
is that it is bound to be more accurate than the wild guess you started
with, especiallly if computed with some of the fancy number working
FogBugz does to account for how good different developers actually are
at estimating their time. However, to every pro is a con and this one
has a big one: the running estimate, although more accurate, is
incomplete. You can only estmate for the tasks you've broken the project
into and that is a fluxing set of tasks. As you develop you break larger
tasks into smaller ones, learn new things you need to do, change
requirements, find bugs in the work you've done already or the
dependencies you use, and continue to iron out the design. This is even
more true if you use agile techniques, so you didn't design a lot of
upfront, but design on the go. Not to say this isn't a good thing, but
it is a thing to be aware of.
|image0|\ The project starts at 0.0 and it ends at 1.0. Your guess is
somewhere below or above 1.0, but mathematically cannot be equal to it
(because, you can't guess!). As you accelerate your collecting of tasks
to do the running estimate begins to increase toward 1.0 very quickly,
until you start to level out and complete more tasks than you create. We
work on the running estimate of a sigmoid curve, winding up from nothing
and leveling off at the best real estimate that can be given with the
real data at hand. Now, I grabbed this image from some place and I
didn't add the flat line that represents your initial guess. This is
both because I didn't have the time and because that guess is completely
useless.
Great, so we work a sigmoid. So what?
The world is flooded with useless information and I don't want to
contribute, so this is the part where I make my revelation somewhat
useful. At least, theoretically. A good estimation system, like the
Evidenced-Based Scheduling from Fog Creek, is really great. But, what if
we included estimation of estimations? Oh, that sounds recursive, for
sure. Suppose that, in addition to computing the weighted estimates and
the running estimates of release after compiling all the information
that can be taken usefully into account, we also track the running
estimates as they change over time. If we graph these, I suspect they
would roughly follow the curve of the sigmoid. If we find this or any
other pattern to be true, we can estimate the estimations. The further
along a project goes, we can estimate the future of the curve and make
moderately intelligent guesses about where the estimation will go in the
future. Weighting for how different teams and individual developers
estimate, the system can train itself for accuracy.
I'm already into my current FogBugz tracked project, but my next will be
setup to grab the estimate data periodically and I'm just itching to
test out my theories. We can't predict when a project is going to be
complete, if it ever is, but we can damn sure do better than pulling
numbers out of the air.

.. |image0| image:: http://1.bp.blogspot.com/_wACg_J16I_8/R012WsJrSeI/AAAAAAAAACY/eN25LO9Ln8w/s400/Logistic-curve.png
   :name: BLOGGER_PHOTO_ID_5137892882080549346
   :target: http://1.bp.blogspot.com/_wACg_J16I_8/R012WsJrSeI/AAAAAAAAACY/eN25LO9Ln8w/s1600-h/Logistic-curve.png
