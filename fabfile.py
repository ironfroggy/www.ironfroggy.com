import os
import datetime
import string

from fabric.contrib.project import rsync_project
from fabric.api import local, run, sudo
from fabric.state import env


env.hosts = ['www.ironfroggy.com']

def newpost(title=None, src=None):
    if title is None and src is not None:
        base = os.path.splitext(os.path.basename(src))[0]
        title = base.replace('-', ' ').title()
    alphanum = string.letters + string.digits
    slug = title.lower().replace(' ', '-')
    slug = ''.join(c for c in slug if c in alphanum + '-')
    now = datetime.datetime.now()
    filename = 'content/posts/{}-{}.html'.format(now.strftime('%Y-%m-%d'), slug)   
    if os.path.exists(filename):
        print "refusing to overwrite", filename
    else:
        with open(filename, 'w') as f:
            f.write('---\n')
            f.write('title: {}\n'.format(title))
            f.write("created: !!timestamp '{}'\n".format(now.strftime('%Y-%m-%d %H:%M:%S')))
            f.write('status: draft\n')
            f.write('---\n')
            f.write('\n')
            src = os.path.expanduser(src)
            if src and os.path.exists(src):
                f.writelines(open(src))

def build():
    local('jules build -f')

def deploy():
    build()
    rsync_project('/domains/www.ironfroggy.com/default/', '_build/')
