#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals

import random
import datetime
from datetime import date
from string import Template
from ficbot_initialise import create_config
from ficbot_sentence_builder import describe_surroundings, substitute_dict
import people_available as peeps
import actions_available as acts

def garment_collection(config):
    return "<p>When they arrived, {config.seamstress.name} had the {config.garment.name} ready. It was perfect. " \
           "They were very happy to be together, and happy to be free.</p>".format(**vars())