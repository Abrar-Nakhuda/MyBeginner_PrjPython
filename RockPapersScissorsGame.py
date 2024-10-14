#RockPapersScissorsGame

import random

options = ("rock", "paper", "scissors")
running = True
player_score = 0
computer_score = 0

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
        player_score += 1
    elif player == "paper" and computer == "rock":
        print(f"player wins! {player} beats {computer}!!")
        player_score += 1
    elif player == "scissors" and computer == "paper":
        print(f"player wins! {player} beats {computer}!!")
        player_score += 1  
    else:
        print(f"Computer wins! {computer} beats {player}")
        computer_score += 1

    if not input("Play again? (y/n): ").lower() == "y":
        running = False

print ("thanks for playing!")
print(f"Final Scores:\nPlayer: {player_score}\nComputer: {computer_score}")