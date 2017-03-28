#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from things import Thing
import datetime

class Place(Thing):
    listof = []
    def __init__(self, name, names = ''):
        Thing.__init__(self, name, names)
        Place.listof.append(self)

def timeofday(dt):
    if dt.hour<12: return 'morning'
    elif dt.hour <18: return 'afternoon'
    elif dt.hour <21: return 'evening'


