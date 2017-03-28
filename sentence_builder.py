#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
import random
import datetime
from datetime import timedelta
import radar


from actions import Action
from facts import Fact, Opinion
from inanimate import Inanimate
from people import Person
from settings import Place, timeofday
from states import State
from things import Thing

from actions_available import *
from inanimate_available import *
from people_available import *
from settings_available import *
from states_available import *
from things_available import *

def describe_surroundings(time, place):
    current_weather = random.choice(Weather.listof)
    current_timeofday = timeofday(time)
    description = 'It was a {current_weather.name} {current_timeofday}'.format(**vars())
    Fact(time.isoformat(), current_weather.name, 'was')
    is_it_ended_yet = random.random()
    description_sentence = '{}'.format(description)
    while is_it_ended_yet<0.6:
        description_sentence = '%s; %s' % (description_sentence, further_description(time, place))
        is_it_ended_yet = random.random()
    return '{description_sentence}.'.format(**vars())

def further_description(time, place):
    object_chosen = random.choice(Inanimate.listof)
    description_chosen = random.choice(Description.listof)
    if object_chosen.pluralised == 'p':
        object_name = object_chosen.plural
        verb = 'were'
    else:
        object_name = object_chosen.name
        verb = 'was'
    Fact(object_name, description_chosen.name, verb)
    return 'the {object_name} {verb} {description_chosen.name}'.format(**vars())
# TO DO: Change this so that instead a new list is created using random.sample and elements are iteratively selected from the list using pop()
# this should also change the issue with repeating descriptions