import requests
import json

class SentenceParser():
    def parse_sentence(self, words):
        print words + "parse_sentence"
        #self.sentiment_analysis(words)
        if 'weather' in words:
            print "weather"
            #return self.get_weather()
            result = requests.get("http://localhost:5000/weather").text
            print result
            return result

        elif 'twitter'  in words or 'tweet' in words:
            print "twitter"
            words = {"sentence":words}
            headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
            result = requests.post ("http://localhost:5000/twitter", data=json.dumps(words), headers=headers)
            return result.text

        elif 'restaurants' in words or 'food' in words:
            print "yelp"
            return self.yelp(words)

        elif "play" in words:
            print "spotify"
            return self.spotify(words)
        else:
            print None
            return None
