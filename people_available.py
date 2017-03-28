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
    frenchgirlnames = ['Inès','Lola','Camille','Sarah','Louise','Lilou','Lena',u'Maëlys',
                   'Clara','Eva','Lina',u'Anaïs','Louna','Romane','Juliette','Lucie',
                   'Ambre','Alice','Lou','Lisa',u'Clémence','Jeanne','Louane',
                   'Mathilde',u'Océane','Charlotte','Marie',u'Noémie','Celia','Anna',
                   'Nina','Pauline','Agathe','Elena','Leane',u'Éloïse',u'Émilie','Yasmine',
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
