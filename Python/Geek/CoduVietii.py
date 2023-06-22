N=9
K=3

queue = list(range(1,N+1))
sol = 0
while len(queue) > 1:
    for i in range(K):
        if len(queue) == 1:
            break
        else:
            del queue[:K]
            del queue[-K:]
print(queue[0])
    
    #https://practice.geeksforgeeks.org/problems/ticket-counter-2731/1?page=1&sortBy=latest

    #Mortu asta de site zice ca mai trebuie optimizat si da fail la 2 cazuri de test