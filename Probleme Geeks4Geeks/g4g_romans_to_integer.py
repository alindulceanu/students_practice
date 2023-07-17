class Solution:
    def romanToInt(self, s: str) -> int:
        romans = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000} # Assigning every letter to it's integer counterpart
        intvalue = romans[s[-1]]                        # Initializing the converted value with the last element of the string
        sign = 1                                        # Sign dictates if the current item should be added or substracted from the converted value

        for i in range(len(s) - 1, 0, -1):              # Iterating from right to left makes the algorithm so much easier
            if romans[s[i]] > romans[s[i - 1]]:         # If the current value is less than the previous one we want to substract it
                sign = -1

            elif romans[s[i]] < romans[s[i - 1]]:       # Else, we add it
                sign = 1

            intvalue += romans[s[i - 1]] * sign         

        return intvalue
    
    def intToRoman(self, s: int) -> str:
        romans = {1 : 'I', 4 : 'IV', 5 : 'V', 9 : 'IX', 10 : 'X', 40 : 'XL', 50 : 'L', 90 : 'XC', 100 : 'C', 400 : 'CD', 500 : 'D', 900 : 'CM', 1000 : 'M'}  # Assigning every combination of roman letters to their values
        romanValue = ''                             # String to store the converted value

        while s != 0:                               # Iterating until s is empty
            for i in reversed(romans.keys()):
                if s >= i:                          # If s is greater or equal with a specific key, add the value of the key to the storing string and substract the key from s
                    romanValue += romans[i]
                    s -= i
                    break

        return romanValue
            

    
ob = Solution()

print(ob.intToRoman(1994))