'''You are an owner of lemonade island, each lemonade costs $5. Customers are standing in a queue 
to buy from you and order one at a time (in the order specified by given array bills[]). 
Each customer will only buy one lemonade and pay with either a $5, $10, or $20 bill.
You must provide the correct change to each customer so that the net transaction is that 
the customer pays $5.

NOTE: At first, you do not have any bill to provide changes with. 
You can provide changes from the bills that you get from the previous customers.

Given an integer array bills of size N where bills [ i ] is the bill the ith customer pays, 
return true if you can provide every customer with the correct change, or false otherwise.'''

class Solution:
    def lemonadeChange(self, N, bills):
        change = {5:0, 10:0, 20:0}              # A dictionary to store the number of bills

        for i in range(N):                      # Iterating through the orders
            if bills[i] == 5:
                change[5] += 1                  # If the client gives a $5 bill, we just add it to the dictionary

            elif bills[i] == 10:                # For $10 we add a $10 bill, but we take a $5 bill as change
                change[10] += 1
                change[5] -= 1

            elif bills[i] == 20:                # For $20 we add a $20 bill and we can either take a $10 bill and a $5 bill
                change[20] += 1

                if change[10] != 0:
                    change[10] -= 1
                    change[5] -= 1

                else:
                    change[5] -= 3              # or we can take 3 $5 bills if there is no $10 bill left

            for j in change.keys():             # Checking if any of the bills went negative, that means we can't give change to all of the clients
                if change[j] < 0:
                    return False
                
            
        return True
                

ob = Solution()

print(ob.lemonadeChange(5, [5,5,10,10,20]))