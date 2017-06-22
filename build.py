def solution(dic1, dic2):
    """Enter Code Here"""
    for key in dic2:
        if key in dic1:
            dic1[key] = dic1[key] + dic2[key]
        else:
            dic1.update({key:dic2[key]})
    return dic1
