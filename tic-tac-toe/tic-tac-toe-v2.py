import random
from termcolor import colored, cprint  
import time

# Winning moves or Blocking moves
win_patterns = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
    ]


def dis():
    
    def format_cell(index):
        if arr[index] == "X":
            return colored(arr[index], "red", attrs=["bold"])
        elif arr[index] == "O":
            return colored(arr[index], "yellow", attrs=["bold"])
    
    cprint(f"""
    -----------
     {format_cell(0) if arr[0] != " " else "1"} | {format_cell(1) if arr[1] != " " else "2"} | {format_cell(2) if arr[2] != " " else "3"}
    -----------
     {format_cell(3) if arr[3] != " " else "4"} | {format_cell(4) if arr[4] != " " else "5"} | {format_cell(5) if arr[5] != " " else "6"}
    -----------
     {format_cell(6) if arr[6] != " " else "7"} | {format_cell(7) if arr[7] != " " else "8"} | {format_cell(8) if arr[8] != " " else "9"}
    -----------
    """, "white")
    
def AI():

    # 1. Try to WIN and BLOCK X
    for a,b,c in win_patterns:
        if (arr[a]==arr[b]=="O" or arr[a]==arr[b]=="X") and arr[c]==" ":
            arr[c]="O"
            return
        
        if (arr[a]==arr[c]=="O" or arr[a]==arr[c]=="X") and arr[b]==" ":
            arr[b]="O"
            return
        
        if (arr[b]==arr[c]=="O" or arr[b]==arr[c]=="X") and arr[a]==" ":
            arr[a]="O"
            return
        
    # 2. Otherwise play random
    while True:
        ai = random.randint(0,8)
        if arr[ai] == " ":
            arr[ai] = "O"
            return

        
def win():
    
    for a,b,c in win_patterns:
        if arr[a]==arr[b]==arr[c]=="X":
            return "X"
        if arr[a]==arr[b]==arr[c]=="O":
            return "O"
        
    return None


starting_player = "X"

while True:
    
    arr=[" " for _ in range(9)]
    print("\n\n----------------------------------------")
    cprint("Welcome to Tic-Tac-Toe!\n", "cyan", attrs=["bold","underline"]    )
    cprint("You are playing as 'X' and the AI is 'O'\n.", "yellow", attrs=["bold"])
    cprint("Enter the Index to play: ", "magenta", attrs=["bold"])
    cprint("""
    -----------
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    -----------
        """, "white", attrs=["bold"])
    print("----------------------------------------\n")
    
    win_status = None
    current_turn = starting_player

    try:
        while True:
            if current_turn == "X":
                ind = input(colored(f"Enter the index {colored('X', 'red', attrs=['bold'])} :", "light_blue", attrs=["bold"]))

                if ind == "" or not ind.isdigit() or int(ind) < 1 or int(ind) > 9:
                    cprint("Invalid input. Please enter a number between 1 and 9.", "red", attrs=["bold"])
                    continue

                ind=int(ind)-1
                if arr[ind] in ("X", "O"):
                    cprint("Already filled. Choose another index.", "red", attrs=["bold"])
                    continue

                arr[ind]="X"
                dis()
                win_status = win()
                if win_status == "X":
                    cprint("You are the Win.", "green", attrs=["bold"])
                    break

                if arr.count(" ") == 0:
                    cprint("Game Over. It's a draw.", "red", attrs=["bold"])
                    break

                current_turn = "O"
                
            else:
                cprint(f"{colored('AI', 'yellow', attrs=['bold'])} is making a move....", "cyan", attrs=["bold"])
                time.sleep(1)  # Pause for a moment to simulate thinking
                AI()
                dis()
                win_status = win()
                if win_status == "O":
                    cprint("AI is the Win.", "green", attrs=["bold"])
                    break

                if arr.count(" ") == 0:
                    cprint("Game Over. It's a draw.", "red", attrs=["bold"])
                    break

                current_turn = "X"
                    
    except IndexError:
        cprint("out of range.", "red", attrs=["bold"])
        
    if win_status in ("X", "O"):
        starting_player = win_status
        
    if win_status is None and arr.count(" ") == 0:
        if current_turn == "X":
            starting_player = "O"
        else:
            starting_player = "X"

    if input(f"{colored('Do you want to play again? (y/n): ', 'magenta', attrs=['bold'])}").lower() != 'y':
        cprint("Thank you for playing!", "cyan", attrs=["bold"])
        exit()