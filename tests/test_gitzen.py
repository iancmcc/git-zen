#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_gitzen
----------------------------------

Tests for `gitzen` module.
"""

import unittest
from tests.utils import clone_fixture, copy_fixture, remote_clone_fixture

from gitzen.begin import begin


def has_branch(repo, name):
    for branch in repo.branches:
        if branch.name == name:
            return True
    return False


class TestBegin(unittest.TestCase):

    @clone_fixture('clean_repo')
    def test_initialization(self):
        begin(self.repo, "x")
        self.assert_(has_branch(self.repo, "develop"))
        self.assert_(has_branch(self.repo, "master"))

    @copy_fixture('dirty_repo')
    def test_init_with_dirty(self):
        begin(self.repo, "x")
        self.assert_(has_branch(self.repo, "develop"))
        self.assert_(has_branch(self.repo, "master"))
        self.assert_(self.repo.is_dirty())

    @clone_fixture('clean_repo')
    def test_newfeature(self):
        begin(self.repo, "testfeature")
        self.assert_(has_branch(self.repo, "feature/testfeature"))
        self.assert_(has_branch(self.repo, "develop"))
        self.assertFalse(self.repo.is_dirty())

    @copy_fixture('dirty_repo')
    def test_newfeature_with_dirty(self):
        begin(self.repo, "testfeature")
        self.assert_(has_branch(self.repo, "feature/testfeature"))
        self.assert_(has_branch(self.repo, "develop"))
        self.assert_(self.repo.is_dirty())

    @remote_clone_fixture('clean_repo')
    def test_publish(self):
        begin(self.repo, "testfeature")
        self.assert_(has_branch(self.repo, "feature/testfeature"))
        self.assert_(has_branch(self.repo, "develop"))
        self.assert_(has_branch(self.remote, "feature/testfeature"))




if __name__ == '__main__':
    unittest.main()