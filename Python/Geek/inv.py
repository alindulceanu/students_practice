n = 5
nums = [10, 3, 5, 6, 2]
sol = []
P = [None] * n
for i in range(n):
    P = nums.copy()
    result = 1
    P.pop(i)
    for x in P:
        result = result * x
    sol.append(result)