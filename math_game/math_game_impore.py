import random

def question(a ,b ,oper): 

    """Generate a math question."""
                        
    if oper == '+':
        return( f"{a} + {b}=")
    elif oper == '-':
        return( f"{a} - {b}=")
    elif oper == '*':
        return( f"{a} x {b}=") 
    elif oper == '/':
        return( f"{a} / {b}=")

def answer(a, b, oper):  

    """Calculate the answer to a math question."""
                                
    if oper == '+':
        return(a+b)
    elif oper == '-':
        return(a-b)
    elif oper == '*':
        return(a*b) 
    elif oper == '/':
        return(round(a/b,3))


print('''MATH GAME 
by @Coding_group''')
print("\n")
print('-'*120,"\n")
name = str(input("Enter your name: "))
print('-'*120,"\n")

while True:
    
    a = random.randint(1,1000)
    b = random.randint(1,1000)
    oper = random.choice(['+','-','*','/'])
    print(question(a,b,oper))
    ans_pro = answer(a,b,oper)

    while True:
        try:
            ans_user = float(input("Enter the answer: "))
        except ValueError:
            print("Invalid input!\n")
            play_again = input("Do you want to play again? (Y/N): ")
            if play_again.upper() != 'Y':
                print('-'*120)
                exit(0)
            else:
                print('-'*120,"\n")
                break

        if ans_pro == ans_user:
            print(f"Correct Answer {name}!")
            print("Go to next question!")
            print('-'*120,"\n")
            break
        else:
            print(f"Wrong Answer {name}!")
            print(f"Try again \n")
    continue