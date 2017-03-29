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


class Config(object):
    def __init__(self, protagonist, confidant, seamstress, story_start_place, story_start_time, garment):
        self.protagonist = protagonist
        self.confidant = confidant
        self.seamstress = seamstress
        self.story_start_place = story_start_place
        self.story_start_time = story_start_time
        self.garment = garment




"""
INITIALISE TO CONFIG
"""
def create_config(seed):
    random.seed(seed)
    random.shuffle(amis)
    random.shuffle(household)
    seamstresses = create_seamstresses()
    random.shuffle(seamstresses)

    ## pick a random date somewhere between bd and the end of the year
    story_start_time = radar.random_date(
        start=datetime.datetime(year=1832, month=6, day=7),
        stop=datetime.datetime(year=1832, month=12, day=31)
    )
    if story_start_time.hour < 8:
        story_start_time = story_start_time + timedelta(hours=8)
    if story_start_time.hour > 20:
        story_start_time = story_start_time - timedelta(hours=8)

    ## pick the place where they're walking

    story_start_place = random.choice(Place.listof)

    ## pick a protagonist
    if random.random() < 0.8:
        protagonist = cosette
    else:
        protagonist = amis[0]

    ## pick a confidant
    if protagonist == cosette:
        confidant = random.choice(household)
    else:
        confidant = amis[1]

    ## pick a garment
    if protagonist.gender == 'F':
        garment = random.choice([x for x in Garment.listof if x.gender == 'F'])
    else:
        garment = random.choice([x for x in Garment.listof if x.gender == 'M'])
    # pick a seamstress
    seamstress = seamstresses[0]

    config = Config(protagonist, confidant, seamstress, story_start_place, story_start_time, garment)
    return config