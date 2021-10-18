n = int(input())

def eratosthenes(n):
    import math
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]
    return data

sosu = eratosthenes(55555)
ans = [i for i in sosu if i%5==1]

print(*ans[:n],sep=' ')