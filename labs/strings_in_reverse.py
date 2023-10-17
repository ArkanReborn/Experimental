user_input = input()


while user_input.lower() not in ["done", "d"]:
        reversed_input = user_input[::-1]
        print(reversed_input)
        user_input = input()