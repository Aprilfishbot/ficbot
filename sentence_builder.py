import random
import datetime

from settings import Place, timeofday
from states import Weather


def describe_surroundings(time, place):
    current_weather = random.choice(Weather.listof)
    current_timeofday = timeofday(time)
    description = 'It was a {current_weather.name} {current_timeofday}'.format(**vars())
    if random.random()<0.3:
        return '{}.'.format(description)
    else:
        return '{}; {}.'.format(description, more_description(time, place))


def more_description(time, place):
    return "further description"