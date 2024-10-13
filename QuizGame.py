#QuizGame

questions = ("What is the capital city of France?: ",
            "Which planet is known as the 'Red Planet'?: ",
            "Who wrote the play 'Romeo and Juliet'?:  ",
            "What is the chemical symbol for gold?: ",
            "Which country is known as the Land of the Rising Sun?: ")

options = (("A. Berlin", "B. Madrid", "C. Rome", "D. Paris"),
           ("A. Venus ", "B. Mars ", "C. Jupiter ", "D. Saturn"),
           ("A. Charles Dickens", "B. William Shakespeare", "C. Jane Austen", "D. Mark Twain"),
           ("A. Ag", "B. Au", "C. Fe", "D. Pb"),
           ("A. China", "B. South Korea", "C. Japan", "D. Thailand"))

answers = ("D", "B","B", "B", "C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("------------------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Choose an option (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct!")
    else:
        print("Incorrect!")
        print(f"{answers[question_num]} is the correct answer!")
    question_num += 1 # this will increment the question numbers

print("------------------------------")
print("          RESULTS             ")
print("------------------------------")
print("answers: ", end=" " )
for answer in answers:
    print(answer, end=" ") # end=" " in the print() function prints answers on the same line with spaces between them.
print() # The extra print() ensures that after printing the answers, the cursor moves to the next line, making the output more readable.

print("guesses: ", end=" " )
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100) 
print(f" your total score is {score}")
print()