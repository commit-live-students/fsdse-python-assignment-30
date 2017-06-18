def solution(dic1, dic2):
    """Enter Code Here"""
    for x in dic1.keys():
        if x in dic2.keys():
            dic1[x] = dic1[x] + dic2[x]
        else:
            pass
    for x in dic2.keys():
        if x in dic1.keys():
            pass
        else:
            dic1[x] = dic2[x]
    return dic1
