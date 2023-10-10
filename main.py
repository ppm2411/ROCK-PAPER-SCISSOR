import random
print("WELCOME TO GAME OF ROCK PAPER SCISSORS")

# user choice 
user_choice=input("What you will choose among rock ,paper and scissor ")
user_choice=user_choice.lower()

# computer choice
x=random.randint(0,2)
if x==0:
    comp_choice="rock"
elif x==1:
    comp_choice="paper"
elif x==2:
    comp_choice="scissor"

# logic to choose who wins
if user_choice=="rock" and comp_choice=="scissor":
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.Congratulations ! You win.")
elif user_choice=="paper" and comp_choice=="rock":
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.Congratulations ! You win.")
elif user_choice=="scissor" and comp_choice=="paper":
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.Congratulations ! You win.")
# logic to choose who looses
elif user_choice=="scissor" and comp_choice=="rock":
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.Sorry ! You loose. Better luck next time.")
elif user_choice=="rock" and comp_choice=="paper":
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.Sorry ! You loose. Better luck next time.")
elif user_choice=="paper" and comp_choice =="scissor":
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.Sorry ! You loose. Better luck next time.")

# logic to choose is it becomes tie
elif user_choice==comp_choice:
    print(f"Your choice is {user_choice}. Computer's choice is {comp_choice}.It is tie.")
else:
    print("invalid input! Try again.")


