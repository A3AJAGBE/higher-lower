"""
A game application that compares two social media following. The user has to guess which account is higher or lower
"""

# Imports
import os
from data import data
from logo import logo, versus
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
        # Default displays
        print(f'Current score: {score}\n')
        print('Which social media account has more followers?')

        # selecting the accounts
        second_acc = random.choice(data)

        if first_acc == second_acc:
            second_acc = random.choice(data)
        else:
            print(f"{first_acc['name']}, a {first_acc['description']}, from {first_acc['country']}")
            print(versus)
            print(f"{second_acc['name']}, a {second_acc['description']}, from {second_acc['country']}")

        # User guess
        guess = input('Is it "A" or "B"? ').upper()
        clear()
        print(logo)

        # Get the account followers
        A = first_acc["follower_count"]
        B = second_acc["follower_count"]

        # Compare followers
        if guess == 'A' and A > B:
            print(f'Correct, {first_acc["name"]} has more followers.')
            score += 1
            # Replace the correct guess has the first account
            guess_data = first_acc
            first_acc = guess_data
        elif guess == 'A' and B > A:
            print(f'Wrong, {second_acc["name"]} has more followers.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        elif guess == 'B' and A < B:
            print(f'Correct, {second_acc["name"]} has more followers.')
            score += 1
            # Replace the correct guess has the first account
            guess_data = second_acc
            first_acc = guess_data
        elif guess == 'B' and A > B:
            print(f'Wrong, {first_acc["name"]} has more followers.')
            print(f'\nFinal score: {score}\n')
            game_over = True
        else:
            print('Invalid guess. Restarting the game...')
            score = 0


game()
