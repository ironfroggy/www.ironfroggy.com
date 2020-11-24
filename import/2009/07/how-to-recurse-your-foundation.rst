.. container::

   .. container::

      Or, the working title: How To Look Down At The Tower of Turtles
      We're a recursive bunch. We're more repetitive than . There is no
      shortage of writing that its caches all the way down or that we're
      repeating the mainframe/dumb terminal era. I have an argument that
      our entire profession is hinged on repeating ourselves.

   .. container::

   .. container::

      Repetition is in the DNA of what we do. Software is the ultimate
      commodity, approaching zero-cost production. Solve one problem and
      the solution is applied to a thousand problems. Generalize and
      solve a million. Everything we do is repeated and is about
      repeating things. At the core, we're just moving little bits
      around and we repeat that action over and over, with very slight
      alterations. We abstract the repetition, and then we repeat the
      abstraction so much we need to abstract that.

   .. container::

   .. container::

      We could continue to make individual observations, like the
      mammoth stack of caches every bit goes through or the abstractions
      we build up over and over on top of our languages and toolsets.
      Look at the core of this and you find an axiom in everything we
      do. We're all about doing whatever we do a lot as efficiently as
      possible. When we realized a block of code might need to be used
      in different places, we created functions and subroutines. When we
      needed to fetch and refetch the same data from memory, we build
      caches inside our CPUs. Libraries helped us reuse code and version
      control systems helped us apply one developers changes to the
      whole teams' workstations. Google needed to do roughly the same
      thing on thousands of machines and abstracted the whole thing with
      not just MapReduce, but some of the smartest, most effective
      sysadmin work we've ever seen.

   .. container::

   .. container::

      We should accept and appreciate the overall pattern that has been
      driving hundreds of individual observations. The difficult part is
      to benefit from the knowledge. How do we make what we do better by
      understanding such a core axiom that drives everything we do?

   .. container::

      Why You Should Stop Complaining

   .. container::

   .. container::

      Things change and the work you do is alsways going to change. In
      some businesses, this is slow. In ours, it is very quick. I've
      seen people complaining about high-level languages. There are some
      who are quick to ignore the claims of benefits from such things as
      Cloud Computing and other new things they believe to be worthless.
      We are in danger of being stubborn. You cannot become entrenched
      in tradition or "the way we've always done it" in an industry that
      moves this fast. While the traditional databases and static typing
      have served us well for decades, this is no negative point to the
      value of other concepts (both new and simply revisited).

   .. container::

   .. container::

      The relational database, as traditionally envisioned, often hits a
      very predictable and known wall: the bounds of any single machine.
      Yes, there is master-master replication. Yes, there are clustering
      techniques that can take advantage of additional hardware in
      particular ways. Yes, you can shard the data across multiple
      database machines. The growth of the database from a single
      machine to many is indicative of the greater pattern we see over
      and over again, of the need to do something over and over again
      commoditizing the individual acts and components.

   .. container::

   .. container::

      Stretching your database over double-digits and triple-digits and
      more of hardware, and maintaining a high growth rate over that
      cluster, and eventually over super clusters, does something
      interesting to your view of the individual databases: they barely
      matter. When everything is managed by a single PostgreSQL, Oracle,
      or MySQL running machine, there is a tendency to do a decent
      amount of specific tuning. What kind of indexing do you need to
      build on which fields? What is the most efficient column layout
      for this table? These are questions that matter. Now, when you
      need to store several dozens of terabytes across hundreds of
      machines, these are details you'll think about as often as Java
      developers think about CPU registers.

   .. container::

   .. container::

      There is no shortage of developers who will soundly tell you just
      how buzzword loving and stupid everyone who enjoys Cloud Computing
      is. Databases are always going to be important, they tell us. Most
      of us don't need to scale like Amazon or Google or eBay, they tell
      us. They are correct, but they miss the point.

   .. container::

   .. container::

      There are two reasons commodity scale computing benefits
      developers and a group of developers for each reason.

   .. container::

   .. container::

      Why That Guy In His Basement Cares About This

   .. container::

   .. container::

      No, the hobbyist making little web apps doesn't need to scale to
      huge loads, high traffic, or enormous datasets. However, those who
      do drive every aspect of dealing with all the details involved
      into commodity status. This is not special to our industry. There
      are independent car companies, thousands of t-shirt companies, and
      the driving down of restaurant opening costs so much that their
      barely profitable. Isn't business grand?

   .. container::

   .. container::

      Why That Guy In The Corner Office Cares About This

   .. container::

   .. container::

      Imagine the growing company in the late 90s building their website
      growth and investing in a dozen or so heavy machines to run nice
      Oracle databases, which are obviously good choices because they're
      expensive and therefor good. The DBA team makes careful estimates
      of the needs their machines will face and plans the roles of each
      box carefully. They map out the schema, build the databases,
      establish their procedures and policies. Everything has its place.

   .. container::

   .. container::

      Then one of the machines dies, thanks to a rare but statistically
      inevitable hardware failure. There is no saving it. The data was
      backed up, and easily retrievable, but downtime is still
      inevitable.

   .. container::

   .. container::

      Contrast this to the cloud mentality's most important aspect:
      individuals don't matter. Individual machines don't matter,
      because functionality and data are spread out and replicated.
      Individual processes don't matter, because state is persisted and
      broken up into many services and workers, who can drop and spawn
      at the drop of a hat.
