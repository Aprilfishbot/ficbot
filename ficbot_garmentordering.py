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
import people_available
import actions_available as acts

def garment_ordering(config):
    greeting = seamstress_greeting(config)
    goose = wild_goose_chase(config)
    return "{greeting} {goose}".format(**vars())


def seamstress_greeting(config):
    return '"Of course I can make you a {config.garment.name}, said {config.seamstress.name}. But would you mind ' \
           'running a few errands for me?'.format(**vars())


def wild_goose_chase(config):
    goose_people = config.amis + config.seamstresses
    goose_people.pop(0)
    goose_people.pop(1)
    errand_receiver = goose_people[0]
    errand_sender = config.seamstress
    sentence = 'Would you mind taking this message to {errand_receiver.name}?"\n'.format(**vars())
    random.shuffle(goose_people)
    i = 0
    while errand_receiver != config.seamstress:
        additional_sentence = '"Of course," they said.\n They brought the note to {errand_receiver.name}.\n'.format(
            **vars())
        errand_sender = errand_receiver
        errand_receiver = goose_people[i]
        i = i + 1
        third_sentence = '"Thank you so much," said {errand_sender.name}. "Since youre here, would you mind carrying' \
                         ' this message to  {errand_receiver.name}?\n'.format(**vars())
        sentence = "{sentence} {additional_sentence} {third_sentence}".format(**vars())
    return sentence
