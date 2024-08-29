import random
import statistics as stats
# Game setup
questions = [
    {"question": "What is 5 + 3?", "answer": 8},
    {"question": "What is 12 - 4?", "answer": 8},
    {"question": "What is 7 * 6?", "answer": 42},
    {"question": "What is 81 / 9?", "answer": 9},
    {"question": "What is 9 + 7?", "answer": 16}
]
# Initialize game
scores = []
num_questions = len(questions)
def ask_question():
    question = random.choice(questions)
    answer = question["answer"]
    user_answer = int(input(question["question"] + " "))
    return user_answer == answer
# Main game loop
for _ in range(num_questions):
    if ask_question():
        print("Correct!")
        scores.append(1)
    else:
        print("Incorrect!")
        scores.append(0)
# Calculate statistics
print("\nGame Over!")
print(f"Total Score: {sum(scores)}")
print(f"Average Score: {stats.mean(scores):.2f}")
print(f"Median Score: {stats.median(scores)}")
print(f"Mode Score: {stats.mode(scores)}")
print(f"Variance: {stats.variance(scores):.2f}")
print(f"Standard Deviation: {stats.stdev(scores):.2f}")

