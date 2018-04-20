def boyer_moore(text, pattern):
    i = 0
    while i < len(text):
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
            return i
    return -1

print(boyer_moore('abacaabacabacababa', 'acabaca'))
