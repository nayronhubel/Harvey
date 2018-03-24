import pymongo
from pymongo import MongoClient
import spacy

nlp = spacy.load('pt')
client = MongoClient('mongodb://localhost:27017/Harvey')
db = client['Harvey']
collection = db['FAQ']
res = collection.find();

for pageView in res :
    print("1")
    doc = nlp(pageView["question"])
    print([(w.text, w.pos_) for w in doc])