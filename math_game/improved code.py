import random
import tkinter
import os

def question(a, b, oper):

    """Generate a math question."""

    if oper == '+':
        return f"{a} + {b} = "
    elif oper == '-':
        return f"{a} - {b} = "
    elif oper == '*':
        return f"{a} x {b} = "
    elif oper == '/':
        return f"{a} / {b} = "

        

def answer(a, b, oper):

    """Calculate the answer to a math question."""
    
    if oper == '+':
        return a + b
    elif oper == '-':
        return a - b
    elif oper == '*':
        return a * b
    elif oper == '/':
        return round(a / b, 3)
       
print("MATH GAME\n")
name = input("Enter your name: ")

arr=os.get_terminal_size()



print(arr)



while True:
    a = random.randint(1, 500)
    b = random.randint(1, 500)
    oper = random.choice(['+','-','*','/'])
    print(question(a, b, oper))
    ans_pro = answer(a, b, oper)

    while True:
        try:
            ans_user = float(input("Enter the answer: "))
            break
        except ValueError:
            print("Invalid input! Please enter a number.")

    if ans_pro == ans_user:
        print(f"Correct, {name}!")
    else:
        print(f"Wrong answer, {name}! The correct answer is: {ans_pro}")

    play_again = input("Do you want to play again? (yes/no): ")
    if play_again.lower() != 'yes':
        break