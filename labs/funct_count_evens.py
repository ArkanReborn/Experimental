def count_evens(num1, num2, num3, num4):
    lst = [num1, num2, num3, num4]
    counter = 0
    
    for num in lst:
        num = num % 2
        if num == 0:
            counter += 1
    return counter

if __name__ == '__main__':
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())
    num4 = int(input())
    
    result = count_evens(num1, num2, num3, num4)
    print(f'Total evens: { result }')