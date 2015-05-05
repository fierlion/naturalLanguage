import nltk
from nltk.corpus import webtext
from nltk.corpus import nps_chat

print('WEBTEXT___')
for fileid in webtext.fileids():
    print(fileid, webtext.raw(fileid)[:20])

print('NPS_CHAT___')
for post in nps_chat.posts():
    print(post)
