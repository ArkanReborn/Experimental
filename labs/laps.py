def laps_to_miles(user_miles):
    return user_miles * 0.25


if __name__ == "__main__":
    miles = float(input())

    print(f"{laps_to_miles(miles):.2f}")
