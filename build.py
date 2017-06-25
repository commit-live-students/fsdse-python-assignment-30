def solution(dic1, dic2):
    """Enter Code Here"""
    common_key_values_addition = {x:dic1.get(x,0)+dic2.get(x,0) for x in set(dic1).union(dic2)}
    return common_key_values_addition
