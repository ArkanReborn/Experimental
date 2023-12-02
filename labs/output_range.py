num1 = int(input())
num2 = int(input())

if num1 > num2:
    print("Second integer can't be less than the first.")
    exit(0)

for number in range(num1, num2 + 1, 5):
    print(number, end=" ")
print()
