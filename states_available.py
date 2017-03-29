#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from states import State, Weather, Mood, Judgement, Description

Weather('sunny', '', 1)
Weather ('rainy', '', 0)
Weather('cloudy', '', 0)
Weather('foggy', '', 0)
Weather('snowy', '', 0)
Weather('windy', '', 0)
Weather ('blustery', '', 0)
Weather('chilly', '', 0)
Weather ('fine', '', 1)

Judgement('good', '', 1)
Judgement('nice', '', 1)
Judgement('lovely', '', 1)
Judgement('gorgeous',  '',1)
Judgement('delightful', '', 1)
Judgement('horrid', '', 0)
Judgement('frightening', '', 0)
Judgement('strange',  '',0.5)
Judgement('peculiar',  '',0.5)

Description('exciting',  '',1)
Description('buzzing with energy',  '',1)
Description('singing', '', 1)
Description('full of life', '', 1)
Description('fresh', '', 1)
Description('reaching for the sky',  '', 1)
