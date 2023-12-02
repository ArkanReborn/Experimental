def name_of_month(month_int):
    if month_int == 0:
        month_int = "Janurary"
    elif month_int == 1:
        month_int = "Feburary"
    elif month_int == 2:
        month_int = "March"
    elif month_int == 3:
        month_int = "April"
    elif month_int == 4:
        month_int = "May"
    elif month_int == 5:
        month_int = "June"
    elif month_int == 6:
        month_int = "July"
    elif month_int == 7:
        month_int = "August"
    elif month_int == 8:
        month_int = "September"
    elif month_int == 9:
        month_int = "October"
    elif month_int == 10:
        month_int = "November"
    elif month_int == 11:
        month_int = "December"
    return month_int


def days_in_month(month, year):
    days = 0
    if str(month).lower() in [
        "janurary",
        "march",
        "may",
        "july",
        "august",
        "october",
        "december",
    ]:
        days = 31
    elif str(month).lower() in ["april", "june", "september", "november"]:
        days = 30
    elif str(month).lower() == "feburary":
        tst = year % 4
        days = "0"
        iy = str(year)
        y = len(iy)

        if (iy[y - 1] == "0" and year % 400 != 0) or tst != 0:
            days = 28
        elif tst == 0:
            days = 29
    return days


def input_day_of_week():
    day = input(
        "What day of the week does January 1 begin on, (ex. Sunday, Monday, Tuesday, etc.): "
    )

    days_of_week = [
        "sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
    ]

    while day.lower() not in days_of_week:
        day = input(
            "ERROR: Enter Sunday, Monday, Tuesday, Wednesday, Thursday, Friday, or Saturday: "
        )

    if day.lower() == "sunday":
        first_day = 0
    elif day.lower() == "monday":
        first_day = 1
    elif day.lower() == "tuesday":
        first_day = 2
    elif day.lower() == "wednesday":
        first_day = 3
    elif day.lower() == "thursday":
        first_day = 4
    elif day.lower() == "friday":
        first_day = 5
    elif day.lower() == "saturday":
        first_day = 6

    return first_day


def print_month(year, month, weekday):
    start_of_next_month = 0

    start_of_next_month = (weekday + days_in_month(name_of_month(month), year)) % 7

    print(f"          {name_of_month(month)}\n-----------------------------")
    print("Sun Mon Tue Wed Thu Fri Sat")

    for i in range(weekday):
        print("    ", end="")

    for day in range(1, days_in_month(name_of_month(month), year) + 1):
        print(f" {day:2}", end=" ")
        weekday = (weekday + 1) % 7
        if weekday == 0:
            print()

    if start_of_next_month != 0:
        print("")
    print("\n")

    return start_of_next_month


if __name__ == "__main__":
    year = int(input("What year do you want a calendar for?: "))
    first_day = input_day_of_week()

    print(f"===Calendar for===\n======{year}======")

    for month in range(12):
        first_day_of_next = print_month(year, month, first_day)
        first_day = first_day_of_next
