mx = 0


def max_magnitude(user_val1, user_val2, user_val3):
    if abs(user_val1) > abs(user_val2) and abs(user_val1) > abs(user_val3):
        mx = user_val1
    elif abs(user_val2) > abs(user_val1) and abs(user_val2) > abs(user_val3):
        mx = user_val2
    elif abs(user_val3) > abs(user_val1) and abs(user_val3) > abs(user_val2):
        mx = user_val3
    return mx


if __name__ == "__main__":
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    maximum = max_magnitude(num1, num2, num3)
    print(maximum)
