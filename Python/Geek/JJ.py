N=5
Jack = 500
Jelly = -500
winner = 500
while N > 0:
        if N >= 4:
            N -= 4
            winner *= -1
        if N >= 2:
            N -=2
            winner *= -1
        if N >= 1:
            N -=1
            winner *= -1
if N == 0 and winner == -500:
    print(Jelly)
else:
    print(Jack)