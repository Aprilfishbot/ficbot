#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from people import Person
import random

cosette = Person('Cosette', '', 'F')

#Cosette is the protagonist
protagonist = cosette

########## HOUSEHOLD

valjean = Person('Valjean', '', 'M')

marius = Person('Marius', '', 'M')

toussaint = Person('Toussaint', '', 'M')

#these are Cosette's household

household = [valjean, marius, toussaint]

######### WOMEN



def create_seamstresses():
    frenchgirlnames = ['In�s','Lola','Camille','Sarah','Louise','Lilou','Lena',u'Ma�lys',
                   'Clara','Eva','Lina',u'Ana�s','Louna','Romane','Juliette','Lucie',
                   'Ambre','Alice','Lou','Lisa',u'Cl�mence','Jeanne','Louane',
                   'Mathilde',u'Oc�ane','Charlotte','Marie',u'No�mie','Celia','Anna',
                   'Nina','Pauline','Agathe','Elena','Leane',u'�lo�se',u'�milie','Yasmine',
                   'Faustine','Sara','Gabrielle','Anaelle','Sofia','Capucine']
    laughingmistress = Person(random.choice(frenchgirlnames), '', 'F')
    musichetta = Person('Musichetta', '', 'F')
    #these are the people who can make clothes
    seamstresses = [musichetta, laughingmistress]
    return seamstresses

######### AMIS

enjolras = Person('Enjolras', '', 'M')

combeferre = Person('Combeferre', '', 'M')

prouvaire = Person('Jean Prouvaire', '', 'M')

courfeyrac = Person('Courfeyrac', '', 'M')

bahorel = Person('Bahorel', '', 'M')

bossuet = Person('Bossuet', 'Lesgle', 'M')

joly = Person('Joly', '', 'M')

grantaire = Person('Grantaire', '', 'M')

amis = [enjolras, combeferre, prouvaire, courfeyrac, bahorel, bossuet, joly]
