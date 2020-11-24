As a support package for some other things, I've written a little module
called ExtSession. The basic idea is to have an easy way to control a
python session running in another process. You can simply instansiate
the ExtSession class, and call the execute() method. The results are
asyncronous-like, but will be improved later. Very likely support will
be added to get Deferreds. For now, you can simply poll or wait. The
results of each execute() call (best done one line at a time) are
seperated and returned individually of output from other commands,
making it very easy to work with over a session's lifetime.
Following is a stripped pydoc pull of the docstrings. I hope someone
finds this as useful as I think I will.
NAME
extsession
FILE
/home/calvin/extsession/extsession.py
DESCRIPTION
ExtSession Module
For executing code in an external interpreter.
There are many cases where operations are either intensive or blocking
by
waiting, and in both situations the extsession module can be used to
control
a python session in a seperate process for the purposes of executing
code
in parellel without the dangers associated with threads or the
complexities
in dealing with asyncronous frameworks.
The core of extsession is the ExtSession class. See its help for
details.
Also, look at the exteval and extexec functions for quick, blocking code
execution in a fresh interpreter. (note: these functions do not execute
in
parellel, only in a seperate process, but blocking the original)
CLASSES
\__builtin__.object
ExtEval
ExtResults
ExtSession
Session
class ExtEval(__builtin__.object)
\| Evaluates expressions in a new process with an asyncronous result.
\|
\| The result attribute evaluates to the result of the expression, or
access
\| raises a ValueError, if the result is not ready.
\|
\| Methods defined here:
\|
\| \__init__(self, expr)
\|
\|
----------------------------------------------------------------------
\| Properties defined here:
\|
\| result
\| = \_get_result(self)
\| Get the result only if its ready.
\|
\|
----------------------------------------------------------------------
\| Data and other attributes defined here:
\|
\| \__dict_\_ =
\| dictionary for instance variables (if defined)
\|
\| \__weakref_\_ =
\| list of weak references to the object (if defined)
class ExtResults(__builtin__.object)
\| Represents results from an operation in another process.
\|
\| Methods defined here:
\|
\| \__init__(self, stdout, stderr, done)
\|
\| read(self, size=None)
\| Read data from stdout of process from operation.
\| Raises ValueError if the operation is not complete.
\|
\| wait(self)
\| Return only when the operation is complete.
\|
\|
----------------------------------------------------------------------
\| Data and other attributes defined here:
\|
\| \__dict_\_ =
\| dictionary for instance variables (if defined)
\|
\| \__weakref_\_ =
\| list of weak references to the object (if defined)
class ExtSession(__builtin__.object)
\| Controls a python session in another process.
\|
\| Methods defined here:
\|
\| \__getitem__(self, name)
\|
\| \__init__(self)
\|
\| execute(self, source)
\| Execute arbitrary python source.
\| Returns an ExtResults object to access the results.
\|
\| exit(self, code=0)
\|
\| readcodes(self)
\|
\| readline(self)
\|
\| writeline(self, line)
\|
\|
----------------------------------------------------------------------
\| Data and other attributes defined here:
\|
\| \__dict_\_ =
\| dictionary for instance variables (if defined)
\|
\| \__weakref_\_ =
\| list of weak references to the object (if defined)
class Session(__builtin__.object)
\| Manages the session in this process. Used by ExtSession in spawned
\| interpreters. Can also be used for a very light sandbox in the same
\| process.
\|
\| Methods defined here:
\|
\| \__init__(self)
\|
\| execute(self, source, stdout_fn=None, stderr_fn=None, done_fn=None)
\| Executes code in a semi-controlled environment and redirects output
\| to given stdout and stderr filenames, or random temp locations.
Writes
\| a code to the file at done_fn when finished. A code of 'DONE' is
\| expected. When a code appears in the done file, the stdout and stderr
\| files are ready for reading and are complete.
\|
\|
----------------------------------------------------------------------
\| Data and other attributes defined here:
\|
\| \__dict_\_ =
\| dictionary for instance variables (if defined)
\|
\| \__weakref_\_ =
\| list of weak references to the object (if defined)
FUNCTIONS
exteval(expression)
Creates a new process running a new python interpreter, evaluates the
given expression, and returns the result. The result must be basic
types,
but may expand in the future to any pickle-capable type.
extexec(source)
Creates a new process, executes the source in a new python interpreter,
and returns a tuple of the stdout and stderr captured.
sleep(...)
sleep(seconds)
Delay execution for a given number of seconds. The argument may be
a floating point number for subsecond precision.
