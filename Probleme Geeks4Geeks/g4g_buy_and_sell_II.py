'''The cost of stock on each day is given in an array A[] of size N. Find all the days on which you buy and sell the stock so that in between those days your profit is maximum.

Note: Output format is as follows - (buy_day sell_day) (buy_day sell_day)
For each input, the output should be in a single line, i.e. It's important to move to a new/next line for printing the output of other test cases.'''

def stockBuySell(price, n): #metoda mea, mai buna IMO
    sol = []
    buy = -1
    buyPrice = 0
    sell = -1
    
    for i in range(1, n):
        
        if i == n - 1 and buyPrice != 0:
            sell = i
            sol.append((buy, sell))
        
        if price[i - 1] < price[i] and buyPrice == 0:
            buy = i - 1
            buyPrice = price[i - 1]
            
        elif price[i - 1] > price[i] and buyPrice > price[i]:
            sell = i - 1
            sol.append((buy, sell))
            buyPrice = 0
            
    formatted_output = ' '.join('({} {})'.format(x, y) for x, y in sol)
        
    print(formatted_output)
            

def stockBuySell2(price, n): #unfinished
    sol = []
    buy = -1
    buyPrice = 0
    sell = -1
    
    for i in range(1, n):
        
        if i == n - 1 and buyPrice != 0:
            sell = i
            sol.append((buy, sell))
        
        if price[i - 1] < price[i] and buyPrice == 0:
            buy = i - 1
            buyPrice = price[i - 1]
            
        elif price[i - 1] > price[i] and buy != -1:
            sell = i - 1
            sol.append((buy, sell))
            buyPrice = 0
            
    formatted_output = ' '.join('({} {})'.format(x, y) for x, y in sol)
        
    print(formatted_output)

print(stockBuySell2([886, 2777, 6915, 7793, 8335, 5386], 6))