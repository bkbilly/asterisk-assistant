#!/usr/bin/env python3

from asterisk.agi import AGI
from gtts import gTTS
from pydub import AudioSegment
import sys
import time

# Init
tts_file = '/tmp/asterisk_tts'
volume_boost = 3.5
agi = AGI()

# TTS
tts = gTTS(sys.argv[1])
tts.save(f"{tts_file}.mp3")
agi.verbose(f"Save as {tts_file}.mp3")
sound = AudioSegment.from_mp3(f"{tts_file}.mp3")
sound = sound.apply_gain(volume_boost)
sound = sound.set_frame_rate(8000)
sound = sound.set_channels(1)
sound.export(f"{tts_file}.wav", format="wav")
agi.verbose(f"Save as {tts_file}.wav")

#agi.set_variable("VOLUME(TX)", 15)
agi.stream_file(f"{tts_file}", escape_digits='0')
#agi.set_variable("VOLUME(TX)", 0)

