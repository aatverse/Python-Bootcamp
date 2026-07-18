def evenodd(n):
    if n%2==0:
        return True
    else:
        return False
n=int(input("enter number:"))
print(evenodd(n))

def is_positive(n):
    return n>0
n=int(input("enter number:"))
print(is_positive(n))

def is_vowel(ch):
    return ch in "aeiou"
ch=input("Enter a character:")
print(is_vowel(ch))