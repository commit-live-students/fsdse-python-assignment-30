def solution(dic1, dic2):
    output = {}
    for k, v in dic1.items():
        output[k] = v

    for k, v in dic2.items():
        if k in output:
            output[k] = output[k] + v
        else:
            output[k] = v

    return output
