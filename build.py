def solution(dic1, dic2):
    """Enter Code Here"""
    result = {}
    keys = list(set(dic1.keys() + dic2.keys()))

    for key in keys:
        temp_value = 0
        if key in dic1.keys() and key in dic2.keys():
            temp_value = temp_value + dic1[key]+dic2[key]
            result[key]=temp_value
        elif key in dic1.keys():
            temp_value += dic1[key]
            result[key]=temp_value
        elif key in dic2.keys():
            temp_value += dic2[key]
            result[key]=temp_value
        else:
            pass
    return result
