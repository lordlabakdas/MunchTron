
# NOTE: this example requires PyAudio because it uses the Microphone class

import speech_recognition as sr
import ConfigParser
import json

cf = ConfigParser.ConfigParser()
cf.read('/home/lordlabakdas/Desktop/config.py')
api_key=cf.get('speech', 'API_KEY')
print api_key
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)
with open ('Speech.json') as json_file:
    json_key = json.load(json_file)
# recognize speech using Google Speech Recognition
try:
    print("Google Speech Recognition thinks you said " + r.recognize_google_cloud(audio, credentials_json=json.dumps(json_key)))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
