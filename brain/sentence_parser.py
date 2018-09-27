import requests
import json

class SentenceParser():
    def parse_sentence(self, words):
        print words + "parse_sentence"
        #self.sentiment_analysis(words)
        words = {"sentence":words}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

        with open ('data/weather/weather.json') as json_data:
            weather_json = json.load(json_data)
        #if 'weather' in words:
        if any(x in words["sentence"].split() for x in weather_json["prefixer"]):
            print "weather"
            if any(x in words["sentence"].split() for x in weather_json["suffixer"]):
                result = requests.get("http://localhost:5000/weather")
            else:
                result = requests.post("http://localhost:5000/weather", data=json.dumps(words), headers=headers)
            print result.text
            return result.text

        elif 'twitter'  in words or 'tweet' in words:
            print "twitter"
            result = requests.post ("http://localhost:5000/twitter", data=json.dumps(words), headers=headers)
            return result.text

        elif 'restaurants' in words or 'food' in words:
            print "yelp"
            result = requests.post ("http://localhost:5000/yelp", data=json.dumps(words), headers=headers)
            return result.text


        elif "play" in words:
            print "spotify"
            result = requests.post ("http://localhost:5000/spotify", data=json.dumps(words), headers=headers)
            return result.text
        else:
            print None
            return None
