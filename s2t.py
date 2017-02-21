
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import ConfigParser
import json
import pyttsx
import brain

br = brain.brain()


def ears():
# obtain audio from the microphone
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        return br.google_s2t_api(audio)

def mouth(text):
    speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
    speech_engine.setProperty('rate', 150)
    speech_engine.say(text)
    speech_engine.runAndWait()

if __name__ == "__main__":
    mouth("Say Something")
    mouth(ears())
