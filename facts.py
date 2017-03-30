#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from things import Thing
from actions import Action

# ~*~*~*~*~*~*I never used these but whatever*~*~*~*~*~*~

class Fact(Thing):
    def __init__(self, subjectof, objectof, verb):
        listof = []
        Thing.__init__(self, 'The fact that' + subjectof + verb + objectof, '')
        Fact.listof.append(self)
        self.subjectof = subjectof
        self.objectof = objectof
        self.verb = Action

    @property
    def getsubject(self):
        return self.subjectof.name

    @property
    def getobject(self):
        return self.objectof.name



class Opinion(Fact):
    listof = []
    def __init__(self, subjectof, objectof, judgement):
        Fact.__init__(self, subjectof, objectof, 'judged')
        Fact.listof.append(self)
        self.judgement = judgement

    @property
    def getJudgement(self):
        return self.judgement