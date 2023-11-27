year = int(input("What year do you want a calendar for?: "))
month_num = int(input("What month (num)?: "))

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
  if ("janurary" or "march" or "may" or "july" or "august" or  "october" or "december") in month.lower():
    days = 31
  elif ("april" or "june" or "september" or "november") in month.lower():
    days = 30
  elif month.lower() == "feburary":
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
  if weekDay == 0:
    weekDay = "Sunday"
  elif weekDay == 1:
    weekDay = "Monday"
  elif weekDay == 2:
    weekDay = "Tuesday"
  elif weekDay == 3:
    weekDay = "Wednesday"
  elif weekDay == 4:
    weekDay = "Thursday"
  elif weekDay == 5:
    weekDay = "Friday"
  elif weekDay == 6:
    weekDay = "Saturday"
  print(f"The year is {year} \nThe month is {text_name_of_month(month)[:3]} and it is {weekDay} \n{text_name_of_month(month)} has {total_number_days_in_month(text_name_of_month(month), year)} days.")

print_month(year, month_num, 0)

i = 1

print(f"===Calendar for===\n======{year}======")
while i <= 12:
  curr_month = (text_name_of_month(i-1))
  print(f"         {curr_month}\n-----------------------------\nSun Mon Tue Wed Thu Fri Sat")
  
  