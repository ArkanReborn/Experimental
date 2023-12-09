def feet_to_steps(user_feet):
    ft = user_feet / 2.5
    return int(ft)


if __name__ == "__main__":
    feet = float(input())
    print(f"{feet_to_steps(feet)}")
