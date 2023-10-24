def mph_and_minutes_to_miles(miles, minutes):
    hours = minutes / 60.0
    miles_traveled = hours * miles
    return miles_traveled

miles_per_hour = float(input())
minutes_traveled = float(input())

print(f'Miles: {mph_and_minutes_to_miles(miles_per_hour, minutes_traveled):f}')