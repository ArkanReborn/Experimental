def exact_change(user_total):
    quarters = user_total // 25
    user_total %= 25
    dimes = user_total // 10
    user_total %= 10
    nickels = user_total // 5
    user_total %= 5
    pennies = user_total
    return (pennies, nickels, dimes, quarters)


if __name__ == "__main__":
    total_change = int(input())

    if total_change == 0:
        print("no change")
    else:
        pennies, nickels, dimes, quarters = exact_change(total_change)

        if pennies > 0:
            if pennies == 1:
                print(pennies, "penny")
            else:
                print(pennies, "pennies")

        if nickels > 0:
            if nickels == 1:
                print(nickels, "nickel")
            else:
                print(nickels, "nickels")

        if dimes > 0:
            if dimes == 1:
                print(dimes, "dime")
            else:
                print(dimes, "dimes")

        if quarters > 0:
            if quarters == 1:
                print(quarters, "quarter")
            else:
                print(quarters, "quarters")
