from flask import Flask, request
import json
import tweepy

app = Flask(__name__)

def getTweet(keywordSearch):
    tweets = []
    for x in range(30):
        tweet = {}
        tweet["id"] = "Id"+str(x)
        tweet["name"] = "Name"+str(x)
        tweet["username"] = "Username"+str(x)
        tweet["text"] = "Text"+str(x)
        tweet["image"] = "https://avatars2.githubusercontent.com/u/31740013?s=460&v=4"
        tweet["spam"] = False
        tweet["date"] = str(x) + " Januari 2018"
        tweets.append(tweet)
    print(tweets)
    return tweets

def getVerdict(tweets, algorithm, keywordSpam, exact):
    for i in range(len(tweets)):
        if algorithm == 0:
            tweets[i]["spam"] = True
        elif algorithm == 1:
            tweets[i]["spam"] = True
        elif algorithm == 2:
            tweets[i]["spam"] = True

@app.route('/', methods=['POST'])
def hello_world():
    body = dict(request.form)
    print(body)

    keywordSpam = body["keywordSpam"][0].split(",")
    algorithm = int(body["algorithm"][0])
    keywordSearch = body["keywordSearch"][0]

    tweetHasil = getTweet(keywordSearch)
    
    getVerdict(tweetHasil, algorithm, keywordSpam, True)
    return json.dumps({'hasil':tweetHasil})

if __name__ == '__main__':
    app.run(debug = True)