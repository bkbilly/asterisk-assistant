#!/usr/bin/env python3

from asterisk.agi import AGI
import speech_recognition as sr
from gtts import gTTS

record_file = '/tmp/asterisk_record'
tts_file = '/tmp/asterisk_tts'
language = 'el-GR'
out_format = 'wav'

agi = AGI()
agi.verbose("Python AGI started")
agi.record_file(record_file, timeout=10000, format=out_format, silence=1, escape_digits='0')

r = sr.Recognizer()

with sr.AudioFile(f"{record_file}.{out_format}") as source:
    audio = r.record(source)
result = r.recognize_google(audio, language=language)
agi.set_variable("recognition", result)

tts = gTTS(result)
tts.save(f"{tts_file}.mp3")
agi.stream_file(f"{tts_file}", escape_digits='0')

