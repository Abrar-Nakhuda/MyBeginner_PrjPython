#NumberGuessingGame

import random

lowest_num = 1
highest_num = 50
answer =  random.randint(lowest_num, highest_num)

guesses = 0
is_running = True


print("python number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("what is your Guess?: ")

    if guess.isdigit():
        guess = int(guess)
        guesses += 1

        if guess < lowest_num or guess > highest_num:
            print("invalid guess, the number is out of range")
            print(f"select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print ("Too low! Try again!")
        elif guess > answer:
            print("Too high! Try again!")
        else:
            print (f"CORRECT! The answer was {answer}")
            print(f"the number of guesses are: {guesses}")
            is_running = False

    else:
        print("invalid guess")
        print(f"select a number between {lowest_num} and {highest_num}")