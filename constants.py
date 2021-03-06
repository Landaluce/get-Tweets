TWEETS_DIRECTORY = "Tweets"  # Directory where all tweets will be saved
USERINFO_DIRECTORY = "Users"  # Directory where all followers will be saved
TWEETS_PER_QUERY = 500  # 500 is the max the API permits
LIMIT_EXCEEDED_ERROR_CODE = 88

# If results from a specific ID onwards are required, set SINCE_ID to that ID,
SINCE_ID = None  # else default to no lower limit, go as far back as API allows
