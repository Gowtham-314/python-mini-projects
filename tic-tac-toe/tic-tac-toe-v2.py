import random
  
def dis():
    
    print(f"""
    -----------
    {arr[0]} | {arr[1]} | {arr[2]}
    -----------
    {arr[3]} | {arr[4]} | {arr[5]}
    -----------
    {arr[6]} | {arr[7]} | {arr[8]} 
    -----------
    """)
    
def AI():
    # Winning moves or Blocking moves
    win_patterns = [
        (0,1,2),(3,4,5),(6,7,8),
        (0,3,6),(1,4,7),(2,5,8),
        (0,4,8),(2,4,6)
    ]

    # 1. Try to WIN
    for a,b,c in win_patterns:
        if arr[a]==arr[b]=="O" and arr[c]==" ":
            arr[c]="O"
            return
        if arr[a]==arr[c]=="O" and arr[b]==" ":
            arr[b]="O"
            return
        if arr[b]==arr[c]=="O" and arr[a]==" ":
            arr[a]="O"
            return

    # 2. Try to BLOCK X
    for a,b,c in win_patterns:
        if arr[a]==arr[b]=="X" and arr[c]==" ":
            arr[c]="O"
            return
        if arr[a]==arr[c]=="X" and arr[b]==" ":
            arr[b]="O"
            return
        if arr[b]==arr[c]=="X" and arr[a]==" ":
            arr[a]="O"
            return

    # 3. Otherwise play random
    while True:
        ai = random.randint(0,8)
        if arr[ai] == " ":
            arr[ai] = "O"
            return

        
  
def win():
    
    # Check rows
    if arr[0]==arr[1]==arr[2]=="X":
        return "X"
    if arr[3]==arr[4]==arr[5]=="X":
        return "X"
    if arr[6]==arr[7]==arr[8]=="X":
        return "X"
    
    # Check columns
    if arr[0]==arr[3]==arr[6]=="X":
        return "X"
    if arr[1]==arr[4]==arr[7]=="X":
        return "X"
    if arr[2]==arr[5]==arr[8]=="X":
        return "X"
    
    # Check diagonals
    if arr[0]==arr[4]==arr[8]=="X":
        return "X"
    if arr[2]==arr[4]==arr[6]=="X":
        return "X"
    
    # Check rows
    if arr[0]==arr[1]==arr[2]=="O":
        return "O"
    if arr[3]==arr[4]==arr[5]=="O":
        return "O"
    if arr[6]==arr[7]==arr[8]=="O":
        return "O"
    
    # Check columns
    if arr[0]==arr[3]==arr[6]=="O":
        return "O"
    if arr[1]==arr[4]==arr[7]=="O":
        return "O"
    if arr[2]==arr[5]==arr[8]=="O":
        return "O"
    
    # Check diagonals
    if arr[0]==arr[4]==arr[8]=="O":
        return "O"
    if arr[2]==arr[4]==arr[6]=="O":
        return "O"
    
    return None


while True:
    
    arr=[" " for _ in range(9)]
    print("\n\n----------------------------------------\n")
    print("Welcome to Tic-Tac-Toe!")
    print("You are playing as 'X' and the AI is 'O'.")
    print("Enter the Index to play: ")
    print("""
    -----------
     1 | 2 | 3
    -----------
     4 | 5 | 6
    -----------
     7 | 8 | 9
    -----------
        """)

    try:
        while True:
            ind=input("Enter the index : ( X )")
            
            if arr.count(" ") == 0:
                print("Game Over. It's a draw.")
                break
            if ind == "" or not ind.isdigit():
                print("Invalid input. Please enter a number.")
                continue
            
            ind=int(ind)-1
            if arr[ind] == "X" or arr[ind] == "O":
                print("Already filled. Choose another index.")
                continue
            
            arr[ind]="X"
            AI()
            dis()
            
            if win()=="X":
                print("X is the Win.")
                break
            if win()=="O":
                print("O is the Win.")
                break
            
    except IndexError:
        print("out of range.")
        
    if input("Do you want to play again? (y/n): ").lower() == 'y':
        continue