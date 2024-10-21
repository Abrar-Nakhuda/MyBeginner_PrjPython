#Hangman game
from Hangman_wordsList import words
import random


#dictionaty of keywords:()
hangman_art = {0: ("   ",
                   "   ",
                   "   "),
               1: ("0",
                   "  ",
                   "  "),
               2: (" 0 ",
                   " | ",
                   "   "),
               3: (" 0 ",
                   "/|",
                   "  "),
               4: (" 0  ",
                   "/|\\",
                   "    "),
               5: (" 0",
                   "/|\\  ",
                   "/   "),
               6: (" 0  ",
                   "/|\\  ",
                   "/ \\  ")}

def display_man(wrong_guesses):
    print("-----------------------------")
    for line in hangman_art[wrong_guesses]:
        print(line)
    print("-----------------------------")    

def display_hint(hint):
    print(" ".join(hint))
    

def display_answer(answer):
    pass

def main():
    answer = random.choice(words)
    hint =  ["_"] * len(answer)
    wrong_guesses = 0
    guessed_letters = set()
    is_running = True

    while is_running:
        display_man(wrong_guesses)
        display_hint(hint)
        guess = input("enter a letter: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("invalid input")
            continue

        if guess in guessed_letters:
            print(f"{guess} is already in Guessed")
            continue

        guessed_letters.add(guess)

        if guess in answer:
            for i in range(len(answer)):
                if answer[i] == guess:
                    hint[i] = guess
        else:
            wrong_guesses += 1
        
        if "_" not in hint:
            display_man (wrong_guesses)
            display_answer(answer)
            print(f"you Win!! {answer} is correct")
            is_running = False
        elif wrong_guesses >= len(hangman_art) -1:
            display_man(wrong_guesses)
            #display_answer(answer)
            print(f"You Lost HAhA, the correct answer is {answer}.")
            is_running = False

if __name__ == "__main__":
    main()