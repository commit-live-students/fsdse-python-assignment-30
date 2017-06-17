def solution(dic1, dic2):
    dic3 = {}
    print dic3
    k1,v1 = list(zip(*dic1.items()))
    k2,v2 = list(zip(*dic2.items()))
    k1 = list(k1)
    k2 = list(k2)
    v1 = list(v1)
    v2 = list(v2)
    k1.extend(k2)
    v1.extend(v2)
    s1 = set()
    for e in k1:
        if e not in s1:
            s1.add(e)
    for key in s1:
        if key in (set(dic1.keys()).intersection(set(dic2.keys()))):
            dic3[key]=dic1[key]+dic2[key]
        elif(key in dic1.keys()):
            dic3[key]=dic1[key]
        else:
            dic3[key]=dic2[key]
    print dic3
    return dic3

solution({'a': 100, 'b': 200, 'c':300,'d':500},{'a': 300, 'b': 200, 'd':400,'e':700})
