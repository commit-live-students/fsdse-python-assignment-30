def solution(dic1, dic2):
    keys = dic1.keys() + dic2.keys()
    dic3 = dict()
    for key in keys:
        if key in dic1.keys() and key in dic2.keys():
            dic3[key] = dic1[key] + dic2[key]
        elif key in dic1.keys():
            dic3[key] = dic1[key]
        elif key in dic2.keys():
            dic3[key] = dic2[key]
    return dic3

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print solution(d1,d2)
