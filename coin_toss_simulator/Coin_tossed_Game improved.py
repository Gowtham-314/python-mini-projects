import random
import turtle

def reward(i):
    if i==1:
        print(random.choice(['Correct_answer!','Congraulations!','Amazing!','Incredible!','Well_done!','Keep_trying']))
    else:
        print(random.choice(['Oops!',"Don't Worry",'Wrong!','Try_again','Motivate!']))

def graphic(name):
    s=turtle.Screen()
    s.bgcolor("black")
    s.title("Winner Announcement")
    t=turtle.Turtle()
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


print('''COIN_TOSSED GAME 
by @Coding_group''')
print("\n")
print('-'*120,"\n")

info = input("You aready to play with computer (Y/N):")
if info.upper() != 'Y':
    exit(0)

User_name = str(input("Enter your name: "))
print('-'*120,"\n")
User_name=User_name.capitalize()
print("Head:H / Tail:T\nGame_begins")
print('-'*120,"\n")

count_user=0
count_com=0
i=0
j=0

while True:
    
    i=i+1

    #User_turn
    print(f"{User_name}'s_turn")
    print('-'*30,'\n')
    oper=random.choice(['T','H'])
    user_input=input("Coin_tosed: Head/Tail>>")

    if user_input.upper() == oper:
        reward(1)
        count_user=count_user+1
    else:
        reward(0)
    non = input("press 'Enter':")
    print('-'*80,"\n")


    #Computer__turn
    print("Computer's_turn")
    print('-'*30),'\n'
    com_input = random.choice(['T','H'])
    print(f"Coin_tosed: Head/Tail>>{com_input.lower()}")
    if com_input.upper() == oper:
        reward(1)
        count_com=count_com+1
    else:
        reward(0)
    non = input("press 'Enter':")
    print('-'*80,"\n")

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
    
        print('-'*120,"\n")


        #reloaded the function
        info = input("Do you want play next level (Y/N):")
        if info.upper() != 'Y':
            exit(0)
        else:
            count_user=0
            count_com=0
            i=0
            j+=1


        print("\n")
        print('-'*120,"\n")