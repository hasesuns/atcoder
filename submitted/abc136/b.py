import numpy as np
n = int(input())
m = int(np.log10(n))
ans = 0

for i in range(m+1):
    if m%2 == 1:
        n = 10**m - 1
        m -= 1
    else:
        ans += n - 10**m + 1 
        n = 10**m - 1
        m -= 1

print(ans)