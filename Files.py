file=open("notes.txt") #or file=open("notex.txt","r") reading is the default mode hence "r" need not be specified
#print(file.readline())
#print(file.read())
print(file.readlines())
file.close()

file=open("notes.txt","w")
file.write("Hello World")
file.close()

file=open("notes.txt","a")
file.write("\nThis is a new line.")
file.close()

file=open("newfile.txt","w") #creating a new file
file.write("This is a new file")
file.close()

with open("newfile.txt") as file:
    print(file.read())

with open("newfile.txt","w") as file:
    file.write("Writing using with")

with open("newfile.txt","r+") as file:
    print(file.tell())
    print(file.read(2))
    file.write("\nHello")
    print(file.tell())
    file.seek(0)
    print(file.tell())