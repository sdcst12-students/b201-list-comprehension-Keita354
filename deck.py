#!python3
import random

ranks = ['A','2','3','4','5','6','7','8','9','T','J','Q','K']
suits = ['C','D','H','S']

deck = [f"{rank}{suit}" for rank in ranks for suit in suits]

def shuffle(deck):
    random.shuffle(deck)
#add hashtag infront to remove shuffling function below.
shuffle(deck)

print(deck[:5])