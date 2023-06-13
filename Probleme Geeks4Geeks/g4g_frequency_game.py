'''Given an array A of size N. The elements of the array consist of positive integers. You have to find the largest element with minimum frequency.'''

def LargButMinFreq(arr,n):
    
    dicts = {}
    lis = []
    for ar in arr:
        if ar in dicts:
            dicts[ar]+= 1
        else:
            dicts[ar] =  1
    
    min_m = min(dicts.values())
    for frq in dicts:
        if dicts[frq] == min_m:
            lis.append(frq)
    return max(lis)