from collections import Counter
def solution(dic1, dic2):
    """Enter Code Here"""
    a = Counter(dic1)
    b = Counter(dic2)
    return a + b
