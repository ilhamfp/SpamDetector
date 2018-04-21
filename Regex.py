import re

# regex algorithm to find string
def Regex(text, patternList):
    """
    param text : text to scan
    text type : string
    param patternList : list of spam word
    patternList type : list of string
    return : true if text contain all string in patternList, either false
    return type : boolean
    """
    ret = []
    for pattern in patternList:
        pattern = pattern.split(' ')
        tmp = [-1]
        for pat in pattern:
            matches = re.finditer(pat, text);
            for match in matches:
                if match.start() < tmp[len(tmp)-1]:
                    break
                tmp.append(match.start())
                break;
        if len(tmp) != len(pattern)+1:
            break
        else:
            ret.append(tmp[0])
    
    return len(ret) > 0
