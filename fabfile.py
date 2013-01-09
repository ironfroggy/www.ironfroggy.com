import os
import re
import datetime
import string

from fabric.contrib.project import rsync_project
from fabric.api import local, run, sudo
from fabric.state import env


env.hosts = ['www.ironfroggy.com']
env.user = 'calvin'

def clean():
    local('find . -name "*.swp" -delete')
    local('rm -fr _build/*')

def build():
    local('jules build -f')

def deploy(delete=True):
    rsync_project('/domains/www.ironfroggy.com/default/', '_build/', delete=delete)

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
template: post.j2
"""

DATEFMT = '%Y-%m-%d %H:%M:00'

def new(key=None):
    params = dict(
        title = raw_input("title: "),
        key = key or raw_input("path: "),
        series = raw_input("series: "),
        now = datetime.datetime.now().strftime(DATEFMT),
        content = raw_input("content: "),
    )
    if not params['key']:
        params['key'] = key = params['title'].lower().replace(' ', '-')
        assert re.match(r'[-a-z/]*', key)
    else:
        key = params['key']

    path_parts = key.split('/')
    for i in range(1, len(path_parts)):
        part_path = os.path.join('contents', *path_parts[:i])
        if not os.path.exists(part_path):
            os.mkdir(part_path)

    if not params['content']:
        open(os.path.join('contents', key) + '.rst', 'w')

    with open(os.path.join('contents', key) + '.yaml', 'w') as f:
        f.write(template.format(**params))
        if params['series']:
            f.write('series: ')
            f.write(params['series'])
            f.write('\n')
        if params['content']:
            f.write('content: ')
            f.write(params['content'])
            f.write('\n')
