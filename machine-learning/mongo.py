import re
import spacy
import pymongo
from pymongo import MongoClient


def insert(artigo, title) :
    client = MongoClient('mongodb://localhost:27017/Harvey')
    db = client['Harvey']
    collection = db['Artigos']
    res = collection.insert({"artigo" : artigo,"title" : title } );

#nlp = spacy.load('pt_core_news_sm')
#client = MongoClient('mongodb://localhost:27017/Harvey')
#db = client['Harvey']
#collection = db['FAQ']
#res = collection.find({})

#for pageView in res :
#    print("1")
#    doc = nlp(pageView["question"])
#    aiml = '*'
#    for w in doc:
#        if ((w.pos_ == 'VERB') or (w.pos_ == 'NOUN')):
#            aiml = aiml + ' ' + w.text + ' '
#            #print(w.text)
#            #print("*\n" + w.text)
#        elif (not(aiml[-1:] == '*')):
#            aiml = aiml + '*'
#    print (re.sub(u'  ' , ' ', aiml))

