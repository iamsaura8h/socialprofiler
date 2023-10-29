def ask_question(question, options, correct_option):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    choice = input("Enter your choice (1-5): ")
    return options[int(choice) - 1] == correct_option

questions = [
    "What is the next number in the sequence: 2, 4, 6, 8, ...?",
    "If a shirt costs $20 after a 25% discount, what was its original price?",
    "Which of the following is a prime number: 16, 23, 32, 41, 50?",
    "If a clock shows 3:15, what is the angle between the hour and minute hands?",
    "Complete the series: 3, 6, 12, 24, ...?",
    "What is the square root of 144?",
    "If x + 5 = 10, what is the value of x?",
    "Which of the following is an example of a renewable resource: coal, wind, or natural gas?",
    "What is the chemical symbol for water?",
    "If a triangle has angles of 90, 45, and 45 degrees, what type of triangle is it?"
]

options = [
    ["10", "12", "14", "16", "18"],
    ["$15", "$18", "$25", "$22", "$24"],
    ["23", "32", "41", "16", "50"],
    ["0 degrees", "45 degrees", "90 degrees", "180 degrees", "360 degrees"],
    ["48", "32", "60", "36", "72"],
    ["12", "10", "16", "14", "8"],
    ["5", "10", "15", "20", "25"],
    ["coal", "wind", "natural gas", "none of the above"],
    ["H2O", "CO2", "O2", "CH4", "NaCl"],
    ["Equilateral", "Isosceles", "Scalene", "Right"]
]

correct_answers = [1, 1, 2, 2, 4, 1, 2, 2, 1, 4]

user_answers = []

print("Welcome to the Aptitude and Logical Reasoning Quiz!")
print("Please select the correct option for each question.\n")

for i in range(10):
    is_correct = ask_question(questions[i], options[i], correct_answers[i])
    user_answers.append(is_correct)

num_correct = sum(user_answers)

if 0 <= num_correct <= 2:
    rating = "Poor"
elif 3 <= num_correct <= 5:
    rating = "Good"
elif 6 <= num_correct <= 8:
    rating = "Excellent"
else:
    rating = "Outstanding"

print("\nThank you for completing the quiz!")
print(f"You got {num_correct} questions right.")
print(f"Your performance is rated as {rating}.")
