import os
import re
import datetime
import string

from fabric.contrib.project import rsync_project
from fabric.contrib.files import upload_template
from fabric.api import local, run, sudo
from fabric.state import env

env.hosts = ['192.241.197.18']
env.deploy_dir = '/var/www/'

def root():
    env.user = 'root'

def clean():
    local('find . -name "*.swp" -delete')
    local('rm -fr _build/*')

def build(deployprefix=None):
    if deployprefix:
        local('jules build -f -d ' + deployprefix)
    else:
        local('jules build -f')

def localbuild(port='8000'):
    local('jules build -f -D -d localhost:' + port)

def deploy(delete=True):
    now = datetime.datetime.now()
    if local('git diff', capture=True).strip():
        local('git commit -am "Committing deploy version at %s"' % now.strftime('%Y-%m-%d %H:%M'))
        local('git push')
    build()
    rsync_project(env.deploy_dir, '_build/', delete=delete)

def update_apache():
    rsync_project('apache.conf', '/etc/apache2/', delete=False)

def setup_domain(domain):
    sudo('mkdir /var/www/%s' % (domain,))

def user_create(user):
    user = user or local('whoami').strip()
    sudo('adduser --disabled-password --gecos "" %s' % (user,))
    user_key(user)

def user_key(user):
    sudo('mkdir -p /home/%s/.ssh/' % (user,))
    sudo('chown {0}:{0} /home/{0}/.ssh/'.format(user))
    sudo('chmod go= /home/{0}/.ssh/'.format(user))
    sudo('chmod u=rwx /home/{0}/.ssh/'.format(user))
    pubkey_path = os.path.join(os.path.expanduser('~'+user), '.ssh', 'id_rsa.pub')
    pubkey = open(pubkey_path).read()
    run('echo "%s" >> /home/%s/.ssh/authorized_keys' % (pubkey, user))
    sudo('chmod u=rwx /home/{0}/.ssh/authorized_keys'.format(user))

def user_pw():
    run('passwd')

def setup_domain_user():
    username = local('whoami')

def domain(domain):
    env.domain = domain
    env.deploy_dir += domain + '/'

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
        tags = raw_input('tags: ').split(','),
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

    post_path = os.path.join('contents', key) + '.yaml'
    with open(post_path, 'w') as f:
        f.write(template.format(**params))
        if params['series']:
            f.write('series: ')
            f.write(params['series'])
            f.write('\n')

        f.write('tags:\n')
        for tag in params['tags']:
            f.write('- ' + tag + '\n')

        f.write('content: |\n')
        f.write('    ' + params['content'] + '\n')
        f.write(params['content'])
        f.write('\n')

        for filename in os.listdir('queue'):
            lines = list(open(os.path.join('queue', filename)))
            for line in lines:
                f.write('    ' + line)
            os.unlink(os.path.join('queue', filename))

    local('git add %s' % (post_path,))
    local('git commit -m "Added %s"' % (params['title'],))

    localbuild()
