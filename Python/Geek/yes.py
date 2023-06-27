A= [1,3,5,2,2] 
sol = 0
sol2 = 0
wow = 0
for i in A:
    A.reverse()
    sol += i
    A.reverse()
    sol2 += i
    wow += 1
if sol == sol2:
    print(wow)