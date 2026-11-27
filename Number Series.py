#1-2+3-4+5-6...n
n=int(input("Enter the number of elements: "))
result=0
for i in range(1,n+1):
    if i%2==0:
        result-=i
    else:
        result+=i
print("Result is:",result)
    
