| 
| I've made a small incremental release on Django Better Cache, adding a
  from_miss() method to handle cache misses in CacheModel objects. Now,
  you can define your cache model and how it initializes data when the
  cache is empty, and perform all your lookups through the CacheModel,
  expecting misses to auto-populate for you.
| You can see a quick example of the new functionality below, but I have
  also made large improvements to the documentation hosted over at
  `ReadTheDocs <http://readthedocs.org>`__, so go read the `full
  docs <http://readthedocs.org/docs/django-better-cache/en/latest/>`__
  right now, if you are interested.

::

   from bettercache.objects import CacheModel
   from django.contrib import auth

   class User(CacheModel):
       username = Key()
       email = Field()
       full_name = Field()

       def from_miss(self, username):
           user = auth.models.User.objects.get(username=username)
           self.email = user.email
           self.full_name = user.get_full_name()

| 
| If this ``get()`` does not find the object in the cache, it will
  create a new
| User instance and call ``from_miss()`` with the key parameter username
  to
| initialize it, and then save and return that object for you. The next
  call,
| it will find it in the cache.

::

   user = User.get(username="bob")
