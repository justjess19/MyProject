import tweepy 

consumer_key = "SHD3fTkJRjuHBTA6NEKq0bsGf"
consumer_secret = "HHOdfVXKawFmaFSJhLtPz0sanJAlrxnO9eEJIj9Xjj4wk39INZ"
access_token = "471136774-Efok12ogN1LpPHNiERO3JWnlN7bDD42YOsam6ZHy"
access_secret = "eRV8GnxhNLWQDlSRYXaXXDhj120UprBk2fpa490GL2KnH"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_secret)

api = tweepy.API(auth)

img = "cutedog.jpg"
txt = "#UMSI-206 #Proj3"

api.update_with_media(img, status = txt)
print ('No output')