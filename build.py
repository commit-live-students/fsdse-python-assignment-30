from collections import Counter

def solution(dic1, dic2):
    """Enter Code Here"""
    a = Counter(dic1)
    b = Counter(dic2)
    c = dict(a+b)
    return c










d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

print solution(d1,d2)
