def stockBuySell(price, n):
    start=0
    i=1
    ans=[]
    while i<n:
        if price[i-1]<price[i]:
            i+=1
        else:
            if start!=i-1:
                ans.append([start,i-1])
            start=i
            i+=1
    if start!=n-1:
        ans.append([start,n-1])
    if not ans:
        print("No Profit")
        return 
    else:
        for i in ans:
            print("("+str(i[0])+' '+str(i[1])+")",end=' ')
        print()
    
#https://practice.geeksforgeeks.org/problems/stock-buy-and-sell2615/1