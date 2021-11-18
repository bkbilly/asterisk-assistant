# Asterisk Speech Recognition
This is inspired by the [asterisk-speech-recog](https://github.com/zaf/asterisk-speech-recog) project which seems to be outdated.
With this script the Asterisk PBX can recognize a person speaking using speach recognition and play back at him the message using Google TTS.
I've created this to help anyone who wants to add AGI functionality to their Asterisk server using speach recognition.

## Install
```bash
sudo pip install -r requirements.txt
sudo cp speech-recognition.py /var/lib/asterisk/agi-bin/speech-recognition.py
sudo chown asterisk:asterisk /var/lib/asterisk/agi-bin/speech-recognition.py
sudo chmod +x /var/lib/asterisk/agi-bin/speech-recognition.py
```

## Example of `extensions.conf`
```
exten => 45,1,Answer()
exten => 45,n,agi(speech-recognition.py)
exten => 45,n,Verbose(1,The text you just said is: ${recognition})
```

## What does this help me achieve...
 - Use NLP to make conversations
 - Connect with my home assistant to control appliances
 - Keep a text transcript of a conversation.
 - Many more that I haven't thought yet...
