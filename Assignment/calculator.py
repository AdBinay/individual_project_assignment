import random
import matplotlib.pyplot as plt

students_performance = {}

def generate_question():
    """Generate random numbers and return a math question."""
    num1 = random.randint(1, 10)
    num2 = random.randint(1, 10)
    return num1, num2

def ask_question(question_type):
    """Ask a math question based on the user's chosen type."""
    num1, num2 = generate_question()
    
    if question_type == 1:
        answer = num1 + num2
        print(f"What is {num1} + {num2}?")
    elif question_type == 2:
        answer = num1 - num2
        print(f"What is {num1} - {num2}?")
    elif question_type == 3:
        answer = num1 * num2
        print(f"What is {num1} * {num2}?")
    elif question_type == 4:
        # Ensure no division by zero
        while num2 == 0:
            num2 = random.randint(1, 10)
        answer = num1 / num2
        print(f"What is {num1} / {num2}? (Round to 2 decimal places)")
    else:
        # Randomly select any type of question
        question_type = random.randint(1, 4)
        return ask_question(question_type)

    return answer

def get_user_input():
    """Prompt the user to select the type of arithmetic problem."""
    print("Choose the type of arithmetic problem to study:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Random Mixture")
    
    while True:
        try:
            choice = int(input("Enter your choice (1-5): "))
            if 1 <= choice <= 5:
                return choice
            else:
                print("Please enter a valid number (1-5).")
        except ValueError:
            print("Invalid input. Please enter a number (1-5).")

def provide_feedback(correct):
    """Give feedback based on the user's answer."""
    if correct:
        responses = ['Very good!', 'Nice work!', 'Keep up the good work!']
        print(random.choice(responses))
    else:
        responses = ['No. Please try again.', 'Wrong. Try once more.', 'No. Keep trying.']
        print(random.choice(responses))

def display_statistics(user_name, performance):
    """Display statistics for a specific user."""
    correct = performance["correct"]
    incorrect = performance["incorrect"]
    total = correct + incorrect
    accuracy = (correct / total) * 100 if total > 0 else 0

    print(f"\nStatistics for {user_name}:")
    print(f"Total Questions: {total}")
    print(f"Correct Answers: {correct}")
    print(f"Incorrect Answers: {incorrect}")
    print(f"Accuracy: {accuracy:.2f}%")

    # Plotting the performance in a graph
    labels = 'Correct', 'Incorrect'
    sizes = [correct, incorrect]
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # explode the 'Correct' slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title(f"Performance of {user_name}")
    plt.show()

def display_all_statistics():
    """Display combined statistics for all users."""
    all_correct = sum(user["correct"] for user in students_performance.values())
    all_incorrect = sum(user["incorrect"] for user in students_performance.values())
    total_questions = all_correct + all_incorrect

    print("\nCombined Statistics for All Students:")
    print(f"Total Questions Answered: {total_questions}")
    print(f"Total Correct Answers: {all_correct}")
    print(f"Total Incorrect Answers: {all_incorrect}")

    # Plotting the combined performance
    labels = 'Correct', 'Incorrect'
    sizes = [all_correct, all_incorrect]
    colors = ['lightgreen', 'lightcoral']
    explode = (0.1, 0)  # explode the 'Correct' slice

    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    plt.title("Combined Performance of All Students")
    plt.show()

def main():
    user_name = input("Enter your name: ")
    question_type = get_user_input()
    score = 0
    total_questions = 5

    # Initialize or update the performance data for the current user
    if user_name not in students_performance:
        students_performance[user_name] = {"correct": 0, "incorrect": 0}

    for _ in range(total_questions):
        correct_answer = ask_question(question_type)
        try:
            user_answer = float(input("Your answer: "))

            if round(user_answer, 2) == round(correct_answer, 2):
                provide_feedback(True)
                students_performance[user_name]["correct"] += 1
                score += 1
            else:
                provide_feedback(False)
                students_performance[user_name]["incorrect"] += 1
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
            students_performance[user_name]["incorrect"] += 1

    print(f"\nYou got {score} out of {total_questions} questions correct!")

    # Display statistics for the current user
    display_statistics(user_name, students_performance[user_name])

    # Optionally display combined statistics for all students
    display_all_statistics()

if __name__ == "__main__":
    main()
