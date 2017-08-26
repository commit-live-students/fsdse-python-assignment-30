def solution(dic1, dic2):
    for i in dic2:
        if i in dic1:
            dic1[i] = dic1[i] + dic2[i]
            #print d1[i]
    return dict(d2, **d1)

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
solution(d1,d2)
