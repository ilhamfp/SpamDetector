from flask import Flask, request
import json
import tweepy
import re

app = Flask(__name__)

consumer_key = "uRmhYow4fOoI1C6NrHd2hTRyE"  
consumer_secret = "YGTUR6sQyijpP8Vu5dhNIAEJTt88wJaklEdWtqxl1AYUUCwKJl"  
access_key = "908013362801401856-ZZMgepM0JVWpeNYRnuN9P0tTetXymOE"  
access_secret = "eyOgN7WB6Gtxwl2u8mqZ1XlhvboG2lddl4rBY8mUmlCJQ"

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

        if count==21:
            break
    print(tweets)
    return tweets

def getVerdict(tweets, algorithm, keywordSpam):
    """
    param tweets : list of tweet to scan
    tweet type : list of string
    param algorithm : KMP if 0, boyerr_moore if 1, regex either 
    algorithm type : int
    param keywordSpam : spam words
    keywordSpam  type : list of string
    """
    for i in range(len(tweets)):
        if algorithm == 0:
            tweets[i]["spam"] = KMP(tweets[i]["text"].lower(), keywordSpam)
        elif algorithm == 1:
            tweets[i]["spam"] = boyer_moore(tweets[i]["text"].lower(), keywordSpam)
        elif algorithm == 2:
            tweets[i]["spam"] = Regex(tweets[i]["text"].lower(), keywordSpam)

@app.route('/', methods=['POST'])
def hello_world():
    """
    main program 
    """
    body = dict(request.form)
    print(body)

    keywordSpam = body["keywordSpam"][0].split(",")
    algorithm = int(body["algorithm"][0])
    keywordSearch = body["keywordSearch"][0]

    tweetHasil = getTweets(keywordSearch) # getting tweets
    
    getVerdict(tweetHasil, algorithm, keywordSpam) # decide wether a tweet is spam or not
    return json.dumps({'hasil':tweetHasil})


### KMP Algorithm ###

# Finding LPS
def countLPS(pattern):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, false either
    return type : boolean
    """
    # finding the LPS from string pattern
    lps = [0]
    
    for i in range(1, len(pattern)):
        j = lps[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[j] == pattern[i]: lps.append(j+1)
        else: lps.append(j)
    
    return lps
        
# KMP implementation        
def KMP(text, patternList):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, false either
    return type : boolean
    """
    # find the initial index where the pattern found in text using KMP algorithm
    kmp = []
    for pattern in patternList:
        pattern = pattern.lower()
        j = 0
        lps = countLPS(pattern)
        for i in range(len(text)):
            while j > 0 and text[i] != pattern[j]:
                j = lps[j - 1]
            if text[i] == pattern[j]: 
                j += 1
            if j == len(pattern):  # found the pattern
                 kmp.append(i-j+1)
                 j = lps[j-1]
                
    return len(kmp) > 0

### Boyer-Moore algorithm ###
def boyer_moore(text, patternList):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, false either
    return type : boolean
    """
    for pattern in patternList:
        pattern = pattern.lower()
        i = 0
        j = 0
        while (i + j) < len(text):
            j = len(pattern) - 1
            while j >= 0:
                if text[i + j] != pattern[j]:
                    closest_occurence = pattern.rfind(text[i + j])
                    if closest_occurence == -1:
                        j = len(pattern) - 1
                        i += j + 1
                        break
                    elif closest_occurence >= j:
                        i += 1
                        j = len(pattern) - 1
                        break
                    else:
                        shift = j - closest_occurence
                        i += shift
                        j = len(pattern) -1
                        break
                j -= 1
            if j <= -1:
                return True

    return False

# regex algorithm to find string
def Regex(text, patternList):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, either false
    return type : boolean
    """
    ret = []
    for pattern in patternList:
        pattern = pattern.split(' ')
        tmp = [-1]
        for pat in pattern:
            matches = re.finditer(pat.lower(), text);
            for match in matches:
                if match.start() < tmp[len(tmp)-1]:
                    break
                tmp.append(match.start())
                break;
        if len(tmp) != len(pattern)+1:
            break
        else:
            ret.append(tmp[0])
    
    return len(ret) > 0

if __name__ == '__main__':
    app.run(debug = True)