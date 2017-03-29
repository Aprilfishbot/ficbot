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


def garment_wanted(config, current_time):
    walking = a_and_b_are_walking(config, current_time)
    want = a_forms_desire(config, current_time)
    says = a_expresses_desire(config)
    suggestion = b_suggests_seamstress(config)

    garment_wanted_intimacy = 0

    return "{walking} {want} {says} {suggestion} \n".format(
        **vars()
    )


def a_and_b_are_walking(config, current_time):
    walked = random.choice(acts.walked_pl.names)
    exposit = "{config.protagonist.name} and {config.confidant.name} {walked} in {config.story_start_place.name}.".format(**vars())
    describe = describe_surroundings(current_time, config.story_start_place.name)
    busy = they_were_busy(config, current_time)
    sentencelist = [exposit, describe, busy]
    random.shuffle(sentencelist)
    sentences = " ".join(sentencelist)
    return "{sentences}\n".format(
        **vars()
    )


def they_were_busy(config, current_time):
    days = (current_time - datetime.datetime(year=1832, month=6, day=6)).days
    if days < 30:
        t = "{days} days".format(**vars())
    else:
        months = days/30
        if months == 1:
            s = ''
        else:
            s = 's'
        t= "{months} month{s}".format(**vars())

    agosentences = [Template("Since the declaration of the new Republic ${timescale} ago"),
                 Template("The ${timescale} since the declaration of the new Republic seemed like an age. Ever since"),
                 Template("It seemed scarcely possible that it had been only ${timescale} since the deposition of Louis-Philippe. Since then"),
                 ]

    ago = random.choice(agosentences).substitute(timescale = t)
    rare = rare_treat()

    busysentences = [Template("${raresentence} ${agosentence}, ${protagonist} "
                              "and ${confidant} had been rushed off their feet.")
                     , Template("${raresentence} ${agosentence}, ${protagonist} had "
                                "hardly had a moment to ${pronoun}self.")
                     , Template ("${raresentence} ${agosentence}, they had been ${adverb} busy${swept}.")
                     , Template("")
                     ]
    busy = random.choice(busysentences).substitute(raresentence=rare
                                                   , agosentence=ago
                                                   , protagonist=config.protagonist.name
                                                   , confidant=config.confidant.name
                                                   , pronoun=config.protagonist.pronoun_obj
                                                   , adverb = random.choice(['tremendously', 'marvellously', 'terribly'
                                                                                , 'so awfully', 'so very'])
                                                   , swept = random.choice([', swept off their feet in a frenzy of activity'
                                                                            , ', tending to the needs of the new Republic'
                                                                            , ''])
                                                   )
    return "{busy} \n".format(**vars())


def rare_treat():
    if random.random() < 0.4:
        return "It was rare to have this moment of peace."
    elif random.random <0.4:
        return "This was a rare treat"
    elif random.random < 0.2:
        return "They were determined to make the use of their free time."
    else:
        return ""


def a_forms_desire(config, current_time):
    intimacy = expression_of_intimacy(config)
    worry = expression_of_worry(config)
    todo = much_to_do(config)
    wedding = wedding_mention(config)
    return "{intimacy} {worry} {todo} {wedding}\n".format(
        **vars()
    )


def expression_of_intimacy(config):
    intimate_moments = [Template("${protagonist} touched ${confidant}'s arm${adjective}.")
                        , Template("${protagonist} took ${confidant} by the arm${adjective}.")
                        , Template("${protagonist} took ${confidant}'s hand${adjective}.")
                        , Template("${protagonist} looked at ${confidant}${adjective}.")
                        ]
    return random.choice(intimate_moments).substitute(protagonist=config.protagonist.name
                                                      , confidant=config.confidant.name
                                                      , adjective = random.choice([" gently"
                                                                                      , " softly"
                                                                                      , " quietly"
                                                                                      , ""])
                                                      )


def expression_of_worry(config):
    worried_moments = ( [Template("${confidant_pronoun} looked tired.")
                       , Template("${confidant_pronoun} looked ${tired} but happy.")
                       ] *2
                        + [Template("")]
                        )
    return random.choice(worried_moments).substitute(confidant_pronoun=config.confidant.pronoun_sub.title(),
                                                     tired =random.choice(["tired", "exhausted", "worn out", "pale"]))

def much_to_do(config):
    expression_of_urgency = [Template("There was ${always}so much ${still}to do.")
                              , Template("Every day there was a never-ending stream of things to do.")]
    return random.choice(expression_of_urgency).substitute(always=random.choice(["always ", ""])
                                                           ,still=random.choice(['still ', '']))

def wedding_mention(config):
    if config.protagonist == peeps.cosette:
        weddingsentences = ["But amidst all this, Cosette was anxious to be married."]
    elif config.protagonist in set(peeps.household):
        weddingsentences = ["But there was still one more thing that needed planning, namely: the wedding."]
    else:
        weddingsentences = ["But nobody had lost sight of the prospect of Marius' wedding."]
    return random.choice(weddingsentences)

def a_expresses_desire(config):
    return '"I want a {config.garment.name}," said {config.protagonist.name}.\n'.format(
        **vars()
    )


def b_suggests_seamstress(config):
    return '"I know just the person," said {config.confidant.name}. "Her name is {config.seamstress.name}. ' \
           'She will make you a lovely {config.garment.name}."\n'.format(
        **vars()
    )
