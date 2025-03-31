num1 = int(input("Enter first number:"))
num2 = int(input("Enter second number:"))

op = input("Enter math operation:")

if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
else:
    print("Enter valid operation")

print(result)