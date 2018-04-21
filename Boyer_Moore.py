def boyer_moore(text, patternList):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, false either
    return type : boolean
    """
    for pattern in patternList:
        pattern = pattern.lower()
        i = 0
        j = 0
        while (i + j) < len(text):
            j = len(pattern) - 1
            while j >= 0:
                if text[i + j] != pattern[j]:
                    closest_occurence = pattern.rfind(text[i + j])
                    if closest_occurence == -1:
                        j = len(pattern) - 1
                        i += j + 1
                        break
                    elif closest_occurence >= j:
                        i += 1
                        j = len(pattern) - 1
                        break
                    else:
                        shift = j - closest_occurence
                        i += shift
                        j = len(pattern) -1
                        break
                j -= 1
            if j <= -1:
                return True

    return False
