import pymongo
from pymongo import MongoClient


def insert(artigo, title) :
    client = MongoClient('mongodb://localhost:27017/Harvey')
    db = client['Harvey']
    collection = db['Artigos']
    res = collection.insert({"artigo" : artigo,"title" : title } );