dic1={'a': 100, 'b': 200, 'c':300}
dic2={'a': 300, 'b': 200, 'd':400}
def solution(dic1, dic2):
    for key in dic1:
        if key in dic2:
            dic1[key]=dic1[key]+dic2[key]
        else:
            pass
    for key in dic2:
        if key not in dic1:
            dic1[key]=dic2[key]
    return dic1
solution(dic1, dic2)
