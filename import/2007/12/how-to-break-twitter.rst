|image0|
So I haven't realized it, but my twitters from the last day or so have
gone unposted. Twitter pod is great, but its completely silent about
authentication errors, apparently. The root of the problem is that I
have two twitter accounts: ironfroggy and pythoncoders, which I intended
as an aggregator of python twitter accounts. At the very least, a place
to find other pythoners on twitter. Now, I haven't been keeping up on
pythoncoders, so I decided to log in and update the followings, only to
realize I forgot the password. Here in lies the cause of my troubles.
The twitter "reset password" form does not take a username. Oh, no, it
takes an e-mail address, which I have two accounts with the same of. I
crossed my fingers, went through the process, and seemed to be brought
back to my ironfroggy account, so I decided to figure it out later.
Somehow, this process leaves the account with an unknown password,
probably random or even null, or for some reason the fact that they
accept multiple accounts with the same e-mail is not taken into account
in code paths that should care about it.
I'm waiting for a solution, Twitter.

.. |image0| image:: http://assets2.twitter.com/images/twitter.png?1196983612
   :target: http://assets2.twitter.com/images/twitter.png?1196983612
