from collections import Counter
def solution(dic1, dic2):
    d = Counter(dic1) + Counter(dic2)
    return d
solution(dic1 = {'a': 100, 'b': 200, 'c':300},
         dic2 = {'a': 300, 'b': 200, 'd':400})
