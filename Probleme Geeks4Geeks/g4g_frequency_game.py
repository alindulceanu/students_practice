'''Given an array A of size N. The elements of the array consist of positive integers. 
You have to find the largest element with minimum frequency.'''

def LargButMinFreq(arr,n):
    
    dicts = {}
    lis = []
    for i in arr:               #Calculating the frequency of every value
        if i in dicts:          #and storing it in a dictionary
            dicts[i]+= 1
        else:
            dicts[i] =  1
    
    min_m = min(dicts.values())
    for frq in dicts:
        if dicts[frq] == min_m:         #Scrolling through the dictionary and adding the values with lowest frequencies
            lis.append(frq)             
    return max(lis)                     #Returning the maximum value from the list