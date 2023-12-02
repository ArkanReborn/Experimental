x = int(input())
mn = x
mx = x

while x > 0:
    if mn > x:
        mn = x
    if mx < x:
        mx = x
    x = int(input())
print(f"{mn} and {mx}")
