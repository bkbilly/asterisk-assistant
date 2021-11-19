# Asterisk Speech Recognition
This is inspired by the [asterisk-speech-recog](https://github.com/zaf/asterisk-speech-recog) project which seems to be outdated.
With this script the Asterisk PBX can recognize a person speaking using speach recognition and play back at him the message using Google TTS.
I've created this to help anyone who wants to add AGI functionality to their Asterisk server using speach recognition.

## Install
```bash
sudo pip install -r requirements.txt
sudo cp sr.py /var/lib/asterisk/agi-bin/
sudo cp tts.py /var/lib/asterisk/agi-bin/
sudo cp hass.py /var/lib/asterisk/agi-bin/
sudo chown asterisk:asterisk /var/lib/asterisk/agi-bin/*.py
sudo chmod +x /var/lib/asterisk/agi-bin/*.py
```

## Example of `extensions.conf`
```
exten => 45,1,Answer()
exten => 45,n,agi(sr.py)
exten => 45,n,agi(tts.py,${recognition})
exten => 45,n,agi(hass.py,${recognition})
exten => 45,n,agi(tts.py,${hass_result})
exten => 45,n,Hangup()
```

## What does this help me achieve...
 - Use NLP to make conversations
 - Connect with my home assistant to control appliances
 - Keep a text transcript of a conversation.
 - Many more that I haven't thought yet...
