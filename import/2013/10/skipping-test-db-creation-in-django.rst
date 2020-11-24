| One of my colleagues at Caktus Group, Mark, as written up one of the
  most useful tips for Django developers trying to make good test
  coverage easier to digest for you team. Test running time is often a
  barrier to getting teams to follow good testing practices.

   Now what if you are running a set of tests which are only
   using \ ``SimpleTestCase``\  or the base \ ``unittest.TestCase``\ ?
   Then you don't really need the test database creation at all.
   Depending on the backend you are using, the number of tables you have
   and the number of tests you are running the database creation can
   take many times longer than running the test themselves.

..

   ... we can skip the database creation/teardown.

| I recommend any Django developers taking a look at the `very simple
  solution he's come up
  with <http://www.caktusgroup.com/blog/2013/10/02/skipping-test-db-creation/>`__,
  which I'm planning to absorb into all of my projects quickly.

    

..

    
