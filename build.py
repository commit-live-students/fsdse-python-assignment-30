from collections import Counter

def solution(dic1, dic2):
    d3 = Counter(dic1) + Counter(dic2)
    d = {}
    for key, value in d3.items():
        d[key] = value
    return d

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
solution(d1,d2)
