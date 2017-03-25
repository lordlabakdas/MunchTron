import requests
import json

class SentenceParser():
    def parse_sentence(self, words):
        print words + "parse_sentence"
        #self.sentiment_analysis(words)
        words = {"sentence":words}
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        if 'weather' in words:
            print "weather"
            #return self.get_weather()
            result = requests.get("http://localhost:5000/weather").text
            print result
            return result

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
