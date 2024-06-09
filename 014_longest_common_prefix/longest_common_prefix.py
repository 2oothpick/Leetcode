strs = ["reflower","flow","flight"]
newStr = ''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    newStr = ''
    if (len(strs) > 2):
        for Aidx in range(len(strs)):
            for StrIdx in range(len(strs[Aidx])):
                if (Aidx != len(strs)-1):
                    for sndStrIdx in range(len(strs[Aidx+1])):
                        if (Aidx != len(strs)-2):
                            for thrdStrIdx in range(len(strs[Aidx+2])):
                                   if (strs[Aidx][StrIdx] == strs[Aidx+1][sndStrIdx] and strs[Aidx][StrIdx] == strs[Aidx+2][thrdStrIdx]):
                                    newStr += strs[Aidx][StrIdx]
    elif (len(strs) == 2):
        for Aidx in range(len(strs)):
            for StrIdx in range(len(strs[Aidx])):
                if (Aidx != len(strs)-1):
                    for sndStrIdx in range(len(strs[Aidx+1])):
                        if (StrIdx == sndStrIdx):
                            if (strs[Aidx][StrIdx] == strs[Aidx+1][sndStrIdx]):
                                newStr += strs[Aidx+1][Aidx]
                        else:
                            break
    else:
        newStr = strs[0]
    return newStr

print(longestCommonPrefix(strs))