#!/usr/bin/env python3

from asterisk.agi import AGI
import speech_recognition as sr

# Init
agi = AGI()
record_file = '/tmp/asterisk_record'
language = 'el-GR'
out_format = 'wav'
agi.set_variable("recognition", "")

# Record audio
agi.verbose("python agi started")
agi.record_file(record_file, timeout=10000, format=out_format, silence=2, escape_digits='0')

# Speech Recognition
r = sr.Recognizer()
with sr.AudioFile(f"{record_file}.{out_format}") as source:
    audio = r.record(source)
result = r.recognize_google(audio, language=language)
agi.set_variable("recognition", result)

