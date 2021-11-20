#!/usr/bin/env python3.9

from asterisk.agi import AGI
from fuzzywuzzy import process
from requests import post
from itertools import chain
import json
import sys

# Init
agi = AGI()
hass_url = 'http://localhost:8123'
hass_token = ''

# Setup string match
actions = {
    "light on": {
        "sentences": ["άναψε το φώς", "turn on the light"],
        "event": "light/turn_on",
        "payload": {'entity_id': 'light.myroom'},
        "type": "command"
    },
    "light off": {
        "sentences": ["σβήσε το φώς", "turn off the light"],
        "event": "light/turn_off",
        "payload": {'entity_id': 'light.myroom'},
        "type": "command"
    },
    "door lock": {
        "sentences": ["κλείδωσε την πόρτα", "lock the door"],
        "event": "lock/lock",
        "payload": {'entity_id': 'lock.frontdoor_up'},
        "type": "command"
    },
    "time": {
        "sentences": ["what time is it", "what is the date", "what day is it"],
        "payload": {"template": "the date is {{ now().strftime('%A %d of %B %H:%M') }}"},
        "type": "template"
    }
}

strOptions = list(chain.from_iterable([value['sentences'] for key, value in actions.items()]))
sentense, score = process.extractOne(sys.argv[1], strOptions)
for key, value in actions.items():
    if sentense in value['sentences']:
        action = key

# Home Assistant
if score > 80:
    payload = json.dumps(actions[action]['payload'])
    if actions[action]['type'] == 'command':
        event = actions[action]['event']
        url = f"{hass_url}/api/services/{event}"
        headers = {
            "Authorization": f"Bearer {hass_token}",
            "content-type": "application/json",
        }
        response = post(url, headers=headers, data=payload)
        agi.set_variable("hass_result", f"Executed command {action}")
    elif actions[action]['type'] == 'template':
        url = f"{hass_url}/api/template"
        headers = {
            "Authorization": f"Bearer {hass_token}",
            "content-type": "application/json",
        }
        response = post(url, headers=headers, data=payload)
        print(response)
        agi.set_variable("hass_result", response.text)
else:
    agi.set_variable("hass_result", "Couldn't recognise what you said")

