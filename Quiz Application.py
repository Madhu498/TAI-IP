import random

# Expanded Question Bank
all_questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
    {"question": "What is 5 + 3?", "options": ["6", "7", "8", "9"], "answer": "8"},
    {"question": "What is the largest planet?", "options": ["Earth", "Jupiter", "Mars", "Saturn"], "answer": "Jupiter"},
    {"question": "Who wrote 'Romeo and Juliet'?", "options": ["Shakespeare", "Dickens", "Homer", "Chaucer"], "answer": "Shakespeare"},
    {"question": "What is the boiling point of water?", "options": ["100°C", "50°C", "150°C", "200°C"], "answer": "100°C"},
    {"question": "What is the fastest land animal?", "options": ["Cheetah", "Lion", "Horse", "Kangaroo"], "answer": "Cheetah"},
    {"question": "What is the square root of 16?", "options": ["2", "3", "4", "5"], "answer": "4"},
    {"question": "Which element has the symbol 'O'?", "options": ["Oxygen", "Gold", "Iron", "Hydrogen"], "answer": "Oxygen"},
    {"question": "Who painted the Mona Lisa?", "options": ["Da Vinci", "Van Gogh", "Picasso", "Rembrandt"], "answer": "Da Vinci"},
    {"question": "What is the currency of Japan?", "options": ["Yen", "Dollar", "Euro", "Won"], "answer": "Yen"}
]

# Global variables
num_questions = 5  # Number of questions per quiz session

# Start Quiz
def start_quiz():
    # Select a subset of random questions
    questions = random.sample(all_questions, num_questions)
    score = 0
    
    print("\nWelcome to the Quiz!")
    print(f"You will be asked {num_questions} questions. Good luck!\n")
    
    for i, q in enumerate(questions):
        # Shuffle options for each question
        options = q["options"][:]
        random.shuffle(options)
        
        print(f"Q{i + 1}: {q['question']}")
        for idx, option in enumerate(options, 1):
            print(f"{idx}. {option}")
        
        # Validate user input
        while True:
            try:
                user_choice = int(input("Enter your choice (1-4): "))
                if user_choice < 1 or user_choice > 4:
                    raise ValueError
                break
            except ValueError:
                print("Invalid input. Please enter a number between 1 and 4.")
        
        # Check if the answer is correct
        if options[user_choice - 1] == q["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer was: {q['answer']}\n")
    
    # Display final score
    print(f"Quiz Completed! Your score: {score}/{num_questions} ({(score / num_questions) * 100:.2f}%)")
    print("Thanks for playing!\n")

# Main Function
def main():
    while True:
        print("=== Quiz Application ===")
        print("1. Start Quiz")
        print("2. Exit")
        
        choice = input("Choose an option: ").strip()
        if choice == "1":
            start_quiz()
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the application
if __name__ == "__main__":
    main()
