from flask import Flask, request
import json
import tweepy
import re
from Regex import Regex
from Boyer_Moore import boyer_moore
from KMP import KMP, countLPS
from DetectSpam import getVerdict
from Tweet import getTweets

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug = True)