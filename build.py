def solution(dic1, dic2):
    return {k: dic1.get(k, 0) + dic2.get(k, 0) for k in set(dic1) | set(dic2)}


d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}
print solution(d1, d2)
