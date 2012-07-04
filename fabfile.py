import os
import datetime
import string

from fabric.contrib.project import rsync_project
from fabric.api import local, run, sudo
from fabric.state import env


env.hosts = ['www.ironfroggy.com']

def clean():
    local('find . -name "*.swp" -delete')

def build():
    local('jules build -f')

def deploy():
    build()
    rsync_project('/domains/www.ironfroggy.com/default/', '_build/')
