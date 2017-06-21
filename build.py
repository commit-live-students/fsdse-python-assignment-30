def solution(dic1, dic2):
    dic3 = {}
    l1 = dic1.keys()
    l2 = dic2.keys()
    for e in l1:
        if e in l2:
            dic3[e] = dic1[e] + dic2[e]
        else:
            dic3[e] = dic1[e]
    for e in l2:
        if e not in l1:
            dic3[e] = dic2[e]
    return dic3 
