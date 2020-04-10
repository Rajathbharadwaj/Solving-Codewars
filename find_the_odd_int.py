def find_it(seq):
    dict = {}
    
    for val in seq:
        if val in dict.keys():
            
            dict[val] = dict[val]+1
        else:
            dict[val] = 1
    answer = []
    for i, v in enumerate(dict.values()):
        if v % 2 != 0:
            answer.append(list(dict)[i])
        else:
            pass
    return answer[0]
