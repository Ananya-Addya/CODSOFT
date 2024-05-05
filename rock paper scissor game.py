import random
print("Welcome to ROCK PAPER and SCISSER")
print("-------------------------------------------------------")
User=input("Enter your name:")
value={0:"Rock",1:"Paper",2:"Scissers"}
print()
up=0 #for user point count
cp=0 #for computer point count
while True:
    user_choice=int(input("Enter your choice=0...Rock,1...Paper,2...Scissors,3...Exit\n"))
    if user_choice==3:
        break
    if user_choice >2 or user_choice < 0:
        print("Wrong input")
    else:
        computer_choice=random.randint(0,2)
        print("Computer choice:")
        print(value[computer_choice])
        print(User," choice:")
        print(value[user_choice])
        if user_choice == computer_choice:
            print("It's a draw")
        elif user_choice == 0 and computer_choice == 2:
            print("winner is",User)
            up+=1
        elif computer_choice == 0 and user_choice == 2:
            print("winner is computer")
            cp+=1
        elif user_choice > computer_choice:
            print("winner is",User)
            up+=1
        elif computer_choice > user_choice:
            print("Winner is computer")
            cp+=1
if up==cp:
    print("The match is draw")
    print(User," point=",up)
    print("Computer point=",cp)
elif up>cp:
    print(User,"win the match")
    print(User," point=",up)
    print("Computer point=",cp)
else:
    print("Computer win the match")
    print(User," point=",up)
    print("Computer point=",cp)
