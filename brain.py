from pyowm import OWM
import ConfigParser

cf=ConfigParser.ConfigParser()
cf.read('config.py')
_api_key_ = cf.get('owm', 'API_KEY')

class brain:

    def get_weather():
        owm = OWM(API_key=_api_key_)
        obs = owm.weather_at_place('Lawrence,US') # TODO: change hardcoded location
        print obs
        w = obs.get_weather()
        print w.get_temperature('fahrenheit')
        print w.get_detailed_status()
        stats = [w.get_temperature('fahrenheit'), get_detailed_status()]
        return stats
