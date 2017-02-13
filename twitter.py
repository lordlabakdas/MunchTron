class twitter (object):
    def __init__(self,api):
        self.api = api

    def read_user_tweets(self,user,count):
        tweets = self.api.user_timeline(screen_name = user, count = count, include_rts = True)
