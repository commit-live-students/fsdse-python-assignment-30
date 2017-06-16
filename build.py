def solution(dic1, dic2):
    dic1_keys=dic1.keys()
    dic2_keys=dic2.keys()
    ans={}
    for i in range(0,len(dic1)):
        if(dic1_keys[i] in dic2_keys):
            ans[dic1_keys[i]] = dic1.get(dic1_keys[i]) + dic2.get(dic1_keys[i])
        else:
            ans[dic1_keys[i]] = dic1.get(dic1_keys[i])
    for i in range(0,len(dic2)):
        if(dic2_keys[i] not in dic1_keys):
            ans[dic2_keys[i]] = dic2.get(dic2_keys[i])
    return ans
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print solution(d1,d2)
