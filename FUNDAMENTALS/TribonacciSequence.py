from collections import deque

def tribonacci(signature, n):
    signature = deque(signature, maxlen = n)
    [signature.insert((i+3),  (signature[i] + signature[i+1] + signature[i+2])) for i in range(n) if len(signature)!=n]
    return list(signature)
