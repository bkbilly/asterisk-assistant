#!/usr/bin/env python3.9

from asterisk.agi import AGI
from requests import post
import json

# Init
agi = AGI()
hass_url = 'http://localhost:8123'
hass_token = ''

# Home Assistant
event = 'light/toggle'
payload = json.dumps({'entity_id': 'light.kitchen'})
url = f"{hass_url}/api/services/{event}"
headers = {
    "Authorization": f"Bearer {hass_token}",
    "content-type": "application/json",
}
response = post(url, headers=headers, data=payload)

agi.set_variable("hass_result", result)

