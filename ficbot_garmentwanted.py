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
import inanimate_available as inan

def garment_wanted(config, current_time):
    walking = a_and_b_are_walking(config, current_time)
    want = a_forms_desire(config, current_time)
    says = a_expresses_desire(config)
    suggestion = b_suggests_seamstress(config)

    return "{walking} {want} {says} {suggestion}\n".format(
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
    return "<p>{sentences}</p>".format(
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
    return "{busy}".format(**vars())


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
    return "<p>{intimacy} {worry} {todo} </p><p>{wedding}</p>".format(
        **vars()
    )


def expression_of_intimacy(config):
    intimate_moments = [Template("${protagonist} touched ${confidant}'s arm${adjective}. ${comment}")
                        , Template("${protagonist} took ${confidant} by the arm${adjective}. ${comment}")
                        , Template("${protagonist} took ${confidant}'s hand${adjective}. ${comment}")
                        , Template("${protagonist} looked at ${confidant}${adjective}. ${comment}")
                        ]
    return random.choice(intimate_moments).substitute(protagonist=config.protagonist.name
                                                      , confidant=config.confidant.name
                                                      , adjective = random.choice([" gently"
                                                                                      , " softly"
                                                                                      , " quietly"
                                                                                      , ""])
                                                      , comment = config.confidant.comment
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
    expression_of_urgency = [Template("There was ${always}so much ${still}to do")
                              , Template("Every day there was a never-ending stream of things to do")]
    urgent = random.choice(expression_of_urgency).substitute(always=random.choice(["always ", ""])
                                                           ,still=random.choice(['still ', '']))
    to_do = ''
    x_to_y = [{'x': 'children', 'y': 'educated'}
                , {'x': 'sick', 'y': 'nursed'}
                , {'x': 'gardens', 'y': 'tended'}
                , {'x': 'streets', 'y': 'cleaned'}
                , {'x': 'families', 'y': 'fed'}
                , {'x': 'newspapers', 'y': 'printed'}
                , {'x': 'poems', 'y': 'recited'}
                ]
    random.shuffle(x_to_y)
    for num in [0, 1, 2]:
        phrase = Template("${x} to be ${y}").substitute(x_to_y[num])
        if num == 0: punc = ":"
        else: punc = ","
        to_do = "{to_do}{punc} {phrase}".format(**vars())
    return "{urgent}{to_do}.".format(**vars())

def wedding_mention(config):
    if config.protagonist == peeps.cosette:
        weddingsentences = ["But amidst all this, Cosette had something on her mind."]
    elif config.protagonist in set(peeps.household):
        weddingsentences = ["But there was still one more thing that needed planning, namely: the wedding."]
    else:
        weddingsentences = ["But nobody had lost sight of the prospect of Marius\' wedding."
                                          , "But they were all expecting to attend Marius\' wedding."
                                          , "But they were all making time to attend Marius\' wedding."]
    return random.choice(weddingsentences)

def a_expresses_desire(config):
    if config.protagonist == peeps.cosette:
        conversation_want = cosette_want_convo(config)
    elif config.protagonist in set(config.household):
        conversation_want = ""
    else:
        conversation_want = ami_want_convo(config)
    return "{conversation_want}".format(**vars())

def cosette_want_convo(config):
    if config.confidant == peeps.marius:
        config.garment = inan.weddingdress
        if random.random()<0.8:
            proposal = cosette_proposes_marriage(config)
        else:
            proposal = marius_proposes_marriage(config)
        discussion = cosette_discusses_marriage(config)
        return "{proposal} {discussion}".format(**vars())
    else:
        return cosette_wants_a_garment(config)

def cosette_proposes_marriage(config):
    proposalsentence = random.choice([Template('<p>"My darling,", said Cosette, "When are you going to marry me?"</p>')]
                                     ).substitute()
    reactionsentence = random.choice([Template('<p>Marius laughed.</p> <p>"I thought it was I who should be asking that," '
                                            'he said. "But perhaps that''s another relic of the past. And anyway'
                                            ', I was going to bring it up myself. How about the Sunday after next? '
                                            'I think we''re all free."</p>')]
                                      ).substitute()
    return "{proposalsentence} {reactionsentence}".format(**vars())


def marius_proposes_marriage(config):
    proposalsentence = random.choice([Template('<p>"My darling," said Marius, '
                                               '"would you like to marry me a week on Sunday?"</p>')]
                                     ).substitute()
    return "{proposalsentence}".format(**vars())

def cosette_discusses_marriage(config):
    cosetteaccepts = random.choice([Template('<p>Cosette couldn''t help smiling. "Why, of course," she said. '
                                             '"How does one do these things?"</p>')]
                                   ).substitute()
    mariusresponds = random.choice([Template('<p>"I really have no idea," said Marius. "I was going to ask Courfeyrac for help. '
                                    'I suppose you''ll need a dress."</p>')]
                                   ).substitute()
    dresswants = random.choice([Template('<p>"Oh yes," said Cosette. If there was one thing she knew about getting married, '
                                'it was that it certainly involved a dress.</p>')]
                               ).substitute()
    return "{cosetteaccepts} {mariusresponds} {dresswants}".format(**vars())

def cosette_wants_a_garment(config):
    if config.garment == inan.weddingdress:
        garmentwantingsentences = [Template('<p>Cosette took a deep breath.</p> <p>"I am getting married," she said, "and I need a ${garment}."</p>'),]
    else:
        garmentwantingsentences = [Template('<p>"I hope you won\'t think me frivolous," said Cosette, "but I should like'
                                            ' a new ${garment}."</p>')
                                   , Template ('<p>"I\'ve been wanting to talk to you about something," said Cosette. "The '
                                               'fact is, I - I want a new ${garment}."</p>')
                                   , Template ('<p>"I have a lot of new friends now," said Cosette, "and I - well, I feel'
                                               ' rather underdressed, to be honest. I would like a new ${garment}."</p>')
                                   ]
    return random.choice(garmentwantingsentences).substitute(garment = config.garment.name)

def ami_want_convo(config):
    conversationsentences = [Template('<p>"I\'m going to need a new ${garment} for Marius\' wedding, you know," said ${protagonist}</p>')
                             , Template('<p>"Marius is getting married," said ${protagonist}, "and I should like to look my'
                                      ' best. I think, all told, that I should get a new ${garment}"</p>')
                             ]
    return random.choice(conversationsentences).substitute(garment = config.garment.name, protagonist = config.protagonist.name)


def b_suggests_seamstress(config):
    if config.confidant == peeps.bahorel and config.seamstress == peeps.laughingmistress:
        sentence = random.choice([Template('<p>"Well," said Bahorel, "That should be easy. ${seamstress} can rustle '
                                           'you up a ${garment} in no time."</p>')
                                 ,])
    elif config.seamstress == peeps.musichetta and config.confidant in {peeps.joly, peeps.bossuet}:
        sentence = random.choice([Template('<p>"Well," said ${confidant}, "Musichetta can make you one. '
                                           'She\'s quite busy, but always happy to help a friend."</p>')
                                 ,])
    elif config.confidant == peeps.marius:
        sentence = random.choice([Template('<p>"Well," said ${confidant}, "We''re in luck. '
                                           'My friend''s, er, lady acquaintance does sewing and things. I think her name''s'
                                           '${seamstress} or something like that."</p>')
                                 ,])
    elif config.confidant in set(peeps.household):
        sentence = random.choice([Template('<p>"My dear," said ${confidant}, "Of course you do. '
                                           'Why not get it made by that friend of Marius''? The lady who came around'
                                           'the other day, what was her name, ${seamstress}."</p>')
                                 ,])
    else:
        sentence = random.choice([Template('<p>"Well," said ${confidant}, "in that case, it seems like the easiest thing'
                                           ' would be to have ${seamstress} make you one, if she\'s got the time."</p>')
                                  ])
    return sentence.substitute(confidant = config.confidant.name
                               , seamstress = config.seamstress.name
                               , garment = config.garment.name)

