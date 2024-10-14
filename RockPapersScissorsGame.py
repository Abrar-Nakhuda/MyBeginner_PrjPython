#RockPapersScissorsGame

import random

options = ("rock", "paper", "scissors")
running = True

while running:
    
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("enter a choice (rock, paper, scissors): ")
        print(f"Player: {player}")
        print(f"Computer: {computer}")

    if player == computer:
        print("its a tie!")
    elif player == "rock" and computer == "scissors":
        print(f"player wins! {player} beats {computer}!!")
    elif player == "paper" and computer == "rock":
        print(f"player wins! {player} beats {computer}!!")
    elif player == "scissors" and computer == "paper":
        print(f"player wins! {player} beats {computer}!!")  
    else:
        print(f"Computer wins! {computer} beats {player}")

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print ("thanks for playing!")