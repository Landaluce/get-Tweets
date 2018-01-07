import tweepy
consumer_key = 'RLBnivPChhdTjB9s2lL1M88Po'
consumer_secret = 'UFXipb6TJb9H9vGolaZoxQczRbPfsy5QafwYSlK80ypAJvfmYx'
access_token = '850748910930972672-wTQ7Gm0zUhrhipOm49N4gpWW6CXwZer'
access_token_secret = 'Tnj3vU8kc51rti8kfZRRvphfs7vDD6dfbDcYLYpnEv8uP'
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)
