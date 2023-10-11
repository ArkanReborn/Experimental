import math

nums = int(input("How many numbers would you like to compute? :\n"))

counts = 0
num_list = []

op = input("What operation would you like to use for this equation? :\n")

while counts != nums:
    counts += 1
    if counts == 1:
        num = input(f"What would you like to enter for your 1st number? : \n")
        num_list.append(num)
    elif counts == 2:
        num = input(f"What would you like to enter for your 2nd number? : \n")
        num_list.append(num)
    elif counts == 3:
        num = input(f"What would you like to enter for your 3rd number? : \n")
        num_list.append(num)   
    elif counts >= 4:
        num = input(f"What would you like to enter for your {counts}th number? : \n")
        num_list.append(num)          

if op == "+":
    while counts > 0:
        sol = (num_list[(counts - 1)] + (num_list[(counts - 2)]))
        counts -= 1
    print(f'The answer to your equation is {sol}', end='')
elif op != "+" or "-" or "/" or "*":
    print("Unsported operand!")