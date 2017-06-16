"""
Input

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Output

{'b': 400, 'd': 400, 'a': 400, 'c': 300}
"""

def solution(dic1, dic2):
    """Enter Code Here"""
    dic3 = {x:dic1.get(x,0)+dic2.get(x,0) for x in set(dic1).union(dic2)}
    return dic3
