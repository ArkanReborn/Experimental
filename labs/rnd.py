num = int(input("Please enter a number:\n"))

numstr = str(num)
numlen = len(numstr)

lenn1 = numstr[numlen-1]
lenn2 = numstr[numlen-2]

if num < 11 or num >= 100:
    print('Input must be 11-100')
    exit(0)

while lenn1 != lenn2 and lenn2 != lenn1:
    if lenn1 == lenn2:
        print(num)
    else:
        print(num)
        num -= 1
        
        numstr = str(num)
        numlen = len(numstr)
        lenn1 = numstr[numlen-1]
        lenn2 = numstr[numlen-2]
print(num)