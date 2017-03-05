from pyowm import OWM
import ConfigParser
import tweepy
from skills.twitter import twitter
import logging as log
from yelp.client import Client
from yelp.oauth1_authenticator import Oauth1Authenticator
import json
from google.cloud import language
import spotipy

cf=ConfigParser.ConfigParser()
cf.read('config.py')



class brain:

    def get_weather(self):
        _owm_api_key_ = cf.get('owm', 'API_KEY')
        owm = OWM(API_key=_owm_api_key_)
        obs = owm.weather_at_place('Lawrence,US') # TODO: change hardcoded location
        print obs
        w = obs.get_weather()
        print w.get_temperature('fahrenheit')
        print w.get_detailed_status()
        stats = [w.get_temperature('fahrenheit'), w.get_detailed_status()]
        return stats

    def twitter(self, words):
        _twr_ck_ = cf.get('twitter', 'consumer_key')
        _twr_cs_ = cf.get('twitter', 'consumer_secret')
        _twr_ak_ = cf.get('twitter', "access_key")
        _twr_as_ = cf.get('twitter', 'access_secret')
        auth = tweepy.OAuthHandler(_twr_ck_,_twr_cs_)
        auth.set_access_token(_twr_ak_,_twr_as_)
        api = tweepy.API(auth)
        tw = twitter(api)
        if "search" in words:
            return tw.search(words.replace('search',''))
        elif "user" in words:
            words.replace('user', '')
            words.replace('twitter','')
            log.info(words)
            return tw.user_tweets(words)

    def google_s2t_api(self, audio, sr, r):
        with open('Speech.json') as json_file:
            json_key = json.load(json_file)
        try:
                words = r.recognize_google_cloud(audio, credentials_json=json.dumps(json_key))
                return self.parse_sentence(words)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

    def sentiment_analysis(self,words):
        language_client = language.Client()
        document = language_client.document_from_text(words)
        entities = document.analyze_entities()
        for entity in entities:
            print('=' * 20)
            print('         name: %s' % (entity.name,))
            print('         type: %s' % (entity.entity_type,))
            print('wikipedia_url: %s' % (entity.wikipedia_url,))
            print('     metadata: %s' % (entity.metadata,))
            print('     salience: %s' % (entity.salience,))


    def parse_sentence(self, words):
        print words + "parse_sentence"
        if 'weather' in words:
            wstats = self.get_weather()
            return ("The temperature in fahrenheit is " + str(wstats[0]["temp"]) + " and it is going to be " + wstats[1])
        elif 'twitter'  in words or 'tweet' in words:
            print "twitter"
            return self.twitter(words)
        elif 'restaurants' in words or 'food' in words:
            print "yelp"
            return self.yelp(words)
        elif "play" in words:
            print "spotify"
            return self.spotify(words)
        else:
            print None
            return None

    def yelp(self, words):
        print "yelp"
        auth = Oauth1Authenticator(consumer_key=cf.get('yelp', 'ConsumerKey'),
                                consumer_secret=cf.get('yelp','ConsumerSecret'),
                                token=cf.get('yelp','Token'),
                                token_secret=cf.get('yelp','TokenSecret'))
        client = Client(auth)
        if 'around me' or 'near me' in words:
            print "yelp"
            params = {
            "term": "food"
            }
            response = client.search('Lawrence', **params)
        text = "Some of the restaurants are " + response.businesses[0].name + " and " + response.businesses[1].name
        print text
        return text


    def spotify (self,words):
        w = words.replace('do play ','')
        sp = spotipy.Spotify()
        results = sp.search(q='artist:' + w, type='artist')
        items = results['artists']['items']
        if len(items) > 0:
            return items[0]["images"][0]['url']
        else:
            return None
