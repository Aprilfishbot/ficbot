#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from things import Thing


class Inanimate(Thing):
    listof = []

    def __init__(self, name, names, pluralised = 's', plural = 's'):
        Thing.__init__(self, name, names)
        Inanimate.listof.append(self)
        self.pluralised = pluralised
        if plural == 's':
            self.plural = name + 's'
        else:
            self.plural = plural

class Garment(Thing):
    listof = []

    def __init__(self, name, names, elements, gender = 'F'):
        Thing.__init__(self, name, names)
        Garment.listof.append(self)
        self.elements = list(elements)
        self.gender = gender


class Doodad(Thing):
    listof = []

    def __init__(self, name, names, reasons, pluralised='s'):
        Thing.__init__(self, name, names)
        self.reasons = reasons
        self.pluralised = pluralised
        Doodad.listof.append(self)