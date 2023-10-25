def swap_values(user_val1, user_val2, user_val3, user_val4):
    num1 = user_val2
    num2 = user_val1
    num3 = user_val4
    num4 = user_val3
    lst = [num1, num2, num3, num4]
    
    return num1, num2, num3, num4
    
if __name__ == '__main__': 
    
    val1 = int(input())
    val2 = int(input())
    val3 = int(input())
    val4 = int(input())
    
    numb1, numb2, numb3, numb4 = swap_values(val1, val2, val3, val4)
        
    print(f'{numb1} {numb2} {numb3} {numb4}')