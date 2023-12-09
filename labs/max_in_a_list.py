def ints_less_than_or_equal_to_threshold(user_values, upper_threshold):
    for value in user_values:
        if value <= upper_threshold:
            print(value, end="\n")


def get_user_values():
    num = int(input())
    lst = []
    for i in range(num):
        lst.append(int(input()))
    return lst


if __name__ == "__main__":
    userValues = get_user_values()
    upperThreshold = int(input())
    ints_less_than_or_equal_to_threshold(userValues, upperThreshold)
