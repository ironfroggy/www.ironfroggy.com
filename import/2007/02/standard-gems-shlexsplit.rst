str.split() is so well known, but a simple step beyond leaves a lot of
pythonistas lost: how do you split without breaking up embedded strings?
How do you split "1 '2 3' 4" into ['1', '2 3', '4']? Why, shlex.split("1
'2 3' 4"), of course! The shlex module is a lexical analyzer and
includes this little useful utility for us.
