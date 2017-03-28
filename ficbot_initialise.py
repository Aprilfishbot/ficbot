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
SETTING THE INITIAL ENTITIES
"""
## pick random date between June 7th 1832 and December 31st 1832
story_start_time = radar.random_date (
    start = datetime.datetime(year=1832, month = 6, day = 7),
    stop = datetime.datetime (year = 1832, month = 12, day =31)
)
if story_start_time.hour <8:
    story_start_time = story_start_time + timedelta(hours = 8)
if story_start_time.hour>20:
    story_start_time = story_start_time - timedelta(hours=8)

## pick the place where they're walking

story_start_place = random.choice(Place.listof)

## pick her confidant

confidant = random.choice(household)

## pick a garment

garment = random.choice(Garment.listof)

#pick a seamstress

seamstress = random.choice(seamstresses)




"""
INITIALISE TO CONFIG
"""
def create_config(seed):
    random.seed(seed)
    config = Config(protagonist, confidant, seamstress, story_start_place, story_start_time, garment)
    return config