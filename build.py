def solution(dic1, dic2):
    d={}

    for k,v in dic1.items() :
        for k2,v2 in dic2.items():
            d[k]=v+dic2.get(k,0)
            d[k2]=v2+dic1.get(k2,0)
    return d
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print solution(d1,d2)
