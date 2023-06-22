N=5
bills = [5, 5, 5, 10, 20]

reservefive = 0
reserveten = 0
reservetwenty = 0
for i in bills:
    if i == 5:
        reservefive += 5
    if i == 10:
        reserveten += 10 
        reservefive -= 5
    if i == 20:
        reservetwenty += 20
        if reserveten >= 10:
            reserveten -= 10 
            reservefive -= 5
        else:
            reservefive -= 15
    if  reservefive <= -5 or reserveten <= -5 or reservetwenty <= -5:
        print(False)
    else:
        continue 
if  reservefive >= 0 and reserveten >= 0 and reservetwenty >= 0:
    print (True)
else:
    print (False)