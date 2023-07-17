class Solution:
    def __init__(self):
        self.sum = 0                    # In comb we will store the current combination, in combs all the combinations that equal the target
        self.comb = []
        self.combs = []
        self.sorted = False             # Boolean variable to check if the candidates have benn sorted

    def combinationSum(self, candidates, target: int):
        if not self.sorted:             # Sorting the candidates
            candidates.sort()
            self.sorted = True

        if self.sum == target:          # If the sum is equal to the target, check if the current combination is already in the combs vector
            x = sorted(self.comb)
            flag = False

            for i in self.combs:
                if x == i:
                    flag = True
                    break
            
            if not flag:
                self.combs.append(self.comb.copy())     # Without using .copy() the code will store pointers of comb inside combs which is not what we want

            return -1
        
        elif self.sum > target:                         # If the sum is greater than the target, we need to go back
            return -1
        
        for i in candidates:                            # Backtracking every combination lesser or equal with the target
            self.comb.append(i)             
            self.sum += i
            self.combinationSum(candidates, target)
            self.comb.pop()
            self.sum -= i

        if len(self.comb) == 0:                         # Return combs only if all the combinations have been tried
            return self.combs
        
        
    
ob = Solution()                                         # Driver code

print(ob.combinationSum([2, 3, 6, 7], 7))


