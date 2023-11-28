def text_name_of_month(month_int):
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

def total_number_days_in_month(month, year):
  days = 0
  if ("janurary" or "march" or "may" or "july" or "august" or  "october" or "december") in str(month).lower():
    days = 31
  elif ("april" or "june" or "september" or "november") in str(month).lower():
    days = 30
  elif str(month).lower() == "feburary":
    tst = year % 4  
    days = "0"
    iy = str(year)
    y = len(iy)

    if (iy[y-1] == '0' and year % 400 != 0) or tst != 0:
      days = 28
    elif tst == 0:
      days = 29
    return days

def print_month(year, month, weekDay):
  print(f"===Calendar for===\n======{year}======")
  print(f"          {text_name_of_month(month)}\n-----------------------------")
  print("Sun Mon Tue Wed Thu Fri Sat")

  for i in range(weekDay):
    print("    ", end="")

  for day in range(1, total_number_days_in_month(text_name_of_month(month), year) + 1):
    print(f"{day:2}", end=" ")
    weekDay = (weekDay + 1) % 7
    if weekDay == 0:
      print()

  start_of_next_month = weekDay

  if start_of_next_month != 0:
    print("")
  return start_of_next_month

if __name__ == "__main__":
  year = int(input("What year do you want a calendar for?: "))
  first_day = int(input("What is the first day of Janurary?: "))

  for month in range(12):
    print_month(year, month, first_day)