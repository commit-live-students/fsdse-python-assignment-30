def solution(dic1, dic2):
    return dict(dic1.items()+dic2.items()+[(k,dic1[k]+dic2[k]) for k in set(dic1)&set(dic2)])
