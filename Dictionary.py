d={"name":"Lia","age":20}
print(d)

print(d.get("age"))

print(d.keys())

print(d.values())

print(d.items())

d.update(name="Sia")
print(d)

print(d["name"])

d["name"]="Lia"
print(d)

d["age"]=21
print(d)

d["marks"]=100
print(d)

d.pop("marks")
print(d)

print("marks" in d)

student={
    "John":{
        "age":20,
        "marks":89
    },
    "Alice":{
        "age":21,
        "marks":99
    }
}
print(student)
print(student["Alice"]["age"])