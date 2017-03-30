#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from things import Thing

class Person(Thing):
    listof = []
    def __init__(self, name, names, gender=None, comment=''):
        Thing.__init__(self, name, names, gender, 1)
        Person.listof.append(self)
        self.comment = comment



