from collections import Counter

def solution(dic1, dic2):
    """
    There can be different ways to do this but counter is the prefered one
    Here this will help you to check the value and return keys
    That can you can use for value sum
    """
    check_counter = Counter(dic1) + Counter(dic2)
    print check_counter
    return check_counter

solution({'a': 100, 'b': 200, 'c':300},{'a': 300, 'b': 200, 'd':400})
