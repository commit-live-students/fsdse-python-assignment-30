def solution(dic1, dic2):
    from collections import Counter
    d = Counter(dic1) + Counter(dic2)
    return(d)

print solution({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})
