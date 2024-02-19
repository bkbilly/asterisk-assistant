#!/usr/bin/env python3

from requests import post, get
import json
import sys
from pydub import AudioSegment
from asterisk.agi import AGI

# Init
agi = AGI()
tts_file = '/tmp/asterisk_tts_hass'
volume_boost = 1

# TTS
hass_url = 'http://localhost:8123'
hass_token = ''
headers = {
    "Authorization": f"Bearer {hass_token}",
    "content-type": "application/json",
}

lang = sys.argv[2]
voice = sys.argv[3]
action = {
    "message": sys.argv[1],
    "engine_id": "tts.piper",
    "language": lang,
    "options": {"voice": voice}
}

url = f"{hass_url}/api/tts_get_url"
response = post(url, headers=headers, data=json.dumps(action))
speech = response.json()

# Save and convert audio file
response = get(speech["url"], stream=True)
with open(f"{tts_file}.mp3", "wb") as file:
    for chunk in response.iter_content():
        if chunk:
            file.write(chunk)

agi.verbose(f"Save as {tts_file}.mp3")
sound = AudioSegment.from_mp3(f"{tts_file}.mp3")
sound = sound.apply_gain(volume_boost)
sound = sound.set_frame_rate(8000)
sound = sound.set_channels(1)
sound.export(f"{tts_file}.wav", format="wav")
agi.verbose(f"Save as {tts_file}.wav")

agi.stream_file(f"{tts_file}", escape_digits='0')
