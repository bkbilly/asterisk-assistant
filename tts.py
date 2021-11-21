#!/usr/bin/env python3.9

from asterisk.agi import AGI
from gtts import gTTS
import sys

# Init
tts_file = '/tmp/asterisk_tts'
volume_boost = 10
agi = AGI()

# TTS
tts = gTTS(sys.argv[1])
tts.save(f"{tts_file}.mp3")
agi.stream_file(f"{tts_file}", escape_digits='0')

