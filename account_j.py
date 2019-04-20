import tweepy
from tweepy import OAuthHandler

# fill in the blank using your Twitter developer account
consumer_key = 'OrumUzMkLysPhcYmCSkdOeQNu'
consumer_secret = 'KvNIGmqSVyNYtrhbGbo7tzBOIWL2Z9jTrre6WP37oRBHFLNDQ5'
access_token = '1108394113026719755-SRJpj5neQzLvs3i1B48suQOMa5G9M7'
access_secret = 'lRQMnAvv0ltSEChmmvVpoxjSVWZgoVqxgvxAe0UmHApfb'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)
 
api = tweepy.API(auth)