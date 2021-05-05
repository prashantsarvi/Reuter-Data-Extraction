import re

from pymongo import MongoClient
from pymongo.collection import Collection
from tweepy import OAuthHandler

myclient = MongoClient("mongodb+srv://TwitterDB:twitterextraction@twittercluster.udioj.mongodb.net/test")
db = myclient["ReuterDb"]
Collection = db["Reuters"]


authentication = OAuthHandler("rfQqCDztquIOPK0yKDB30SBEa", "fPHxHfJR9QMeVaK5pm9k1poyLWWJzbARXmjkwwm5kwgwdDfJPE")
authentication.set_access_token("1322905249078652928-ijzNu28JIYUkQsc3sDzN5bAJnDqfRa",
                                "5zo03NCBjUYGEMuQPmle0juHQb1FEEJs0Sv7uEJdQFfEf")
sgmFile = open('reut2-014.sgm', 'r')
sgmRead = sgmFile.read()
sgmFile2 = open('reut2-009.sgm', 'r')
sgmRead2 = sgmFile2.read()

listRead = []

x = re.findall('<REUTERS(.*?)<\/REUTERS>', sgmRead, re.DOTALL)
y = re.findall('<REUTERS(.*?)<\/REUTERS>', sgmRead2, re.DOTALL)
listSgm = []
for i in x:
    titleSgm = re.findall('<TITLE>(.*?)</TITLE>', i, re.DOTALL)
    text = re.findall('<BODY>(.*?)</BODY>', i, re.DOTALL)
    article = {}
    if len(titleSgm) > 0:
        article['titleSgm'] = titleSgm[0]
    if len(text) > 0:
        article['text'] = text[0]
    listSgm.append(article)
for i in y:
    titleSgm = re.findall('<TITLE>(.*?)</TITLE>', i, re.DOTALL)
    text = re.findall('<BODY>(.*?)</BODY>', i, re.DOTALL)
    article = {}
    if len(titleSgm) > 0:
        article['titleSgm'] = titleSgm[0]
    if len(text) > 0:
        article['text'] = text[0]
    listSgm.append(article)
Collection.insert_many(listSgm)
