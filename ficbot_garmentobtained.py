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
    element = random.choice(config.garment.elements)
    if config.garment.gender == 'M':
        descriptions = ['embroidered', 'purple', 'gold', 'damask', 'scarlet', 'crimson', 'silk', 'velvet']
    else:
        descriptions = ['ruffled', 'silk', 'crimson', 'rose-pink', 'lace', 'embroidered', 'sky blue']

    description = random.choice(descriptions)

    detailcomment = Template("${protagonist} especially admired the ${description} ${component}.").substitute(
                                protagonist=config.protagonist.name
                                , description=description
                                , component=element
                                )

    if 'sleeves' in set(config.garment.elements):
        sleevecomment = random.choice(['The sleeves were the widest she had ever seen. '])
    else:
        sleevecomment = ''

    return "<p>When they arrived, {config.seamstress.name} had the {config.garment.name} ready. It was perfect. " \
           "{detailcomment} {sleevecomment}" \
           "They were very happy to be together, and happy to be free.</p>".format(**vars())