'''Given an array a[] of size N which contains elements from 0 to N-1, 
you need to find all the elements occurring more than once in the given array. 
Return the answer in ascending order.

Note: The extra space is only for the array to be returned.
Try and perform all operations within the provided array. '''

from collections import Counter

class Solution:                                     # Too slow
    def duplicates(self, arr, n): 
        freq = {}
        dupli = []

        for i in arr:                               # Iteranting through all the elements in arr
            if i not in dupli:
                if i not in freq.keys():            # If 'i' can't be found inside freq - add it with the value of 1
                    freq[i] = 1

                else:
                    freq[i] += 1

                    if freq[i] > 1:                 # If 'i' is found more than 2 times (duplicate), then add it to the list that stores only the duplicates
                        dupli.append(i)

        if len(dupli) == 0:                         # If dupli is empty return -1
            return [-1]
        
        else:
            dupli.sort()
            return dupli
        



    def duplicates2(self, arr, n):
        dupli=[]
        c = Counter(arr)                            # Counter() stores every value of arr as dictionary keys and the values are the frequencies, thus making it easier to count them

        for i in c:
            if c[i] > 1:                            # Check if the value is greater than 1
                dupli.append(i)

        if len(dupli) == 0:                          # If dupli is empty return -1
            return [-1]

        dupli.sort()
        return dupli