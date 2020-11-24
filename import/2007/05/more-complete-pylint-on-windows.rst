| `Others <http://mateusz.loskot.net/2006/01/15/running-pylint-from-komodo/>`__
  have posted about getting pylint installed on Windows, but I always
  fell short getting the steps to lead to the destination. Some
  tinkering and I got it right. This also includes the instructions to
  get it integrated into `Komodo <http://activestate.com/>`__.

#. Grabbing the Goods
   First off the bat we need to grab all the packages we need. pylint
   depends on two other packages from Logilabs, who write pylint for us.
   We need to grab the latest releases of
   `pylint <http://www.logilab.org/view?rql=Any%20X%20WHERE%20X%20eid%20857>`__,
   `logilab-astng <http://www.logilab.org/view?rql=Any%20X%20WHERE%20X%20eid%20856>`__,
   and
   `logilab-common <http://www.logilab.org/view?rql=Any%20X%20WHERE%20X%20eid%20848>`__.
#. Extract all of these somewhere to install from.
#. Open a command shell and move to each of the directories, executing
   the install command in each:
   python setup.py install
#. Feel free to remove the extracted files now that everything has been
   installed. You can use pylint now. On to Komodo integration.
#. In Komodo, open the toolbox from the View menu with
   View->Tabs->Toolbox. Now, click your "Add Item to Toolbox" button in
   the new tab, and select "New Command..." to add a command to Komodo
   that will analyze your current file with pylint.
#. For the command enter the line 'python -c "import
   sys,pylint.lint;pylint.lint.Run(sys.argv[1:])" "%F"'. This will
   import pylint, handle spaces in Windows filenames, and run the
   processing on your file.
#. Check the "Parse output with:" box and enter this regular expression
   to parse the lines from pylint,
   '.*?:(?P<line>\d+):\s*(?P<content>.*?)$'. Also, check the "Show
   parsed output as list" box.
#. Optionally, bind a key shortcut from the Key Binding tab. I use
   ctrl+alt+L.

|image0|

.. |image0| image:: http://2.bp.blogspot.com/_wACg_J16I_8/Rj9jC2tNk8I/AAAAAAAAABk/H7R52AkMGdQ/s400/komodopylint.png
   :name: BLOGGER_PHOTO_ID_5061873406883763138
   :target: http://2.bp.blogspot.com/_wACg_J16I_8/Rj9jC2tNk8I/AAAAAAAAABk/H7R52AkMGdQ/s1600-h/komodopylint.png
