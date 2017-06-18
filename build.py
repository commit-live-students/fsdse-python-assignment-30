"""Example:

Input

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}

Output

{'b': 400, 'd': 400, 'a': 400, 'c': 300}"""
from collections import Counter
def solution(dic1, dic2):
    d = 0
    d = Counter(dic1) + Counter(dic2)
    return d
