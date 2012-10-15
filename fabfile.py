import os
import re
import datetime
import string

from fabric.contrib.project import rsync_project
from fabric.api import local, run, sudo
from fabric.state import env


env.hosts = ['www.ironfroggy.com']

def clean():
    local('find . -name "*.swp" -delete')
    local('rm -fr _build/*')

def build():
    local('jules build -f')

def deploy():
    build()
    rsync_project('/domains/www.ironfroggy.com/default/', '_build/')

def update():
    clean()
    local('git pull')
    build()

template = """title: "{title}"
publish_time: !!timestamp '{now}'
updated_time: !!timestamp '{now}'
created_time: !!timestamp '{now}'
status: published
type: post
rnder: jinja2
template: post.j2
series: {series}
content: {content}
"""
def new():
    params = dict(
        title = raw_input("title: "),
        key = raw_input("path: "),
        series = raw_input("series: "),
        now = datetime.datetime.now().strftime('%Y-%M-%d %h:%m:%s'),
        content = raw_input("content: "),
    )
    if not params['key']:
        params['key'] = key = title.lower().replace(' ', '-')
        assert re.match(r'[-a-z/]*', key)
    else:
        key = params['key']
    if not params['content']:
        open(os.path.join('contents', key) + '.rst', 'w')
    with open(os.path.join('contents', key) + '.yaml', 'w') as f:
        f.write(template.format(**params))
