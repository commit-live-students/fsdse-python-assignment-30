from collections import Counter
def solution(dic1, dic2):
    """Enter Code Here"""
    d = Counter(dic1) + Counter(dic2)
    return d
