# Partly modified versions of gitflow's tests.handlers
# Copyright (c) 2010-2011 Vincent Driessen
# Copyright (c) 2012-2013 Hartmut Goebel
# Released under the BSD License
from unittest import TestCase
from functools import wraps

import py.path
from git import Repo


def in_tmpdir(f):
    @wraps(f)
    def inner(self, *args, **kwargs):
        assert isinstance(self, TestCase)
        tmpdir = py.path.local.mkdtemp()
        self.addCleanup(tmpdir.remove)
        self.sandbox = tmpdir
        with tmpdir.as_cwd():
            f(self, *args, **kwargs)
    return inner


def copy_fixture(fixture):
    def decorator(f):
        @wraps(f)
        @in_tmpdir
        def inner(self, *args, **kwargs):
            fdir = py.path.local(__file__).dirpath().join('fixtures',
                                                          fixture)
            dest = self.sandbox.join(fixture)
            fdir.copy(dest)
            dest.join('dot_git').rename('.git')
            self.repo = Repo(dest.strpath)
            with dest.as_cwd():
                f(self, *args, **kwargs)
        return inner
    return decorator


def clone_fixture(fixture):
    def decorator(f):
        @wraps(f)
        @in_tmpdir
        def inner(self, *args, **kwargs):
            fdir = py.path.local(__file__).dirpath().join('fixtures',
                    fixture, 'dot_git')
            self.repo = Repo(fdir.strpath).clone(self.sandbox.strpath)
            f(self, *args, **kwargs)
        return inner
    return decorator


def remote_clone_fixture(fixture):
    def decorator(f):
        @wraps(f)
        @in_tmpdir
        def inner(self, *args, **kwargs):
            fdir = py.path.local(__file__).dirpath().join('fixtures', fixture)
            dest = self.sandbox.join("remote")
            fdir.copy(dest)
            dest.join('dot_git').rename('.git')
            self.remote = Repo(dest.strpath)
            clone = self.sandbox.join('clone')
            self.repo = self.remote.clone(clone.strpath, origin='origin')
            with clone.as_cwd():
                f(self, *args, **kwargs)
        return inner
    return decorator


def commit(repo, message, append=True, filename="newfile"):
    mode = 'a' if append else 'w'
    with py.path.local(repo.working_dir).as_cwd():
        with open(filename, mode) as f:
            f.write("Making a change.\n")
    repo.index.add([filename])
    return repo.index.commit(message)
