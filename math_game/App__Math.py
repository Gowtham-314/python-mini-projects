import random
import tkinter as tk
from tkinter import messagebox
def question(a, b, oper):
    """Generate a math question."""
    if oper == '+':
        return f"{a} + {b} ="
    elif oper == '-':
        return f"{a} - {b} ="
    elif oper == '*':
        return f"{a} x {b} ="
    elif oper == '/':
        return f"{a} / {b} ="
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
def check_answer():
    try:
        ans_user = float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return
    if ans_pro == ans_user:
        messagebox.showinfo("Correct!", f"Correct Answer, {name}!")
        next_question()
    else:
        messagebox.showerror("Wrong", f"Wrong Answer, {name}! Try again.")
        entry.delete(0, tk.END)
def next_question():
    global a, b, oper, ans_pro
    a = random.randint(1, 1000)
    b = random.randint(1, 1000)
    oper = random.choice(['+', '-', '*', '/'])
    question_label.config(text=question(a, b, oper))
    ans_pro = answer(a, b, oper)
    entry.delete(0, tk.END)
def start_game():
    global name
    name = name_entry.get()
    if name.strip() == "":
        messagebox.showerror("Error", "Please enter your name.")
        return
    name_label.config(text=f"Player: {name}")
    next_question()
    name_frame.pack_forget()
    game_frame.pack()
def exit_game():
    root.destroy()

    
root = tk.Tk()
root.title("Math Game")
# Welcome Screen
welcome_label = tk.Label(root, text="MATH GAME\nby @Coding_group",
font=("Arial", 20))
welcome_label.pack(pady=10)
# Name Entry Frame
name_frame = tk.Frame(root)
name_frame.pack(pady=10)
name_label = tk.Label(name_frame, text="Enter your name:")
name_label.grid(row=0, column=0, padx=10)
name_entry = tk.Entry(name_frame)
name_entry.grid(row=0, column=1, padx=10)
start_button = tk.Button(name_frame, text="Start Game",
command=start_game)
start_button.grid(row=1, column=0, columnspan=2, pady=10)
# Game Frame
game_frame = tk.Frame(root)
question_label = tk.Label(game_frame, text="", font=("Arial", 16))
question_label.pack(pady=10)
entry = tk.Entry(game_frame, font=("Arial", 16))
entry.pack(pady=10)
submit_button = tk.Button(game_frame, text="Submit Answer",
command=check_answer)
submit_button.pack(pady=10)
exit_button = tk.Button(game_frame, text="Exit", command=exit_game)
exit_button.pack(pady=10)
# Start the application
root.mainloop()