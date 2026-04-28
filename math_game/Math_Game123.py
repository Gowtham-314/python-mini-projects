import random

def question(a,b):                              #question

    if a <= 500:
        print( f"{a}+{b}=")
    elif a <= 200:
        print( f"{a}-{b}=")
    elif b <= 300:
        print( f"{a}x{b}=") 
    elif b >= 0:
        print( f"{a}/{b}=")
    else:
        print( f"{a}-{b}=")

def answer(a,b):                                 #Answer

    if a <= 500:
        return(a+b)
    elif a <= 200:
        return(a-b)
    elif b <= 300:
        return(a*b) 
    elif b >= 0:
        return(round(a/b,3))
    else:
        return(a-b)

print("MATH GAME")
print("\n")
print("WELCOME TO YOU")
name = str(input("enter the your name >>"))
print("\n")
while True:
    a = random.randint(1,500)
    b = random.randint(1,500)
    print(question(a,b))
    ans_pro = answer(a,b)

    while True:
        ans_user = float(input("enter the answer >> "))
        if ans_pro == ans_user:
            print(f"Answer is correct {name}!")
            print("Try next question!")
            print("\n")
            break
        else:
            print(f"Answer is wrong {name}!")
            print(f"It's Okay, Try again {name}!")
            print("\n")
    continue