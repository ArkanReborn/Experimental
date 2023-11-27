def days_in_feb(user_year):
    tst = user_year % 4  
    days = "0"
    iy = str(user_year)
    y = len(iy)
    i = iy[y-1]
    
    if (i == '0' and user_year % 400 != 0) or tst != 0:
        days = 28
    elif tst == 0:
        days = 29
    return days
    
if __name__ == '__main__':
    year = int(input())
    days = days_in_feb(year)
    
    print(f'{year} has {days} days in February.')