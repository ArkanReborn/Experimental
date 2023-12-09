def calc_toll(hour, is_morning, is_weekend):
    
    cost = 0.0
    
    if (hour < 7) and (is_morning == True):
        cost = 1.15
        if is_weekend == True:
            cost -= 0.10
    elif (hour >= 7 and hour < 10) and (is_morning == True):
        cost = 2.95
        if is_weekend == True and hour < 8:
            cost -= 0.80
    elif (hour >= 10 and is_morning == True) or (hour < 3 and is_morning == False):
        cost = 1.90
        if is_weekend == True:
            cost += 0.25
    elif (hour >= 3 and hour < 8) and (is_morning == False):
        cost = 3.95
    elif (hour >= 8 and is_morning == False):
        cost = 1.40
        if is_weekend == True:
            cost -= 0.30
    return round(cost, 2)
    
if __name__ == '__main__':
    print(f"{calc_toll(8, True, False)}")
    print(f"{calc_toll(1, False, False)}")
    print(f"{calc_toll(3, False, True)}")
    print(f"{calc_toll(5, True, True)}")