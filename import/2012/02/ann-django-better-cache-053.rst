| I've added a small, but useful, addition to Django Better Cache,
  today. The new bettercache.decorators.CachedFormMethod utility is a
  decorator for Django form methods, which is essentially a memoizer,
  but with a nice twist.
| This is great for forms that include DB or search index reading
  methods which can be expensive and you'd like to cache, but normal
  memoization fails when the important parameters to key on are in the
  form data, not the arguments to the actual method.
| Read about the new decorator at the
  `docs <http://readthedocs.org/docs/django-better-cache/en/latest/cachemodel.html#cachedformmethod>`__
  to learn more.

::

   class FriendsLookup(forms.Form):

       username = forms.CharField(required=True)

       @CachedFormMethod(expires=60*15) # expire in 15 minutes
       def get_friends_list(self, include_pending=False):
           username = self.cleaned_data['username']
           friends = Friendship.objects.filter(
               from_user__username=username)
           if include_pending:
               friends = friends.filter(status__in=(PENDING, APPROVED))
           else:
               friends = friends.filter(status=APPROVED)

           return friends 
