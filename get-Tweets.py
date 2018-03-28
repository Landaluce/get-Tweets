import tweepy
from api import api
from constants import *
import json
import os


def search_tweets(search_query, number_tweets=15, geocode=None, lang=None):
    """Gets a list of tweets.

    https://developer.twitter.com/en/docs/tweets/search/api-reference/get-search-tweets
    :param search_query: search query used to find tweets (String)
    :param number_tweets: number of tweets to get (Integer)
    :param lang: Restricts tweets to the given language, given by an ISO 639-1 code. Language detection is best-effort.
    :param geocode: Returns tweets by users located within a given radius of the given latitude/longitude.
    :return: List of tweet objects
    """
    max_id = 0  # If results only below a specific ID are, set max_id to that ID, else default to no upper limit
    tweets = []
    while len(tweets) < number_tweets:
        try:
            if max_id <= 0:
                if not SINCE_ID:
                    new_tweets = api.search(q=search_query,
                                            count=TWEETS_PER_QUERY,
                                            geocode=geocode,
                                            lang=lang,
                                            tweet_mode="extended")
                else:
                    new_tweets = api.search(q=search_query,
                                            count=TWEETS_PER_QUERY,
                                            geocode=geocode,
                                            lang=lang,
                                            tweet_mode="extended",
                                            since_id=SINCE_ID)
            else:
                if not SINCE_ID:
                    new_tweets = api.search(q=search_query,
                                            count=TWEETS_PER_QUERY,
                                            geocode=geocode,
                                            lang=lang,
                                            tweet_mode="extended",
                                            max_id=str(max_id - 1))
                else:
                    new_tweets = api.search(q=search_query,
                                            count=TWEETS_PER_QUERY,
                                            geocode=geocode,
                                            lang=lang,
                                            tweet_mode="extended",
                                            max_id=str(max_id - 1),
                                            since_id=SINCE_ID)
            if not new_tweets or len(new_tweets) == 0:
                print("No more tweets found")
                break
            else:
                for tweet in new_tweets:
                    tweets.append(tweet)
                max_id = new_tweets[-1].id
        except tweepy.TweepError as error:
            to_json = json.loads(error.reason.replace("[", "").replace("]", "").replace("'", "\""))
            print(to_json["message"])
            break
    "%s_search lat:%f long:%f r:%d%s"
    options = (search_query,)
    folder_name_format = '%s_search'
    if lang:
        options += (lang,)
        folder_name_format += ' lang:%s'
    if geocode:
        options += (geocode,)
        folder_name_format += ' geocode:%s'
    print(folder_name_format % options)
    save_tweets(folder_name_format % options, tweets[:number_tweets])
    return tweets[:number_tweets]


def get_timeline_tweets(screen_name, number_tweets=15, include_rts=True):
    """Gets a list of tweets.

    https://developer.twitter.com/en/docs/tweets/timelines/overview
    :param screen_name: The screen name of the user for whom to return results (String)
    :param number_tweets: number of tweets to get (Integer)
    :param include_rts: When set to false , the timeline will strip any native retweets
    (though they will still count toward both the maximal length of the timeline and the
    slice selected by the count parameter)
    :return: List of tweet objects
    """
    max_id = 0  # If results only below a specific ID are, set max_id to that ID, else default to no upper limit
    tweets = []
    while len(tweets) < number_tweets:
        try:
            if max_id <= 0:
                if not SINCE_ID:
                    new_tweets = api.user_timeline(screen_name=screen_name,
                                                   count=TWEETS_PER_QUERY,
                                                   include_rts=include_rts,
                                                   tweet_mode="extended")
                else:
                    new_tweets = api.user_timeline(screen_name=screen_name,
                                                   count=TWEETS_PER_QUERY,
                                                   include_rts=include_rts,
                                                   tweet_mode="extended",
                                                   since_id=SINCE_ID)
            else:
                if not SINCE_ID:
                    new_tweets = api.user_timeline(screen_name=screen_name,
                                                   count=TWEETS_PER_QUERY,
                                                   include_rts=include_rts,
                                                   tweet_mode="extended",
                                                   max_id=str(max_id - 1))
                else:
                    new_tweets = api.user_timeline(screen_name=screen_name,
                                                   count=TWEETS_PER_QUERY,
                                                   include_rts=include_rts,
                                                   tweet_mode="extended",
                                                   max_id=str(max_id - 1),
                                                   since_id=SINCE_ID)
            if not new_tweets or len(new_tweets) == 0:
                print("No more tweets found")
                break
            else:
                for tweet in new_tweets:
                    tweets.append(tweet)
                max_id = new_tweets[-1].id
        except tweepy.TweepError as error:
            try:
                tojson = json.loads(error.reason.replace("[", "").replace("]", "").replace("'", "\""))
                print(tojson["message"])
            except:
                print("Username not found")
            break
    save_tweets(screen_name + '_timeline', tweets[:number_tweets])
    return tweets[:number_tweets]


def save_tweets(folder_name, tweets):
    if len(tweets) > 0:
        folder_path = os.path.join(TWEETS_DIRECTORY, folder_name)
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        for tweet in tweets:
            file_name = str(tweet.created_at) + ' ' + str(tweet.id) + ".txt"
            # : from the timestamp will cause problems in filenames on Windows.
            file_name = file_name.replace(':', '-')
            file_path = os.path.join(folder_path, file_name)
            if not os.path.isfile(file_path):
                file = open(file_path, "w", encoding="UTF-8")
                file.write(tweet.full_text)
                file.close()


def menu():
    answer = ""
    while answer != "3":
        print("\t1. Pull tweets from timeline")
        print("\t2. Search tweets")
        print("\t3. Exit")
        answer = input("\tWhat would you like to do? ")
        if answer == "1":
            screen_name = input("Username: ")
            number_tweets = int(input("Number of tweets: "))
            tweets = get_timeline_tweets(screen_name=screen_name,
                                         number_tweets=number_tweets)
            if len(tweets) > 0:
                print(len(tweets), "tweets saved in", screen_name + "_timeline")
        elif answer == "2":
            search_query = input("Search query: ")
            number_tweets = int(input("Number of tweets: "))
            tweets = search_tweets(search_query=search_query,
                                   number_tweets=number_tweets)
            if len(tweets) > 0:
                print(len(tweets), "tweets saved in", search_query + "_search")
        elif answer != "3":
            print("Invalid choice, try again")


menu()

# Geocode filter
"""
search_query = "Wheaton"
number_tweets = 10
# Wheaton's lat & long Check: https://www.mapdevelopers.com/geocode_tool.php
latitude = 41.96801
longitude = -71.185194
radius = 1
units = "mi"  # mi or km
tweets = search_tweets(search_query=search_query,
                       number_tweets=number_tweets,
                       geocode="%f,%f,%d%s" % (latitude, longitude, radius, units))
"""

# Language filter
"""
search_query = "Wheaton"
number_tweets = 10
language = "es"  # given in ISO 639-1 code, check: https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes
tweets = search_tweets(search_query=search_query,
                       number_tweets=number_tweets,
                       lang=language)
"""
