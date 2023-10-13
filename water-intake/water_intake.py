import math

weight = int(input("Please input your weight: \n"))
wtmod = (weight) * 2/3
activity = int(input("Please indicate how many minutes you exercised today: \n"))

actwater = 0

if activity > 15 and activity >= 0:
    actwater += 6
    activity -= 15

final = wtmod + actwater
cups = final // 12

print(f"Your final water intake needed is: \n{final:.0f} ounces or {cups:.0f} cups")