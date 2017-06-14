from collections import Counter
def solution(dic1, dic2):
    """Enter Code Here"""
    d = Counter(dic1) + Counter(dic2)
    return d

solution({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})
