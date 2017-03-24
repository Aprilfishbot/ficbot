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



#BITS THAT CAN GO ANYWHERE
## Cosette thinks about Marius

## Cosette thinks about anything really

## Description of the surroundings in political terms
## BasicSceneSetting

def describe_surroundings(time, place):
    current_weather = random.choice(Weather.listof)
    current_timeofday = timeofday(time)
    description = 'It was a {current_weather.name} {current_timeofday}'.format(**vars())
    if random.random()<0.3:
        return '{}.'.format(description)
    else:
        return '{}; {}.'.format(description, 'and so ends the sentence')


## Cosette remembers?



# -- Cosette and her confidant go for a walk. the revolution has succeeded
## pick random date between June 7th 1832 and December 31st 1832
story_start_time = radar.random_date (
    start = datetime.datetime(year=1832, month = 6, day = 7),
    stop = datetime.datetime (year = 1832, month = 12, day =31)
)

print story_start_time

if story_start_time.hour <8:
    story_start_time = story_start_time + timedelta(hours = 8)

if story_start_time.hour>20:
    story_start_time = story_start_time - timedelta(hours=8)

current_time = story_start_time


## pick the place where they're walking

current_place = random.choice(Place.listof)
print current_place.name


## pick her confidant

confidant = random.choice(household)

## >DescribeSurroundings

print describe_surroundings(story_start_time,current_place)

# -- Cosette wants a garment
## pick random garment

## pick reason

## > FormOpinion (want garment)

## > Speech (want garment)



# -- Her confidant gives advice as to where to go to get a garment.
## if confidant = marius then 'my friend knows' etc

## if confidant = valjean or toussaint then 'one of marius' strange friends knows' etc

# -- It's either 1) Musichetta or 2) BLM
## pick random seamstress


# -- They go to visit the seamstress
# -- Cosette describes her garment
# -- They agree a timeframe
# M: Musichetta sends Cosette on [A Romantic Adventure]
# B: The Laughing Mistress sends Cosette on [A Political Adventure]
# Cosette returns to pick up the garment
#