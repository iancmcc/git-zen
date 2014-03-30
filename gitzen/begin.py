#!/usr/bin/env python
# -*- coding: utf-8 -*-
from gitflow.core import GitFlow
from gitflow.exceptions import NoSuchRemoteError


def begin(repo, feature):
    gitflow = GitFlow(repo)
    if not gitflow.is_initialized():
        gitflow.init(force_defaults=True)
    stashed = False
    if gitflow.is_dirty():
        stashed = True
        gitflow.git.stash()
    gitflow.create("feature", feature, "develop", fetch=False)

    try:
        if gitflow.origin().repo != repo:
            gitflow.publish("feature", feature)
    except NoSuchRemoteError:
        pass
    if stashed:
        gitflow.git.stash("pop")
