def solution(dic1, dic2):
    print(set(dic1) | set(dic2))
    return { k: dic1.get(k, 0) + dic2.get(k, 0) for k in set(dic1) | set(dic2) }

print(solution({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400}))

d={'a': 100, 'b': 200, 'c':300}
help(d)
