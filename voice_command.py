import time
import urllib.request
import json
from gtts import gTTS
from playsound import playsound
import os
import sys
from random import choice
import requests
from lxml import html
from ar_command import ArCommand

class VoiceCommand():
    def __init__(self,inComingVoice):
        self.voice = inComingVoice.upper()
        self.voice_block = self.voice
        self.commands = ['HOW ARE YOU', 'CLOSE APPLICATION', 'TURN ON LIGHT', 'TURN OFF LIGHT']

    def findVoiceCommand(self):
        for VoiceCommand in self.commands:
            if VoiceCommand in self.voice_block:
                self.runCommand(VoiceCommand)

    def runCommand(self, VoiceCommand):
        ac = ArCommand()
        if VoiceCommand == "HOW ARE YOU":
            self.talkingFunc('Im fine, how are you?')
        if VoiceCommand == 'TURN ON LIGHT':
            self.talkingFunc('LED turns on.')
            ac.openLed()
        if VoiceCommand == 'TURN OFF LIGHT':
            self.talkingFunc('LED turns off.')
            ac.closeLed()
        if VoiceCommand == 'CLOSE APPLICATION':
            self.closeFunc()


    def talkingFunc(self, inComingText):
        tts = gTTS(text=inComingText, lang='en')
        tts.save("ses.mp3")
        playsound("ses.mp3")
        os.remove("ses.mp3")
        print(inComingText)


    def closeFunc(self):
        self.talkingFunc("System shuts down")
        sys.exit()


    def talkFunc(self):
        stype = ["I\'m fine, how are you ?", "I\'m fine, how about you ?"]
        choosing = choice(stype)


