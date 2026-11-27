def frequency(str,char):
    return str.count(char)
def replace_char(str,old_char,new_char):
    return str.replace(old_char,new_char)
def remove_first(str,char):
    return str.replace(char," ",1)
def remove_all(str,char):
    return str.replace(char," ")
while True:
    print("========================== MENU ============================")
    print("a. Find frequency of a character in a string: ")
    print("b. Replace a character with another character in a string: ")
    print("c. Remove first occurence of a character in a string: ")
    print("d. Remove all occurences of a character from a string: ")
    print("e. Exit")

    choice=input("Enter your choice(a/b/c/d/e): ").lower()

    if choice=='e':
        print("Exiting the program...")
        break
    str=input("Enter string: ")
    if choice=='a':
        char=input("Enter character from string: ")
        print(f"Frequency of {char} is {frequency(str,char)}")
    elif choice=='b':
        old_char=input("Enter the character to be replaced: ")
        new_char=input("Enter the new character: ")
        print(f"New string: {replace_char(str,old_char,new_char)}")
    elif choice=='c':
        char=input("Enter the character to remove(first occurence): ")
        print(f"New string: {remove_first(str,char)}")
    elif choice=='d':
        char=input("Enter the character to remove(all occurences): ")
        print(f"New string: {remove_all(str,char)}: ")
    else:
        print("Invalid choice! Please select a valid option.")
print("================================================================")