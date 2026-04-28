import random

def generate_question():
    """Generate a math question and return the question string and the correct answer."""
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    oper = random.choice(['+', '-', '*', '/'])
    
    if oper == '/':
        # Ensure no division by zero
        b = random.randint(1, 1000)
    
    question_str = f"{a} {oper} {b} = "
    
    if oper == '+':
        correct_answer = a + b
    elif oper == '-':
        correct_answer = a - b
    elif oper == '*':
        correct_answer = a * b
    elif oper == '/':
        correct_answer = round(a / b, 3)
    
    return question_str, correct_answer

def math_game():
    print("MATH GAME by @Coding_group\n")
    name = input("Enter your name: ")
    print("\nWelcome, " + name + "!")
    print("Instructions: Solve the math problems. Type 'exit' to quit the game.\n")
    
    score = 0
    
    while True:
        question_str, correct_answer = generate_question()
        print(question_str)
        
        while True:
            user_input = input("Enter the answer (or type 'exit' to quit): ")
            
            if user_input.lower() == 'exit':
                print(f"Thanks for playing, {name}! Your final score is {score}.")
                return
            
            try:
                user_answer = float(user_input)
                
                if user_answer == correct_answer:
                    print(f"Correct Answer, {name}!")
                    score += 1
                    print("Go to the next question!\n")
                    break
                else:
                    print(f"Wrong Answer, {name}! Try again.\n")
                    
            except ValueError:
                print("Invalid input! Please enter a number.\n")

if __name__ == "__main__":
    math_game()