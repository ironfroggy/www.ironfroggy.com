Sphinx is awesome for writing documentation. ReadTheDocs is awesome for
hosting it. Autodocs are great for covering your entire API easily.
Django is a great framework that makes my job easier.
Between these four things is an interaction that only brought me pain,
however. I'm here to help the next dev avoid this.
Autodocs works by importing your modules and walking over the classes
and functions to build documentation out of the existing docstrings. It
can be used to generate complete API docs quickly and keep them in sync
with the libraries existing docstrings, so you won't get conflicts
between your docs and your code. Fantastic.
This creates a problem when used with Django applications, where many
things cannot be imported unless a valid settings module can be found.
This can prevent a hurdle in some situations, and requires a little
boilerplate to get working properly with Sphinx. It require a little
extra to get working on ReadTheDocs. What makes this particularly hard
to figure out, is the environment running on their servers is not the
same as your own, and you have only terse error reports to guess about.
Here is the snippet you need to add into the conf.py of your docs/ to
tell Sphinx how to load a settings.py.

.. container::

import sys, os
sys.path.append(os.path.dirname(__file__))
import django 
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
if django.VERSION < (1, 4):
    from django.core.management import setup_environ
    settings = \__import__(os.environ["DJANGO_SETTINGS_MODULE"])
    setup_environ(settings)
and a simple settings.py is all you need sitting beside that.

.. container::

# Django settings for docs project.
# import source code dir
import os
import sys
sys.path.insert(0, os.getcwd())
sys.path.insert(0, os.path.join(os.getcwd(), os.pardir))
SITE_ID = 303
DEBUG = True
TEMPLATE_DEBUG = DEBUG
DATABASES = {"default": {
    "NAME": ":memory:",
    "ENGINE": "django.db.backends.sqlite3",
    "USER": '',
    "PASSWORD": '',
    "PORT": '',
}}
INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'YOUR_APP_HERE', # This is where you put your app
)
And you should be good to go!
