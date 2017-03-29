#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from things import Thing


class Action(Thing):
    listof = []
    def __init__(self, name, names, transitive=0):
        Thing.__init__(self, name, names, 0, None)
        self.transitive = transitive
        Action.listof.append(self)
