#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Function to read STATIONS file

:copyright:
    Martin van Driel (Martin@vanDriel.de)
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from __future__ import absolute_import

import numpy as np
from source import Receiver

def read_STATIONS(filename):
    f = open(filename, 'r')
    receivers = []

    for line in f:
        name, network, lat, lon, elev, bury = line.split()
        lat = float(lat)
        lon = float(lon)
        receivers.append(Receiver(lat, lon, name, network))

    f.close

    return receivers