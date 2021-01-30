"""
A game application that compares two social media following. The user has to guess which account is higher or lower
"""

# Imports
from data import data
import random


def game():
    # Initial game score
    score = 0

    game_over = False
    while not game_over:

        # Display number of correct guess
        print(f'\nCurrent score: {score}\n')

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

        A = compare["follower_count"]
        B = against["follower_count"]

        # Testing, will be removed
        print(A)
        print(B)

        # User guess
        guess = input('Who has more followers? "A" or "B"\n').upper()

        # Compare followers
        if guess == 'A' and A > B:
            print('Correct, A is the answer.')
            score += 1
        elif guess == 'A' and B > A:
            print('Wrong, B is the answer.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        elif guess == 'B' and A < B:
            print('Correct, B is the answer.')
            score += 1
        elif guess == 'B' and A > B:
            print('Wrong, A is the answer.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        else:
            print('Invalid guess.')
            print(f'\nFinal score: {score}\n')
            game_over = True


game()
