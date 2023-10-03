import math
# Calculator

num1 = float(input("What would you like your first number to be? :\n"))
num2 = float(input("What would you like your second number to be? :\n"))
op = input("What operation would you like to use? : (+, -, /, *, ^, |, <, >)\n")

solution = 0

if op == "+":
    solution = num1 + num2
    print('The answer to your problem is:', solution)
elif op == "-":
    solution = num1 - num2
    print('The answer to your problem is:', solution)
elif op == "/":
    solution = num1 / num2
    print('The answer to your problem is:', solution) 
elif op == "*":
    solution = num1 * num2
    print('The answer to your problem is:', solution)
elif op == "^":
    solution = (math.pow((num1), num2))
    print('The answer to your problem is:', solution)
elif op == "|":
    solution = (math.sqrt(num1))
    print('The answer to your problem is:', solution)
elif op == ">":
    if num1 > num2:
        print('The answer to your problem is: True')
    else:
        print("The answer to your problem is: False")
elif op == "<":
    if num1 < num2:
        print('The answer to your problem is: True')
    else:
        print("The answer to your problem is: False")
else:
    print('Unsupported operation!')