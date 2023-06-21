import random


start = "15/03/2020"

startNums = start.split('/')

end = "30/07/2025"

endNums = end.split('/')

year = random.choice(range(int(startNums[2]), int(endNums[2]) + 1))

if year == int(startNums[2]):
    month = random.choice(range(int(startNums[1]) + 1, 13))

elif year == int(endNums[2]):
    month = random.choice(range(1, int(endNums[1]) + 1))

else:
    month = random.choice(range(1, 13))


if month == int(startNums[1]) and year == int(startNums[2]):
    day = random.choice(range(int(startNums[0]), 31))

elif month == int(endNums[1]) and year == int(endNums[2]):
    day = random.choice(range(1, int(endNums[0]) + 1))

else:
    day = random.choice(range(1, 31))

print(day,'/', month, '/', year)
