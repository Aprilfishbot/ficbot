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

class Garment(Inanimate):
    listof = []
    def __init__(self, name, names, elements):
        Inanimate.__init__(self, name, names)
        Garment.listof.append(self)
        self.elements = list(elements)

