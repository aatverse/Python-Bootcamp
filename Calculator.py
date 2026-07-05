#calculator
print("Enter first number:")
a = float(input())
print("Enter second number:")
b = float(input())
print("Enter operator (+, -, *, /):")
op = input()
if op == "+":
    print("Result:", a + b)
elif op == "-":
    print("Result:", a - b)
elif op == "*":
    print("Result:", a * b)
elif op == "/":
    print("Result:", a / b)
else:
    print("Invalid operator")