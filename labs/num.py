low = int(input())
high = int(input())

x = int(input())

counter = 0

if low + x >= high:
    print("0")
    exit(0)

while low < high:
    counter += 1
    low += x
print(counter)
