L=[]
for i in range(3):
    L.append(i)
print(L)

a=[1,0,3]
b=[4,5,6]
b.extend(a)
print(b)

b.insert(3,"sup")
print(b)

b.remove(1)
print(b)

b.pop(0)
print(b)

c=sorted(a)
print(a)
print(c)

users = ["Alice","Bob"]
scores = [90,80]
for u,s in zip(users,scores):
    print(u,s)

L1=[x*x for x in range(1,4)]
print(L1)