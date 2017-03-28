#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals

import random
import datetime
from datetime import date
from ficbot_initialise import create_config
from sentence_builder import describe_surroundings
import people_available




"""
CONSTRUCT THE STORY
"""


def garment_story(config):
    current_time = config.story_start_time
    want = garment_desire_expressed(config, current_time)
    order = garment_ordering(config)
    collect = garment_collection(config)
    return "{want} {order} {collect}".format(
        **vars()
    )

def garment_desire_expressed(config, current_time):
    walking = a_and_b_are_walking(config, current_time)
    want = a_forms_desire(config, current_time)
    says = a_expresses_desire(config)
    suggestion = b_suggests_seamstress(config)

    return "{walking} {want} {says} {suggestion} \n".format(
        **vars()
    )

def a_and_b_are_walking(config, current_time):
    walkinglist = ['were walking in', 'were going for a stroll in', 'were taking the air in']
    walking = random.choice(walkinglist)
    exposit = "{config.protagonist.name} and {config.confidant.name} were walking in {config.story_start_place.name}.".format(**vars())
    describe = describe_surroundings(current_time, config.story_start_place.name)
    sentencelist = [exposit, describe]
    random.shuffle(sentencelist)
    sentences = " ".join(sentencelist)
    return "{sentences}\n".format(
        **vars()
    )

def a_forms_desire(config, current_time):
    busy = they_were_busy(config, current_time)
    return "{busy} {config.protagonist.name} wanted a {config.garment.name}.\n".format(
        **vars()
    )

def they_were_busy(config, current_time):
    days = (current_time - datetime.datetime(year=1832, month=6, day=6)).days
    if days < 30:
        timescale = "{days} days".format(**vars())
    else:
        months = days/30
        if months == 1:
            s = ''
        else:
            s = 's'
        timescale = "{months} month{s}".format(**vars())

    sentences = ["Since the declaration of the new Republic {timescale} ago".format(**vars()),
                 "The {timescale} since the declaration of the new Republic seemed like an age. Ever since".format(**vars()),
                 "It seemed scarcely possible that it had been only {timescale} since the deposition of Louis-Philippe. Since then".format(**vars()),
                 ]

    ago = random.choice(sentences)
    rare = rare_treat()

    if config.protagonist == people_available.cosette:
        busy = "{rare} {ago}, {config.protagonist.name} and {config.confidant.name} had been rushed off their feet.".format(**vars())
    else:
        busy = "{rare} {ago}, {config.protagonist.name} had hardly had a moment to himself.".format(**vars())

    return "{busy}\n".format(**vars())

def rare_treat():

    if random.random() < 0.4:
        return "It was rare to have this moment of peace."
    elif random.random <0.4:
        return "This was a rare treat"
    elif random.random < 0.2:
        return "They were determined to make the use of their free time."
    else:
        return ""

def a_expresses_desire(config):
    return '"I want a {config.garment.name}," said {config.protagonist.name}.\n'.format(
        **vars()
    )

def b_suggests_seamstress(config):
    return '"I know just the person," said {config.confidant.name}. "Her name is {config.seamstress.name}.' \
           'She will make you a lovely {config.garment.name}."\n'.format(
        **vars()
    )

def garment_ordering(config):
    return "So they ordered a {config.garment.name}.".format(
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

    if random.random() <0.9:
        return garment_story(config)
    else:
        return "skating story placeholder"
        #skating(config)
print tell_story()
