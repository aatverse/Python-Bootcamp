def Is_even(num):
    if num%2==0:
        return True
    else:
        return False
n=int(input("Enter a number: "))
if Is_even(n):
    print(n,"is even.")
else:
    print(n,"is odd.")