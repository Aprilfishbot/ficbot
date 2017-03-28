import random
import datetime
from ficbot_initialise import create_config
from sentence_builder import describe_surroundings



"""
CONSTRUCT THE STORY
"""
config = create_config(datetime.datetime.now())

current_time = config.story_start_time




def garment_story(config):
    return "{} {} {}".format(
        garment_desire_expressed(config)
        , garment_ordering(config)
        , garment_collection(config)
    )

def garment_desire_expressed(config):
    walking = a_and_b_are_walking(config)
    want = a_forms_desire(config)
    says = a_expresses_desire(config)
    suggestion = b_suggests_seamstress(config)

    return "{walking} {want} {says} {suggestion}".format(
        **vars()
    )

def a_and_b_are_walking(config):
    exposit = "{config.protagonist.name} and {config.confidant.name} were walking in {config.story_start_place.name}.".format(**vars())
    describe = describe_surroundings(current_time, config.story_start_place.name)
    sentences = " ".join([exposit, describe])
    return "{sentences}".format(
        **vars()
    )

def a_forms_desire(config):
    return "{config.protagonist.name} wanted a {config.garment.name}.".format(
        **vars()
    )

def a_expresses_desire(config):
    return '"I want a {config.garment.name}," said {config.protagonist.name}.'.format(
        **vars()
    )

def b_suggests_seamstress(config):
    return '"I know just the person," said {config.confidant.name}. "Her name is {config.seamstress.name}. ' \
           'She will make you a lovely {config.garment.name}."'.format(
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
    if random.random() <0.9:
        return garment_story(config)
    else:
        return "skating story placeholder"
        #skating(config)
print tell_story()
