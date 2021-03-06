`Brett Cannon: Clarifications on
LINQ <http://sayspy.blogspot.com/2006/02/clarifications-on-linq.html>`__:
"Calvin Spealman set me straight on the true importance of LINQ."
Well, what an interesting start to an article in my news reader. Yes, I
am Calvin Spealman. Brett goes on to talk about some details of this,
mostly repeating and rephrasing what I set him straight on (his words,
not mine), in reguards to LINQ.
Although we can not, at this time, get the AST for any expressions or
blocks prior to compilation, I don't expect or see how or why we would
reach this at Python 2.6, either. Firstly, I don't see how python would
no to not-compile anything without some special "this is meant to be
used just for its AST" syntax. Secondly, I doubt it would be any cheaper
to generate the AST without compiling it into bytecode, after factoring
in the time it might take to figure out if you need to do so or not. The
most likely and efficient way will probably be the most obvious, in this
case: pass a function object, built with def or lambda, but expressions
by themselves (ie, not lambdas) will be pretty unusable. Anything else
would require some kind of mechanism to know that a parameter expects
AST, and that would break the python function model. So, barring
anything along the lines of function decorators that say "parameter 3
gets the expression's AST" and hooks in the function call mechanism to
catch this sort of thing, I don't see the direction of the Python 2.6
comment. Besides, anything along those lines seems like it would pose
some serious security risks.
Am I misunderstanding the statement?
