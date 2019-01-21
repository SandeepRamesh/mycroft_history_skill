#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 21 10:45:47 2019

@author: sramesh2
"""

import requests
url = 'http://history.muffinlabs.com/date'

r = requests.get(url)
json_output = r.json()

output = json_output['data']
events = output['Events']
births = output['Births']
deaths = output['Deaths']

todays_event = events[0]['text']
print(todays_event)