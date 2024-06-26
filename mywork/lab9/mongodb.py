import os
from pymongo import MongoClient

def main():
    MONGOPASS = os.getenv("MONGOPASS")
    uri = "mongodb+srv://cluster0.pnxzwgz.mongodb.net/"
    client = MongoClient(
        uri,
        username="nmagee",
        password=MONGOPASS,
        connectTimeoutMS=200,
        retryWrites=True,
    )

    db = client["ycq2zz"]
    collection = db["soccer_players_class"]

    players = [
        {"name": "Cristiano Ronaldo", "position": "Forward", "teams": ["Sporting CP", "Manchester United", "Real Madrid", "Juventus"]},
        {"name": "Lionel Messi", "position": "Forward", "teams": ["FC Barcelona", "Paris Saint-Germain"]},
        {"name": "Neymar", "position": "Forward", "teams": ["Santos", "FC Barcelona", "Paris Saint-Germain"]},
        {"name": "Virgil van Dijk", "position": "Defender", "teams": ["Groningen", "Celtic", "Southampton", "Liverpool"]},
        {"name": "Kevin De Bruyne", "position": "Midfielder", "teams": ["Genk", "Chelsea", "Werder Bremen", "VfL Wolfsburg", "Manchester City"]}
    ]

    collection.insert_many(players)

    result = collection.find().limit(3)

    for doc in result:
        print(doc)
