s="this is a string"
print(s.split())

str="hey*bud"
print(str.split("*"))

st=["sup","yo"]
print("@".join(st))
print(" ".join(st))

password="password=123456"
print(password.replace("123456","******"))

phone_number="+91 1234567890"
print(phone_number.startswith("+91"))

jsonfile="file.json"
print(jsonfile.endswith(".zip"))

fruit="banana is a fruit"
print(fruit.find("a"))
print(fruit.count("a"))

num=1234
print(f"Number {num}")

a=12
b=27
print(f"{a} + {b} = {a+b}")

pre="one sentence"
space1=pre.find(" ")
rem=pre.slice(0,2)
print(rem)


