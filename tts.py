#!/usr/bin/env python3.9

from asterisk.agi import AGI
from gtts import gTTS
from pydub import AudioSegment
import sys

# Init
tts_file = '/tmp/asterisk_tts'
volume_boost = 10
agi = AGI()

# TTS
tts = gTTS(sys.argv[1])
tts.save(f"{tts_file}.mp3")
song = AudioSegment.from_mp3(f"{tts_file}.mp3")
song += volume_boost
song.export(f"{tts_file}.mp3", format='mp3')
agi.stream_file(f"{tts_file}", escape_digits='0')

