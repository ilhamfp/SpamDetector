def countLPS(pattern):
    # finding the LPS from string pattern
    lps = [0]
    
    for i in range(1, len(pattern)):
        j = lps[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[j] == pattern[i]: lps.append(j+1)
        else: lps.append(j)
    
    return lps
        
def KMP(text, pattern):
    # find the initial index where the pattern found in text using KMP algorithm
    kmp = []
    j = 0
    lps = countLPS(pattern)
    for i in range(len(text)):
        while j > 0 and text[i] != pattern[j]:
            j = lps[j - 1]
        if text[i] == pattern[j]: 
            j += 1
        if j == len(pattern):  # found the pattern
             kmp.append(i-j+1)
             j = lps[j-1]
    return len(kmp) > 0

if __name__ == "__main__":
    print( KMP("abacaabacabacababa", "acabaca"))