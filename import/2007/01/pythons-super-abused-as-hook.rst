| There has been some recent-ish discussion on the python-dev mailing
  list about "fixing" the super built-in, which is used to access
  attributes of an object with lookup rules on the superclass of a given
  class. This is used for different things and in different ways, but
  the most common usage seems to be as follows:

::

   class Foo(Bar):
      def action(self):
          super(Foo, self).action()
          self.actionCalledOnFooInstance = True

| 
| This causes a call to Foo().action() to call the action method of the
  next class in the Method Resolution Order. Now, Bar.action might
  exist, or maybe Bar inherits from Baz and Baz.action() will be called.
  The point is, you don't have to know. The typical pattern here is the
  that we are looking for the superclass of the same class we are within
  (Foo) and call the same method we're already in (action), which is a
  repetition some people want to fix.
| I propose that super() is not broken at all, or even failing, but
  simply that we are misusing it where anothing idiom may be more
  appropriate. The more appropriate idiom might be hooks. Sometimes our
  function using super() should actually be calling a hook and other
  times it should be the hook. In the example above, we want something
  to happen after the regular action() method is called, so we redefine
  the entire action() method to call the original and then execute our
  one little line. We require all the overhead and issues with super()
  largely for varients of this common use case. Instead, consider if we
  wrote the following:

::

   class Foo(Bar):
      def hook_after_action(self):
          self.actionCalledOnFooInstance = True

| 
| Do you see how much simpler that is? The requirement here is that
  either super(Foo, self).action would call hook_after_action if it
  exists (or there could be a default no-op version) or some mechanism
  outside of the action() method might handle it, perhaps wrapping it up
  on request or at definition. Maybe a standard hook format could even
  be a candidate for brining into the language.
| Hooks are very valuable concepts that are not used enough. We can save
  ourselves a lot of trouble by using them. There is a lot more I could
  say about them, but this post was mostly about their relation to the
  many use cases of super.
| PS - Some of this can be known to relate to the concept called
  "Aspect-Oriented Programm" which has very little weight in the Python
  world, because here its so easy to do that it doesn't deserve a name
  and is reduced to simply wrapping functions or having hooks.
