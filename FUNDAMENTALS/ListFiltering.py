def filter_list(l):
    lst = []  
    for i in l:
        if str(type(i)) == "<class 'int'>":
            lst.append(i)
        else:
            pass
    return lst
