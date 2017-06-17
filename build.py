from collections import Counter
def solution(dic1, dic2):
    """Enter Code Here"""

    new_dic = Counter(dic1) + Counter(dic2)
    return new_dic

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(solution(d1,d2))
