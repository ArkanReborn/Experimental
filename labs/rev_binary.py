def int_to_reverse_binary(x):
    input_string = ''
    
    while x > 0:
        input_string = input_string + str(x % 2)
        x = x // 2
    return input_string

def string_reverse(input_string):
    rev = ''
    for i in range(len(input_string), 0, -1):
        rev = rev + input_string[i-1]
    print(rev)
    return rev
        
if __name__ == '__main__':
    # Type your code here. 
    # Your code must call int_to_reverse_binary() to get 
    # the binary string of an integer in a reverse order.
    # Then call string_reverse() to reverse the string
    # returned from int_to_reverse_binary().
    
    int_val = int(input())
    
    input_string = int_to_reverse_binary(int_val)
    string_reverse(input_string)