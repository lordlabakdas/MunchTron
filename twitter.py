import tweepy
class twitter (object):
    def __init__(self,api):
        self.api = api

    def read_user_tweets(self,user,count):
        tweets = self.api.user_timeline(screen_name = user, count = count, include_rts = True)

    def search(self,words):
        max_tweets = 2
        searched_tweets = [status for status in tweepy.Cursor(self.api.search, q=words).items(max_tweets)]
        for status in searched_tweets:
            print status
