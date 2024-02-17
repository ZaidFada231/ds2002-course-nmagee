#!/usr/bin/python3

import os

FAV_BOOK = input('What is your favorite book? ')
BEST_FRIEND = input('What is the name of your best friend? ')
DREAM_DESTINATION = input('What is your dream travel destination? ')

os.environ["FAV_BOOK"] = FAV_BOOK
os.environ["BEST_FRIEND"] = BEST_FRIEND
os.environ["DREAM_DESTINATION"] = DREAM_DESTINATION

print("Favorite Book:", os.getenv("FAV_BOOK"))
print("Best Friend:", os.getenv("BEST_FRIEND"))
print("Dream Destination:", os.getenv("DREAM_DESTINATION"))
