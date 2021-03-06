import numpy as np

x = int(input())

def sieve(n):
    is_prime = [True for _ in range(n+1)]
    is_prime[0] = False

    for i in range(2, n+1):
        if is_prime[i-1]:
            j = 2 * i
            while j <= n:
                is_prime[j-1] = False
                j += i
    table = [ i for i in range(1, n+1) if is_prime[i-1]]
    return table

sosu_table = sieve(100000)
sosu_table.append(100003)

sosu_table = np.array(sosu_table)

print(sosu_table[x<=sosu_table][0])