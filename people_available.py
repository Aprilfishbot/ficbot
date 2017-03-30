#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from people import Person
import random


cosette = Person('Cosette', '', 'F')

########## HOUSEHOLD

valjean = Person('Valjean', '', 'M', 'Somehow he had seemed much more relaxed since June, although he wouldn\'t explain why.')
marius = Person('Marius', '', 'M')
toussaint = Person('Toussaint', '', 'F')

#these are Cosette's household

household = [valjean, marius, toussaint]

######### SEAMSTRESSES

musichetta = Person('Musichetta', '', 'F')
laughingmistress= Person('Charlotte', '', 'F', 'Her merry laugh was infectious.')
#these are the people who can make clothes
seamstresses = [musichetta, laughingmistress]


def name_laughingmistress(lm):
    frenchgirlnames = ['Inès','Lola','Camille','Sarah','Louise','Lilou','Lena',u'Maëlys',
                       'Clara','Eva','Lina',u'Anaïs','Louna','Romane','Juliette','Lucie',
                       'Ambre','Alice','Lou','Lisa',u'Clémence','Jeanne','Louane',
                       'Mathilde',u'Océane','Charlotte','Marie',u'Noémie','Celia','Anna',
                       'Nina','Pauline','Agathe','Elena','Leane',u'Éloïse',u'Émilie','Yasmine',
                       'Faustine','Sara','Gabrielle','Anaelle','Sofia','Capucine']
    lm.name = random.choice(frenchgirlnames)

######### AMIS

enjolras = Person('Enjolras', '', 'M')
combeferre = Person('Combeferre', '', 'M')
prouvaire = Person('Jean Prouvaire', '', 'M')
feuilly = Person('Feuilly', '', 'M')
courfeyrac = Person('Courfeyrac', '', 'M')
bahorel = Person('Bahorel', '', 'M')
bossuet = Person('Bossuet', 'Lesgle', 'M')
joly = Person('Joly', '', 'M')
grantaire = Person('Grantaire', '', 'M', 'Since the revolution, he had really sorted his life out.')


amis = [enjolras, combeferre, prouvaire, feuilly, courfeyrac, bahorel, bossuet, joly, grantaire]

