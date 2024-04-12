from pymongo import MongoClient

#your mongo clinet connection string
client = MongoClient(' ')

db = client['ycq2zz']

collection = db['soccer_players_class']

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
