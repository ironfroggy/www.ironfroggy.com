| Discussions and my first PEP will hopefully lead to "fixing" super in
  3.0 and could probably also be backported to 2.x branches. The two
  threads are linked here, and I'm going to include the reference
  implementation so anyone can check it out and comment on the design.

-  http://mail.python.org/pipermail/python-3000/2007-April/006667.html
-  http://mail.python.org/pipermail/python-dev/2007-April/072807.html

| 

::

        #!/usr/bin/env python
        #
        # newsuper.py

        import sys

        class SuperMetaclass(type):
            def __getattr__(cls, attr):
                calling_frame = sys._getframe().f_back
                instance_name = calling_frame.f_code.co_varnames[0]
                instance = calling_frame.f_locals[instance_name]
                return getattr(instance.__super__, attr)

        class Super(object):
            __metaclass__ = SuperMetaclass
            def __init__(self, type, obj=None):
                if isinstance(obj, Super):
                    obj = obj.__obj__
                self.__type__ = type
                self.__obj__ = obj
            def __get__(self, obj, cls=None):
                if obj is None:
                    raise Exception('only supports instances')
                else:
                    return Super(self.__type__, obj)
            def __getattr__(self, attr):
                mro = iter(self.__obj__.__class__.__mro__)
                for cls in mro:
                    if cls is self.__type__:
                        break
                for cls in mro:
                    if attr in cls.__dict__:
                        x = cls.__dict__[attr]
                        if hasattr(x, '__get__'):
                            x = x.__get__(self, cls)
                        return x
                raise AttributeError, attr

        class autosuper(type):
            def __init__(cls, name, bases, clsdict):
                cls.__super__ = Super(cls)

        if __name__ == '__main__':
            class A(object):
                __metaclass__ = autosuper
                def f(self):
                    return 'A'

            class B(A):
                def f(self):
                    return 'B' + Super.f()

            class C(A):
                def f(self):
                    return 'C' + Super.f()

            class D(B, C):
                def f(self, arg=None):
                    var = None
                    return 'D' + Super.f()

            assert D().f() == 'DBCA'

| 
| What do you think?
