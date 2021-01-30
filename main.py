"""
A game application that compares two social media following. The user has to guess which account is higher or lower
"""

# Imports
from data import data
import random


def game():

    # selecting the accounts
    compare = random.choice(data)
    name = compare['name']
    desc = compare['description']
    country = compare['country']
    print(f"A: {name}, a {desc}, from {country}")

    against = random.choice(data)
    if against == compare:
        against = random.choice(data)
    name = against['name']
    desc = against['description']
    country = against['country']
    print(f"B: {name}, a {desc}, from {country}")


game()
