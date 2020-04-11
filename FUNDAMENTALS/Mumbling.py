def accum(s):
    acum = []
    s = s.split()[0].capitalize()
    for index, val in enumerate(s):
        for i in range(index+1):
            acum.append(val)
        acum.append("-")
    for i,v  in enumerate(acum[:-1]):
        if v == '-':
            acum[i+1] = acum[i+1].upper()
    acum = "".join(acum[:-1])
    return acum
