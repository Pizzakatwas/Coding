#the rock, paper, scissors game hehehe
import time
import random
while True:

    list = ["rock","paper","scissors"]
    choice = random.choice(list)

    while True:
        choicex = input("chooose your player ('rock','paper','scissors'): ")
        if choicex == list[0] or choicex == list[1] or choicex == list[2]:
            break
        else:
            print("invalid choice")
            pass

    for i in range(3,0,-1):
        print("the computer will choose in "+str(i))
        time.sleep(1)
    print("computer has chosen "+choice)
    if choicex == choice:
        print("its a draw!")
    elif choicex == "rock" and choice== "paper" or choicex == "paper" and choice == "scissors" or choicex == "scissors" and choice == "rock":
        print("you lose stoopid")
    else:
        print("you win")
    replay = input("Do you want to play again (yes/no)?: ")
    if replay == "yes":
        pass
    else:
        break