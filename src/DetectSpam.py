from Regex import Regex
from Boyer_Moore import boyer_moore
from KMP import KMP, countLPS

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
