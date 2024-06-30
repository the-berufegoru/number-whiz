# This Python script is a simple number guessing game.
#!/usr/bin/python3
import random

if __name__ == '__main__':
    number_range = 100
    random_number = random.randint(1, number_range)
    guess_number = 0

    while guess_number != random_number:
        guess_number = int(input(f'Enter Number To Guess Between 1 and {number_range}: '))
        if guess_number < random_number:
            print('Ohh sorry, your guess is too low...')
        elif guess_number > random_number:
            print('Ohh sorry, your guess is too high...')

    print(f'Booyah, your guess is correct: {random_number} !!!!')
    