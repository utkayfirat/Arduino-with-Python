import time
import speech_recognition as sr
from voice_command import VoiceCommand

r = sr.Recognizer()

while True:
    with sr.Microphone() as source:
        print("I can hear you!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio, language='en-EN')
        print(data)
        vc = VoiceCommand(data)
        vc.findVoiceCommand()
        time.sleep(1)
    except sr.UnknownValueError:
        print("ERROR")

