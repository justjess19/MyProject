print ("No output necessary but can print success/failure if wanted")

import tweepy
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
from textblob import TextBlob 

consumer_key = "SHD3fTkJRjuHBTA6NEKq0bsGf"
consumer_secret = "HHOdfVXKawFmaFSJhLtPz0sanJAlrxnO9eEJIj9Xjj4wk39INZ"
access_token = "471136774-Efok12ogN1LpPHNiERO3JWnlN7bDD42YOsam6ZHy"
access_secret = "eRV8GnxhNLWQDlSRYXaXXDhj120UprBk2fpa490GL2KnH"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

api = tweepy.API(auth)

search_term = input('Input a term: ')
for tweets in tweepy.Cursor(api.search, q=search_term, result_type = "recent", include_entities= True, land ="en", count = 100).items(100):
    print (tweets.text)

analysis = TextBlob(tweets.text)
print (analysis.sentiment)
sub = analysis.sentiment.subjectivity
pol = analysis.sentiment.polarity
print ('The average subjectivity is: ', sub)
print ('The avergae polarity is: ', pol)


