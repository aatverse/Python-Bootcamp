def yo():
    print("Hello")
    print("Wassup")
yo()


def hey(name): #with parameter
    print("hey",name)
hey("Julie")
hey("Tom")


def room(color,size): #with multiple parameters
    print("This room is",color)
    print("It's quite",size)
room("red","big")


def add(a,b): #using return
    return(a+b) #Use print() to show something to the user. Use return to give a value back so your program can use it later.
sum=add(3,6) #won't show any output if called without print()
print(sum)


def summ(c,d): #using print() instead of return
    print(c,d)
x=summ(4,8)
print(x)


def area(length, width):
    return length*width
print(area(5, 4))