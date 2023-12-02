x = int(input())
mn = x
mx = x

while x >= 0:
    if mx < x:
        mx = x
    x = int(input())
print(f"{mx}")
