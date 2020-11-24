| ` <profile/13682774192456462795>`__\ So, after posting about the
  exception raising list comprehensions, I got this:

   `Kevin <profile/13682774192456462795>`__ has left a new comment on
   your post "`How to Add Memory Leaks to
   Python <http://ironfroggy-code.blogspot.com/2007/09/how-to-add-memory-leaks-to-python.html>`__":
   Doesn't '_' only exist in the interactive interpreter?

| Kevin has a misunderstanding here in that there is a huge difference
  between the expressions \_ and the locals()["_[1]"]. You might spot
  why they are so different, or you might not. The second, the one from
  the list comprehension, is unable to be accessed by name directly. You
  can only get at it via the locals() and globals() functions, depending
  on your scope (locals() always works right after the LC in question,
  though). The name is intentially something that, if tried to resolve
  as an actual name in the scope, won't find the object in question.
  Python will look for \_ and then do a subscript lookup on key 1 on it.
  This is completely different than actually looking up the name \_[1]
  in the dictionary where names are stored and grabbing up the value its
  bound to.
| So, Kevin, your question can be answered in that its irrelevant,
  because we aren't dealing with \_ at all. Also, open your profile so I
  can respond to you directly, next time.
