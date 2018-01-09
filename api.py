import tweepy
consumer_key = 'tKOCwOilXvs35mhLrpHYu0Z4j'
consumer_secret = 'swajXhEbtkanBqTiGAPkgRbCy5zodG1uH3f21Ku5XIIIt16lit'
access_token = '311545238-uGQzvuJgUAgsELpqGesRoE0EoZJGlqI8PjoU3nBo'
access_token_secret = 'iw1UQ693AKZdvsjZ7lVa8704NWEj7FYlBGklK6TYjRX0C'
authentication = tweepy.OAuthHandler(consumer_key, consumer_secret)
authentication.set_access_token(access_token, access_token_secret)
api = tweepy.API(authentication)
