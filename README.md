# Asterisk Asssistant
Have a voice assistant on Asterisk PBX Server using Google for Speach recognition and for Text-to-Speech. It can integrate with Home Assistant by recognizing the intention of the speaker.

## How it works
There are three parts on the recognition (Speech Recognition, Text-to-Speech, Intent) on three seperate files:

### Speech Recognition (`sr.py`)
Records the speaker to a file as a wav and sends it to the recognizer to get the output text. This is stored in a variable called `${recognition}`.

### Text-to-Speech (`tts.py`)
Takes as a text argument and uploads it to google to get the audio file which is saved as an mp3. The audio file is then streamed to the listener.

### Text-to-Speech for Home Assistant (`tts_hass.py`)
It works similar as `tts.py`, but it connects to home assistant to use the piper speech recognition, though you could change.

### Intent (`hass.py`)
This finds the closest sentence that matches the sentences provided on the `actions` variable. It can support multiple sentences for the same event like you can see at the example provided on hass.py file.
There are some options that are needed for each action type so that they can communicate succesfully with Home assistant.

## Example of `extensions.conf`
Whith this example when you dial 45 it will direct you to the voiceassistant.
This is responsible for calling all the AGI scripts and repeat itself after each successfull recognition.
There are 3 ways to stop the excecution:
  - You Hang Up
  - You don't say anything (endvoice is triggered)
  - You say Goodbye which will trigger the end action type

```
[dialplan]
exten => 45,1,Gosub(voiceassistant,${EXTEN},1)

[voiceassistant]
exten => _X.,1,Answer()
exten => _X.,n,Set(VOLUME(TX)=15)
exten => _X.,n(startvoice),NoOP(Started voice assistant)
exten => _X.,n,agi(sr.py)
exten => _X.,n,GotoIf($["${recognition}" == ""]?endvoice)
exten => _X.,n,agi(hass.py,${recognition})
exten => _X.,n,agi(tts.py,${hass_text})
exten => _X.,n,agi(tts_hass.py,${hass_text},"en_US","en-us-amy-low")
exten => _X.,n,Goto(startvoice)
exten => _X.,n(endvoice),Hangup()
```

## Install
You might want to edit the init section to meet your needs, like **language**, **hass_url**, **hass_token** and the **actions**:
```bash
sudo apt install ffmpeg
sudo pip install -r requirements.txt
sudo cp sr.py /var/lib/asterisk/agi-bin/
sudo cp tts.py /var/lib/asterisk/agi-bin/
sudo cp hass.py /var/lib/asterisk/agi-bin/
sudo chown asterisk:asterisk /var/lib/asterisk/agi-bin/*.py
sudo chmod +x /var/lib/asterisk/agi-bin/*.py
```

## What does this help me achieve...
 - Use NLP to make conversations
 - Connect with my home assistant to control appliances
 - Keep a text transcript of a conversation.
 - Many more that I haven't thought yet...


## Insipration
This is inspired by the [asterisk-speech-recog](https://github.com/zaf/asterisk-speech-recog) project which seems to be outdated.

## Video Preview
[![IMAGE ALT TEXT HERE](https://img.youtube.com/vi/pNg3k7Uutpk/0.jpg)](https://youtu.be/pNg3k7Uutpk?t=110)

