from string import ascii_letters

def lexicographic_permutations(elements):
    permutations = []
    elements.sort()  # Sort the elements in ascending order
    permutations.append(elements.copy())  # Add the initial sorted permutation

    while True:
        i = len(elements) - 2
        while i >= 0 and elements[i] >= elements[i + 1]:
            i -= 1

        if i == -1:
            break

        j = len(elements) - 1
        while elements[j] <= elements[i]:
            j -= 1

        x = elements[i]
        elements[i] = elements[j]
        elements[j] = x

        elements[i + 1:] = elements[-1: i: -1]

        permutations.append(elements.copy())

    return permutations


class Solution:
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

