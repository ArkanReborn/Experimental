num = int(input())

lst = []

last = 0

for number in range(num + 1):
    number = int(input())
    lst.append(number)
    last = number

lst.pop(-1)

for number in lst:
    if number <= last:
        print(number, end=',')