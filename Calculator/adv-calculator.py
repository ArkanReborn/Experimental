import math

nums = int(input("How many numbers would you like to compute? :\n"))

count = 0
num_list = []

op = input("What operation would you like to use for this equation? :\n")

while count != nums:
    num = input("What would you like to enter for your {count} number? : \n")
    num_list.append(num)
    count += 1

if op == "+":
    while count > 0:
        sol = str(num_list[(count - 1)] + (num_list[(count - 2)]))
        count -= 1
print(f'The answer to your equation is {sol}')