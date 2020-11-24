This situation comes up, from time to time, when we need to get
something to happen after a many-to-many field is changed. The novice
will connect a post_save signal and scratch his head when it doesn't
fire on the addition or removal of items in the ManyToManyField. We all
learn that it takes a slightly more complicated signal, the `m2m_changed
signal, and its many
actions <http://docs.djangoproject.com/en/dev/ref/signals/#m2m-changed>`__,
which tell us exactly what has changed in the particular field sending
it (the signal comes from the field's through table, to be exact).

.. container::

.. container::

   Well, a slightly more complicated case arose in a design today and I
   was scratching my head and feeling like a novice all over again. You
   see, I needed to know when new things had been adding to such a
   field, but I had more than one. In fact, I had four of them. I needed
   a specific function called on the instance when all of these fields
   were finished being cleared or added to or subtracted from. This was
   in a form in the Django admin.

.. container::

.. container::

   Thankfully I had an assumption I could make this easier with: the
   fields in question would only be set from the admin interface. With
   this knowledge in hand, I hopped into the app's admin.py and I added
   these methods:
       def response_change(self, request, obj):
           response = super(MyAdmin, self).response_change(request, obj)
           obj.do_thing()
           return response
       def response_add(self, request, obj, \*args, \**kwargs):
           response = super(MyAdmin, self).response_add(request, obj,
   \*args, \**kwargs)
           obj.do_thing()
           return response
   These get called when the admin interface is used to edit and create
   a new object, respectively. It happens *after* both the model
   instance itself and all of the many-to-many fields have been saved,
   which is exactly what we need. It works, but I wish I could find a
   better solution.
