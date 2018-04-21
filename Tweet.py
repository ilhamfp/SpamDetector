# Tweeter API to get tweet from user home timeline
def getTweets(keywordSearch):
    """
    param keywordSearch : keyword from a sentence
    keywordSearch type : string
    return : list of string that contains substring keywordSearch
    return type : list of string
    """
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_key, access_secret)
    api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)
    keywordSearch = keywordSearch.lower()

    #get tweet from a user's timeline
    tweets = []
    count = 0
    for eachTweet in tweepy.Cursor(api.home_timeline, tweet_mode="extended").items():
        if keywordSearch.lower() in eachTweet.full_text.lower():
            count+=1
            print(count)
            tweet = {}
            tweet["id"] = str(eachTweet.id)
            tweet["name"] = str(eachTweet.user.name)
            tweet["username"] = str(eachTweet.user.screen_name)
            tweet["text"] = str(eachTweet.full_text)
            tweet["image"] = str(eachTweet.author.profile_image_url_https)
            tweet["spam"] = False
            tweet["date"] = str(eachTweet.created_at)
            tweets.append(tweet)

        if count==30:
            break
    print(tweets)
    return tweets