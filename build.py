def solution(dic1, dic2):
    for key in dic1.keys():
        if key in dic2.keys():
            dic2[key] += dic1[key]
        elif key not in dic2.keys():
            dic2.update({key:dic1[key]})
    return dic2

d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
solution(d1, d2)
