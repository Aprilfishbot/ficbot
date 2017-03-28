#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from inanimate import Inanimate, Garment

Inanimate('bird','', 'p')
Inanimate('soil','', 's')
Inanimate('leaf','', 'p', 'leaves')
Inanimate('cloud','','p')
Inanimate('paving stone','','p')
Inanimate('street','','p')
Inanimate('building','','p')
Inanimate('sky','','s')
Inanimate('butterfly','','p', 'butterflies')
Inanimate('weather','','s')
Inanimate('revolution','','s')

Garment("morning dress", "", "sleeves, tippet, collar, skirts, ruffles, belt")
Garment("evening gown", "", "sleeves, neckline, skirts, ruffles, sash, skirt-trim")
Garment("mantle", "", "hood, cape-collar, lining, trim")
Garment("bonnet", "", "brim, trim, ribbons, lining")
