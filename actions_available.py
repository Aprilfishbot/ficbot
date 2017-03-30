#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from actions import Action

wanted_thing = Action('wanted', ['wanted, wished, desired, longed for, wished for, dreamed of, hoped for'], 1)
wanted_action = Action('wanted', ['wanted, longed, wished, hoped'])
walked_sng = Action('walked', ['was walking', 'was going for a stroll', 'was taking the air'])
walked_pl = Action('walked', ['were walking', 'were going for a stroll', 'were taking the air'])
said = Action('said', ['said, remarked'])