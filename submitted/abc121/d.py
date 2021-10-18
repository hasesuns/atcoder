a, b = map(int, input().split())

def xor_zero2n(n):
    remainder4 = n%4
    ret = 0
    for i in range(remainder4+1):
        ret ^= n-i
    return ret

def xor_a2b(a,b):
    return xor_zero2n(a-1)^xor_zero2n(b)

print(xor_a2b(a,b))