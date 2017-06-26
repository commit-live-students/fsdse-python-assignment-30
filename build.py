def solution(dic1, dic2):
    d3 = {}
    for x,y in dic1.items():
        if x in dic2.keys():
            d3[x]=dic1[x]+dic2[x]
        else:
            d3[x]=dic1[x]
    for x,y in dic2.items():
        if x not in dic1.keys():
            d3[x]=dic2[x]
    print (d3)
    return d3
