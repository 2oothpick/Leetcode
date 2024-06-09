strs = ["cir","car"]
newStr = ''

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    newStr = ''
    if (len(strs) > 2):
        for idx in range(len(strs)):
            for item in strs[idx]:
                if (idx != len(strs)-1):
                    for item1 in strs[idx+1]:
                        if (idx != len(strs)-2):
                            for item2 in strs[idx+2]:
                                if (item == item1 and item == item2):
                                    newStr += item
    elif (len(strs) == 2):
        for idx in range(len(strs)):
            for item in strs[idx]:
                if (idx != len(strs)-1):
                    for item1 in strs[idx+1]:
                        if (item == item1):
                                    newStr += item
    else:
        newStr = strs[0]
    return newStr

print(longestCommonPrefix(strs))