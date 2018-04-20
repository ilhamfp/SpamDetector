from flask import Flask, request
import json
import tweepy

app = Flask(__name__)

def getTweet(username):
    clean_tweets = []
    for x in range(5):
        clean_tweet = {}
        clean_tweet["id"] = "Id"+str(x)
        clean_tweet["name"] = "Name"+str(x)
        clean_tweet["username"] = "Username"+str(x)
        clean_tweet["text"] = "Text"+str(x)
        clean_tweet["image"] = "https://avatars2.githubusercontent.com/u/31740013?s=460&v=4"
        clean_tweet["spam"] = False
        tanggal = "01 31"
        # seharusnya kaya gini nanti
        # tanggal = str(tweet.created_at)[5:10]
        clean_tweet["date"] = generate_date_string(tanggal)
        clean_tweets.append(clean_tweet)
    print(clean_tweets)
    return clean_tweets

def generate_date_string(s):
    month = s[:2]
    date = s[-2:]

    month_s = ""

    if month == "01":
        month_s = "Jan"
    elif month == "02":
        month_s = "Feb"
    elif month == "03":
        month_s = "Mar"
    elif month == "04":
        month_s = "Apr"
    elif month == "05":
        month_s = "May"
    elif month == "06":
        month_s = "Jun"
    elif month == "07":
        month_s = "Jul"
    elif month == "08":
        month_s = "Aug"
    elif month == "09":
        month_s = "Sep"
    elif month == "10":
        month_s = "Oct"
    elif month == "11":
        month_s = "Nov"
    elif month == "12":
        month_s = "Dec"

    return month_s + ' ' + date


def getVerdict(clean_tweets, algorithm, keywords, exact):
    for i in range(len(clean_tweets)):
        if algorithm == 0:
            clean_tweets[i]["spam"] = True
        elif algorithm == 1:
            clean_tweets[i]["spam"] = True
        elif algorithm == 2:
            clean_tweets[i]["spam"] = True

@app.route('/', methods=['POST'])
def hello_world():
    body = dict(request.form)
    print(body)

    keywords = body["keywords"][0].split(",")
    algorithm = int(body["algorithm"][0])
    username = body["username"][0].split('@')[-1]
    clean_tweets = getTweet(username)
    
    getVerdict(clean_tweets, algorithm, keywords, True)
    return json.dumps({'data':clean_tweets})

if __name__ == '__main__':
    app.run(debug = True)