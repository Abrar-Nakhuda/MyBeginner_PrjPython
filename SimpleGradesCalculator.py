#SimpleGradesCalculator

def get_grade(score):
    if 95 <= score <= 100:
        return "A+"
    elif 90 <= score <= 94:
        return "A-"
    elif 85 <= score <= 89:
        return "B+"
    elif 80 <= score <= 84:
        return "B-"
    elif 75 <= score <= 79:
        return "C+"
    elif 70 <= score <= 74:
        return "C-"
    elif 65 <= score <= 69:
        return "D+"
    elif 60 <= score <= 64:
        return "D-"
    elif 0 <= score < 59:
        return "F"
    else:
        return "Invalid score"

while True:
    try:
        score = float(input("Enter the student's score (0-100): "))
        if score < 0 or score > 100:
            print(f"{score} is Invalid.")
        else:
            grade = get_grade(score)
            print(f"The student's grade is: {grade}")
        break
    except ValueError:
        print("Please enter a valid numeric score.")