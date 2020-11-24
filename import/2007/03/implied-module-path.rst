| We all know there is an implied path to import from for the main
  module, but it seems a few people get mixed about the details of how
  this works. In particular, it seems that this path is being confused
  for the current working directory. Here is a little note to help
  remember the distinction.

-  Any module implicitly can import packages and modules in the same
   directory its file resides in, which is
   os.path.dirname(the_module.__file__)
-  Often you run a script, when starting out, from its own directory, so
   that this implied path is the current working directory. This fact is
   purely a coincidence.

The result boils down simply to understanding that any import can be
relative to the module it appears in, and if you run a local (not
system-wide available) script, that just happens to be your current
directory, by coincidence.
