from pyowm import OWM
import ConfigParser
import tweepy
import twitter
import logging as log

cf=ConfigParser.ConfigParser()
cf.read('config.py')
_owm_api_key_ = cf.get('owm', 'API_KEY')

_twr_ck_ = cf.get('twitter', 'consumer_key')
_twr_cs_ = cf.get('twitter', 'consumer_secret')
_twr_ak_ = cf.get('twitter', "access_key")
_twr_as_ = cf.get('twitter', 'access_secret')

class brain:

    def get_weather(self):
        owm = OWM(API_key=_owm_api_key_)
        obs = owm.weather_at_place('Lawrence,US') # TODO: change hardcoded location
        print obs
        w = obs.get_weather()
        print w.get_temperature('fahrenheit')
        print w.get_detailed_status()
        stats = [w.get_temperature('fahrenheit'), w.get_detailed_status()]
        return stats

    def twitter(self, words):
        auth = tweepy.OAuthHandler(_twr_ck_,_twr_cs_)
        auth.set_access_token(_twr_ak_,_twr_as_)
        api = tweepy.API(auth)
        tw = twitter.twitter(api)
        if "search" in words:
            return tw.search(words.replace('search',''))
        elif "user" in words:
            words.replace('user', '')
            words.replace('twitter','')
            log.info(words)
            return tw.user_tweets(words)

    def google_s2t_api(audio):
        with open('Speech.json') as json_file:
            json_key = json.load(json_file)
        try:
                words = r.recognize_google_cloud(audio, credentials_json=json.dumps(json_key))
                return parse_sentence(words)
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))

    def parse_sentence(words):
        if 'weather' in words:
            wstats = br.get_weather()
            return ("The temperature in fahrenheit is " + str(wstats[0]["temp"]) + " and it is going to be " + wstats[1])
        elif 'twitter'  or 'tweet' in words:
            return br.twitter(words)
        else:
            print None
            return None
