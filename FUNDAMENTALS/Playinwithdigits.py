def dig_pow(n, p):
    num = str(n)
    lst = 0
    for i, v in enumerate(range(len(num))):
        lst = lst+int(num[i])**p
        p = p+1
    val = lst/int(num)
    return [val if lst % int(num) == 0 else -1][0]
