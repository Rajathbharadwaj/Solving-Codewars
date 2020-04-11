def create_phone_number(n):
    st = '('
    for  v in n[:4]:
        if len(st)<4:
            st=st+str(v)
    st = st +')'+ " "
    for  i in n[3:]:
        if len(st)>5 and len(st)<9:
            st = st+str(i)
    st = st+'-'
    for i in n[6:]:
        st =st+str(i)
    return st
