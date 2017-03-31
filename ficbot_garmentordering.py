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
import people_available as peeps
import actions_available as acts
from inanimate import Doodad

def garment_ordering(config):
    greeting = seamstress_greeting(config)
    goose = wild_goose_chase(config)
    return "{greeting} {goose}".format(**vars())


def seamstress_greeting(config):
    if config.seamstress == peeps.musichetta:
        adv_phrase = random.choice([' who was dressed very fashionably herself'
                                       , ' her fortune-teller\'s eyes sparkling'
                                       , ' who was looking very happy and plumper than ever'
                                       , ' putting down a volume of poetry'
                                       , ' putting down a book of poems'
                                       , ' putting down the play she had been reading'
                                    ])
    else:
        adv_phrase = random.choice([' laughing'
                                    , ' merrily'
                                    , ' who seemed to find the whole thing a great joke'
                                    , ' with a smile so broad it was very nearly a laugh'
                                    ])

    return '<p>"Of course I can make you a {config.garment.name}, Citizen {config.protagonist.name}," ' \
           'said {config.seamstress.name},{adv_phrase}. ' \
           '"But would you mind doing me a favour?</p>'.format(**vars())


def wild_goose_chase(config):
    goose_people = config.amis + config.seamstresses
    if config.protagonist in goose_people:
        goose_people.remove(config.protagonist)
    if config.confidant in goose_people:
        goose_people.remove(config.confidant)
    random.shuffle(goose_people)
    while goose_people[0] == config.seamstress:
        random.shuffle(goose_people) #otherwise she sends a message to herself
    errand_receiver = goose_people[0]
    errand_sender = config.seamstress
    Doodad.listof = Doodad.listof*2
    doodad = Doodad.listof[0]
    if doodad.pluralised == 's': indexical = 'this'
    else:
        indexical = 'these'
    reason = random.choice(doodad.reasons)
    sentence = '<p>Could you take these {indexical} {doodad.name} to {errand_receiver.name}? {reason}" </p>\n'.format(**vars())

    i = 1
    while errand_receiver != config.seamstress:
        speaker = random.choice([config.protagonist, config.confidant])
        affirmation = random.choice(['Of course', 'No problem', 'You can count on us'])
        movement = random.choice(['It was a bit of a distance, but they took the', 'They brought the'
                                     , 'They took the', 'It was a short walk to take the'
                                     , 'It took them very little time to take the'
                                     , 'In short order they carried the'
                                    , 'They chatted to one another as they took the'
                                  ])
        additional_sentence = '<p>"{affirmation}," said {speaker.name}.</p> <p>{movement} {doodad.name} to ' \
                              '{errand_receiver.name}. {errand_receiver.comment}</p>\n'.format(
            **vars())
        errand_sender = errand_receiver
        errand_receiver = goose_people[i]
        doodad = Doodad.listof[i+1]
        reason = random.choice(doodad.reasons)
        if doodad.pluralised == 's': indexical = 'this'
        else: indexical = 'these'
        thanks = random.choice (['Thank you so much', 'That will do nicely', 'Just the ticket', 'Just what we needed'])
        exhortation = random.choice(['Since you\'re here', 'By the way', 'Now', 'You\'ve been a great help already, but'])
        imprecation = random.choice(['would you mind carrying', 'do you think you could take', 'would you be able to bring'
                                     ,'could you help me to get', 'would you be a dear and bring'])
        i = i + 1
        third_sentence = '<p>"{thanks}," said {errand_sender.name}. "{exhortation}, {imprecation}' \
                         ' {indexical} {doodad.name} to  {errand_receiver.name}? {reason}"</p>\n'.format(**vars())
        sentence = "{sentence} {additional_sentence} {third_sentence}".format(**vars())
    return sentence
