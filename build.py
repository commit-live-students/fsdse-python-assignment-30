def solution(dic1, dic2):
    """Enter Code Here"""
    b = {}
    dic3 = dic1
    for k1, v1 in dic1.iteritems():
        for  k2, v2 in dic2.iteritems():
            if  k1 == k2:
                v = v1 + v2
                b[k1] = v

    dic3.update(dic2)
    dic3.update(b)
    return dic3



'''
dic1 = {1:12, 2:23,3: 33, 4: 12}
dic2 = {2: 31, 4: 43}
a = solution(dic1, dic2)
print a
'''
