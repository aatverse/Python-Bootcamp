#rockpaperscissors
import string
import random
choices=['rock','paper','scissors']
user=input("Choose(Rock/Paper/Scissors):")
user.lower()
opponent=random.choice(choices)
print(opponent)
if user==opponent:
    print("Draw")
elif user=="rock":
    if opponent=="paper":
        print("You lost")
    else:
        print("You won!")
elif user=="paper":
    if opponent=="rock":
        print("You won!")
    else:
        print("You lost")
else:
    if opponent=="rock":
        print("You lost")
    else:
        print("You won!")

