
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import ConfigParser
import json
import pyttsx
import brain

br = brain.brain()

def ears():
# obtain audio from the microphone
    cf = ConfigParser.ConfigParser()
    cf.read('/home/lordlabakdas/Desktop/config.py')
    api_key = cf.get('speech', 'API_KEY')
    print api_key
    with open('Speech.json') as json_file:
        json_key = json.load(json_file)
        r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    # recognize speech using Google Speech Recognition
    try:
            words = r.recognize_google_cloud(audio, credentials_json=json.dumps(json_key))
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))

    if 'weather' in words:
        wstats = br.get_weather()
        return ("The temperature in fahrenheit is " + wstats[0] + " and it is going to be " + wstats[1])
    else:
        return None

def mouth(text):
    speech_engine = pyttsx.init('espeak') # see http://pyttsx.readthedocs.org/en/latest/engine.html#pyttsx.init
    speech_engine.setProperty('rate', 150)
    speech_engine.say(text)
    speech_engine.runAndWait()

mouth("Say Something")
mouth("I heard you say " + ears())
