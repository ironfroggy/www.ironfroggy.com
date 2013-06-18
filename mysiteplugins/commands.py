#!/usr/bin/env python

from __future__ import print_function

import os
import shutil
import operator
import itertools
from datetime import datetime

import yaml

from straight.command import Command, SubCommand, Option
from straight.plugin import load

import jules
from jules.plugins.commands import BaseCommand


class Test(BaseCommand):

    version = "0.1"
    help = "test command plugins"

    def execute(self, **kwargs):
        print("ENGINE", self.engine)


class TestCommand(SubCommand):
    name = 'test'
    command_class = Test
