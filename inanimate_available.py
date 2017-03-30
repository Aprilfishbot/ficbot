#!/usr/bin/python
# -*- coding: latin-1 -*-
from __future__ import unicode_literals
from inanimate import Inanimate, Garment, Doodad

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
weddingdress=Garment("dress","", "sleeves, tippet, collar, skirts, ruffles, belt")
Garment("mantle", "", "hood, cape-collar, lining, trim")
Garment("bonnet", "", "brim, trim, ribbons, lining")
Garment("coat", "", "sleeves, lapels", 'M')
Garment("waistcoat", "", "panels, lapels, buttons", 'M')

Doodad("medicines", '', ['They\'re needed for the free clinic.', 'There are a few families over in that area who need them.'], 'p')
Doodad("message", '', ['It\'s rather important.', 'Feel free to read it if you wish, it\'s nothing interesting.'
                        , 'Oh, and please don\'t break the seal.'], 's')
Doodad("maps", '', ['It\'s important that we distribute ones with the new place names.'
                        , 'The old ones are useless since so many streets were renamed.'], 'p')
Doodad("candles", '', ['There are families who need them.'
                        , 'The schoolroom is running low.'], 'p')
Doodad("potatoes", '', ['They\'re making a hearty stew in the free kitchen tomorrow.'
                        , 'There are a lot of mouths that need feeding.'], 'p')
Doodad("pencils", '', ['They\'re for the infant school.'
                        , 'The high school girls need something to write with, after all.'], 'p')
Doodad("newspapers", '', ['They\'re a bit heavy, I hope that\'s all right.'
                        , 'Today\'s edition, no less!'], 'p')
