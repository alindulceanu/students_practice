from string import ascii_letters

def lexicographic_permutations(elements):
    permutations = []
    elements.sort()                                                     # Sort the elements in ascending order
    permutations.append(elements.copy())                                # Add the initial sorted permutation

    while True:                                                         # i and j are the elements we want to swap
        i = len(elements) - 2
        while i >= 0 and elements[i] >= elements[i + 1]:                # i is the rightmost element that is greater than it's right adjacent element
            i -= 1

        if i == -1:                                                     # when i = -1 the permutation will look like this '4321' which is the last one in an lexicographical order
            break

        j = len(elements) - 1                                           # j is the first element (counting from right to left) that is lesser than i
        while elements[j] <= elements[i]:
            j -= 1

        x = elements[i]                                                 # swap i and j
        elements[i] = elements[j]
        elements[j] = x

        elements[i + 1:] = elements[-1: i: -1]                          # all elements from i to n will be turned upside down

        permutations.append(elements.copy())                            # adding the permutation to the list

    return permutations


class Solution:                                                         # The same thing as above, but with letters from 'ascii_letters'
    def find_permutation(self, S):
        perm = []

        val = ''.join(sorted(S))

        perm.append(val)

        h = list(val)

        while True:
            
            i = len(val) - 2
            while i >= 0 and ascii_letters.find(h[i]) > ascii_letters.find(h[i + 1]):
                i -= 1

            if i == -1:
                break

            j = len(val) - 1
            while ascii_letters.find(h[j]) < ascii_letters.find(h[i]):
                j -= 1

            h[i], h[j] = h[j], h[i]

        
            h[i + 1:] = h[-1: i: -1]
            
            perm.append(''.join(h))

        return perm


print(ascii_letters)
    

obj = Solution()

print(obj.find_permutation("ABSG"))

