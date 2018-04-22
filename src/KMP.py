### KMP Algorithm ###

# Finding LPS
def countLPS(pattern):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, false either
    return type : boolean
    """
    # finding the LPS from string pattern
    lps = [0]
    
    for i in range(1, len(pattern)):
        j = lps[i - 1]
        while j > 0 and pattern[j] != pattern[i]:
            j = lps[j - 1]
        if pattern[j] == pattern[i]: lps.append(j+1)
        else: lps.append(j)
    
    return lps
        
# KMP implementation        
def KMP(text, patternList):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, false either
    return type : boolean
    """
    # find the initial index where the pattern found in text using KMP algorithm
    kmp = []
    for pattern in patternList:
        pattern = pattern.lower()
        if(len(pattern) == 0):
            continue
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