s1 = "Hello"
s2 = "Bye"

def merge_alternatively(s1, s2):
    merged_string = ''
    i = 0
    while i < len(s1) and i < len(s2):
        merged_string += s1[i] + s2[i]
        i += 1
    
    if i < len(s1):
        merged_string += s1[i:]
    elif i < len(s2):
        merged_string += s2[i:]
    
    return merged_string

print(merge_alternatively(s1,s2))