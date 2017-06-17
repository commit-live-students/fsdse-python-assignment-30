from collections import Counter
def solution(dic1, dic2):
    dic1 = {'a': 100, 'b': 200, 'c':300}
    dic2 = {'a': 300, 'b': 200, 'd':400}
    dic3 = Counter(dic1) + Counter(dic2)
    return dic3
