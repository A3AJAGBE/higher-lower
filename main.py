"""
A game application that compares two social media following. The user has to guess which account is higher or lower
"""

# Imports
import os
from data import data
from logo import logo
import random


def clear():
    """This function clears the console"""
    os.system('clear')


def game():
    print(logo)
    # Initial game score
    score = 0
    first_acc = random.choice(data)

    game_over = False
    while not game_over:
        # Display number of correct guess
        print(f'Current score: {score}\n')

        # selecting the accounts
        second_acc = random.choice(data)

        if first_acc == second_acc:
            second_acc = random.choice(data)
        else:
            print(f"A: {first_acc['name']}, a {first_acc['description']}, from {first_acc['country']}")

            print(f"B: {second_acc['name']}, a {second_acc['description']}, from {second_acc['country']}")

        A = first_acc["follower_count"]
        B = second_acc["follower_count"]

        # Testing, will be removed
        print(A)
        print(B)

        # User guess
        guess = input('Who has more followers? "A" or "B"\n').upper()
        clear()
        print(logo)

        # Compare followers
        if guess == 'A' and A > B:
            print('Correct, A is the answer.')
            score += 1
            # Replace the correct guess has the first account
            guess_data = first_acc
            first_acc = guess_data
        elif guess == 'A' and B > A:
            print('Wrong, B is the answer.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        elif guess == 'B' and A < B:
            print('Correct, B is the answer.')
            score += 1
            # Replace the correct guess has the first account
            guess_data = second_acc
            first_acc = guess_data
        elif guess == 'B' and A > B:
            print('Wrong, A is the answer.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        else:
            print('Invalid guess.')
            print(f'\nFinal score: {score}\n')
            game_over = True


game()
