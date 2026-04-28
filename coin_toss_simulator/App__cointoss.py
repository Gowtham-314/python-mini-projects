import random
import turtle
import tkinter as tk
from tkinter import messagebox
def reward(i):
    """Returns the reward to user."""
    if i==1:
        print(random.choice(['Correct_answer!','Congraulations!','Amazing!','Incredible!','Well_done!','Keep_trying']))
    else:
        print(random.choice(['Oops!',"Don't Worry",'Wrong!','Try_again','Motivate!']))

def graphic(name):  
    """Return the graphic visual."""   
    s = turtle.Screen()
    s.bgcolor("black")
    s.title("Winner Announcement")

    t = turtle.Turtle()
    t.speed(0)
    t.hideturtle()
    t.color("yellow")
    t.up()
    t.goto(0, -100)
    t.write("Winner!", align="center", font=("Times new roman", 60, "bold"))
    t.up()
    t.goto(0,0)
    t.write(f"{name}", align="center", font=("Times new roman", 60, "bold"))
    s.mainloop()


def winner():
    
    if count_user > count_com:
        return(f"{User_name}.")
    elif count_user < count_com:
        return("Computer.")
    elif count_user == 0 and count_com == 0:
        return("No Winner.")
    else:
        return(f"{User_name} and Computer.")



def winner():
    try:
        ans_user = float(entry.get())
    except ValueError:
        messagebox.showerror("Invalid input", "Please enter a valid number.")
        return
    if count_user > count_com:
        messagebox.showinfo(f"{User_name}.")
    elif count_user < count_com:
        messagebox.showinfo("Computer.")
    elif count_user == 0 and count_com == 0:
        messagebox.showinfo("No Winner.")
    else:
        messagebox.showerror(f"{User_name} and Computer.")
        entry.delete(0, tk.END)

def next_question():
    global oper
    oper=random.choice(['T','H'])
    question_label.config(text="Coin_tosed: Head/Tail>>")
    ans_pro = answer(a, b, oper)
    entry.delete(0, tk.END)

def initial():
    global count_user
    global count_com
    global i

    while True:
        
        i=i+1

def User_turn():
    print(f"{User_name}'s_turn")
    oper=random.choice(['T','H'])
    user_input=input("Coin_tosed: Head/Tail>>")

    if user_input.upper() == oper:
        reward(1)
        count_user=count_user+1
    else:
        reward(0)

def com_turn():
    #Computer__turn
    print("Computer's_turn")
    com_input = random.choice(['T','H'])
    print(f"Coin_tosed: Head/Tail>>{com_input.lower()}")
    if com_input.upper() == oper:
        reward(1)
        count_com=count_com+1
    else:
        reward(0)

def check_win():
    #score checking
    if i==10:
        print(f'''
        Level_completed:

        Score_Board:
                    {User_name} scored {count_user}.
                    Computer scored {count_com}.
                
        Level_Winner:
                    {winner()}
                                ''')

    if winner()==f"{User_name}.":
        graphic(User_name)
    elif winner()=='Computer.':
        graphic('Computer')
    else:
        graphic('none')

        
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
root.title("COIN_TOSSED GAME")         
# Welcome Screen
welcome_label = tk.Label(root, text="COIN_TOSSED GAME\nby @Coding_group",
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
submit_button = tk.Button(game_frame, text="Submit Answer",command=winner)
submit_button.pack(pady=10)
exit_button = tk.Button(game_frame, text="Exit", command=exit_game)
exit_button.pack(pady=10)
# Start the application
root.mainloop()