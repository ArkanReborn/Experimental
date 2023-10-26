import math

temp = int(input("Enter current Farenheit temperature, must be value >= -58 and <= 50 degrees: "))
ws = int(input("Enter the current wind speed that must be >= 3 mph: "))

if temp < -58 or temp > 50:
  print("No wind chill temperature calculated:\nInvalid Temperature: valid value must be >= -58 and <= 50 degrees")
elif ws < 3:
  print("No wind chill temperature calculated:\nInvalid Wind Speed: valid value, must be >= 3 mph")
elif temp < -58 or temp > 50 and ws > 3:
  print('No wind chill temperature calculated:\nInvalid temperature and Wind Speed Entered! Both outside of valid ranges')
else:

  celsius = ((temp - 32) * 5) / 9

  print()
  print(f'The current Farenheit temperature is: {temp:.2f}')
  print(f'The current Celsius temperature is: {celsius:.2f}')
  print(f'The current wind speed is: {ws}')
  print()

  v = math.pow(ws, 0.16)
  chill_form = 35.74 + 0.6215 * temp - 35.75 * v + 0.4275 * temp * v
  
  print(f'Based on the entered temperature {temp:.2f} and wind speed of {ws:.2f} the currently calculated wind-chill is calculated to be: {chill_form:.2f}')
  
  if chill_form <= -18:
    print('WARNING: Frostbite can occur at this wind-chill in less than 30 minutes')