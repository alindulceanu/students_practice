from itertools import product, permutations
import numpy as np
'''N = int(input('N:'))
K = int(input('K:'))'''
N = 3
K = 3
z = K
nums = [x for x in range(K)]

prod = tuple(product(nums, repeat = N))
perm = tuple(permutations(prod, len(prod)))

perm2 = np.asarray(perm)


print(perm2)

def check(S, values): 

    if len(S) == 0 or len(S) < N:
        return False
    flag = False
    for i in range(len(S) - N):
        if int(S[i]) == values[0]: 
            for k in range(1, len(values) - 1):
                if int(S[i + k]) == values[k]:
                    if k == len(values) - 1:
                        flag = True
                        break
                    else:
                        continue
                else:
                    break

        if flag == True:
            break

    return flag


def minimize(perm):
    Smin = '999999999999999999999999999999'
    for i in range(len(perm)):
        S = str()
        for j in range(1, len(perm[i])):
            x = 0
            flag = False
            if check(S,perm[i][j - 1]) == True:
                continue

            if perm[i][j - 1][len(perm[i][j]) - 1] == perm[i][j][0]:

                while x < len(perm[i][j - 1]):
                    S = S + str(perm[i][j - 1][x])
                    x = x + 1

                for k in range(j, len(perm[i])):
                    if check(S,perm[i][k]) == True:
                        flag = True
                        break

                if flag == False:
                    S = S[:-x]
                    x = 0
                    while x < len(perm[i][j - 1]) - 1:
                        S = S + str(perm[i][j - 1][x])
                        x = x + 1
            else:
                while x < len(perm[i][j - 1]):
                        S = S + str(perm[i][j - 1][x])
                        x = x + 1

                
            if j == len(perm[i]) - 1:
                if check(S,perm[i][j]) == False:
                    x = 0
                    while x < len(perm[i][j]):
                        S = S + str(perm[i][j][x])
                        x = x + 1

        if len(S) < len(Smin):
            Smin = S

    return Smin
            


print(minimize(perm2))



