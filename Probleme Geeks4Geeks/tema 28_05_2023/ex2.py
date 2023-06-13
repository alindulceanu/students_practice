"""[Thursday 16:43] Borza, Razvan (PERO-SD)

•Given a list of elements, perform grouping of similar elements, as different key-value list in dictionary.

•Input : test_list = [4, 6, 6, 4, 2, 2, 4, 8, 5, 8]

•Output : {4: [4, 4, 4], 6: [6, 6], 2: [2, 2], 8: [8, 8], 5: [5]}

•Explanation :

•Similar items grouped together on occurrences. ]

•Input : test_list = [7, 7, 7, 7]

•Output : {7 : [7, 7, 7, 7]}

•

•Convert Key-Value list Dictionary to List of Lists.

•Sometimes, while working with a Python dictionary, we can have a problem in which we need to perform the flattening of a key-value pair of dictionaries to a list and convert it to a list of lists.

•This can have applications in domains in which we have data.
"""

l = list()
d = dict()

N = int(input('N:'))

for i in range(N):
    l.append(int(input('list:')))

while len(l) != 0:
    x = l.pop(0)

    if d.get(x) is not None:
        d[x].append(x)

    else:
        d[x] = [x]



print(d)