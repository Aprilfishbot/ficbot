#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
class Thing(object):
    listof = []
    def __init__(self, name, names=None, gender = None, person =0):
        self.name = name
        self.names = list(names)
        self.person = person
        self.gender = gender
        Thing.listof.append(self)

    @property
    def posessive(self):
        return self.name + "'s"

    @property
    def pronoun_sub(self):
        if self.person == 0:
            return'it'
        elif self.gender == 'M':
            return 'he'
        elif self.gender == 'F':
            return 'she'
        else:
            return 'they'

    @property
    def pronoun_obj(self):
        if self.person == 0:
            return'it'
        elif self.gender == 'M':
            return 'him'
        elif self.gender == 'F':
            return 'her'
        else:
            return 'them'

    @property
    def pronoun_pos(self):
        if self.person.equals(0):
            return 'its'
        elif self.gender.equals('M'):
            return 'his'
        elif self.gender.equals('F'):
            return 'her'
        else:
            return 'their'
