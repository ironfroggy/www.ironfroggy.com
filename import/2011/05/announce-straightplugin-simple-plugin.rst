Tonight I uploaded straight.plugin 1.1 to the Python Package Index. This
release includes a new loader, straight.plugin.loaders.ClassLoader and
adds an subclasses parameter to the simple load() API to invoke class
loading, opposed to the default module loading. The classes are filtered
by type and are looked up in the same modules that would be loaded by
the ModuleLoader available in straight.plugin 1.0. This release has been
testing on Python 2.7 and 3.2.

.. container::

.. container::

   You can check out the `source at
   github <https://github.com/ironfroggy/straight.plugin>`__ or the
   `packages at
   PyPI <http://pypi.python.org/pypi/straight.plugin/1.1>`__.
