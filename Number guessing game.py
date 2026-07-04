import random
hide = random.randint(1,100)
while True:
    num = int(input("Guess a number between 1 and 100: "))
    if num<hide:
        print("Too low...")
    elif num>hide:
        print("Too high...")
    else:
        print("Right guess!")
        break
    
