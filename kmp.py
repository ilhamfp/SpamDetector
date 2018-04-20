def kmp_preprocess(pattern):
    border_table = {}
    for miss in range(1, len(pattern)):
        k = miss - 1
        largest_border = 0
        for j in range(0, k):
            prefix = pattern[:(j + 1)]
            suffix = pattern[k - j : k + 1]
            if prefix == suffix:
                largest_border = j + 1
                
        border_table[miss] = largest_border
    return border_table
            
def kmp(text, pattern):
    border_table = kmp_preprocess(pattern)
    #print(border_table)
    i = 0
    j = 0
    while i < len(text):
        while j < len(pattern):
            #print(i, j, text[i + j], pattern[j])
            if text[i + j] != pattern[j]:
                forward = border_table.get(j, -1)
                #print("Forward ", forward, " j ", j)
                if forward == 0:
                    i += j
                    j = 0
                elif forward == -1:
                    i += j + 1
                    j = 0
                else:
                    #print("Before ", i)
                    i += j - forward
                    #print("After ", i)
                    j = forward
                break
            j += 1
        if j == len(pattern):
            return i
    return -1

print(kmp('abacaabacabacababa', 'acabaca'))
