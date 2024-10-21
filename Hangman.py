#Hangman game

import random
words = ("apple", "pear", "banana", "coconut", " pineapple")

#dictionaty of keywords:()
hangman-art = {0: ("   ",
                   "   ",
                   "   "),
               1: (" 0  ",
                   "   ",
                   "   "),
               2: (" 0  ",
                   " |  ",
                   "   "),
               3: (" 0  ",
                   " |/  ",
                   "  "),
               4: (" 0  ",
                   "\|/  ",
                   "    "),
               5: (" 0  ",
                   "\|/  ",
                   "/   "),
               6: (" 0  ",
                   " \/  ",
                   " /\  ")}