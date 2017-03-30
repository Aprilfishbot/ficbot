#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals

import random
import datetime
from datetime import date
from string import Template
from ficbot_initialise import create_config
from ficbot_sentence_builder import describe_surroundings, substitute_dict
from ficbot_garmentwanted import garment_wanted
from ficbot_garmentordering import  garment_ordering
import people_available
import actions_available as acts


"""
CONSTRUCT THE STORY
"""


def garment_story(config):
    current_time = config.story_start_time
    want = garment_wanted(config, current_time)
    order = garment_ordering(config)
    collect = garment_collection(config)
    return "{want} {order} {collect}".format(
        **vars()
    )

def garment_collection(config):
    return "And then they picked it up.".format(
        **vars()
    )

"""
PUT IT ALL TOGETHER
"""
def tell_story():
    config = create_config(datetime.datetime.now())

    if random.random() <2:
        return garment_story(config)
    else:
        return "skating story placeholder"
        #skating(config)
print tell_story()

