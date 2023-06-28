'''Given two arrays: a1[0..n-1] of size n and a2[0..m-1] of size m. 
Task is to check whether a2[] is a subset of a1[] or not. Both the arrays can be sorted or unsorted. 
There can be duplicate elements.'''


def isSubset( a1, a2, n, m):
    
    A2 = {}                                             # Initializing a hashmap for values in a2

    for i in range(m):                                  # Adding the values and their frequencies in the hashmap
        if a2[i] not in A2.keys():
            A2[a2[i]] = 1

        else:
            A2[a2[i]] += 1

    for i in a1:                                        # If we find a value from a2 in a1 we decrease the frequency of that key by 1
        if i in A2.keys():
            if A2[i] > 0:
                A2[i] -= 1

    if all(map(lambda x: x == 0, A2.values())):         # If all the frequencies in A2 are 0, a2 is a subset of a1
        return 'Yes'
    
    else:
        return 'No'
    
print(isSubset([11, 7, 1, 13, 21, 3, 7, 3], [11, 3, 7, 1, 7], 8, 5))