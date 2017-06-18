def solution(dic1, dic2):
    d={}
    for k in dic1.keys():
        if k in dic2.keys():
            d[k]=dic1[k]+dic2[k]
        else:
            d[k]=dic1[k]
    for k in dic2.keys():
        if k not in dic1.keys():
            d[k]=dic2[k]
    return d
