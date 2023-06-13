from itertools import product


'''N = int(input('N:'))
K = int(input('K:'))'''
N = 2
K = 2
k = N
nums = [x for x in range(K)]

perm = tuple(product(nums, repeat = N))

S = str()


print(perm)

def recursive(perm,i,j, k = 0):
    global S
    
    if S[j] == str(perm[i][k]):
        if k == N - 1:
            return True
        else:
            return recursive(perm, i, j + 1, k + 1)

    else:
        return False


def checkConnection(perm, i = 1):
    global S
    global k
    
    if S[-(k-i)] == str(perm[i - 1]):
        
        if i == k - 1:
            
            k = N
            return i
        else:
            return checkConnection(perm, i + 1)
    
    elif i == k - 1:
    
        k = N
        return i - 1   


    else:
        k = k - 1
        return checkConnection(perm, i)

def addAtTheEnd(i, permut):
    
    global S
    
    for x in range(i,N):
        H = str(permut[x])
        S = S + H
        

if len(S) == 0:
    for i in range(N):
        S = S + str(perm[0][0])

for i in range(len(perm)):
    flag = False
    for j in range(len(S) - N + 1):
        if recursive(perm,i,j) == True:
            flag = True
            break

    if flag == False:
        addAtTheEnd(checkConnection(perm[i]), perm[i])
        


print(S)


