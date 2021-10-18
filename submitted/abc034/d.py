import numpy as np
n,k = map(int, input().split())

w = np.array([0]* n)
p = np.array([0]* n)
for i in range(n):
    w[i], p[i] = map(int, input().split())

w = np.array(w)
p = np.array(p)

max_p_index = np.argmax(p)

ans = p[max_p_index]
volume = w[max_p_index]
w[max_p_index] = 10**9
p[max_p_index]=0



for i in range(k-1):
    next_p = (volume*ans + p*w)/(volume+w)
    max_next_p_index = np.argmax(next_p)

    volume = volume + w[max_next_p_index]
    ans = next_p[max_next_p_index]
    w[max_next_p_index] = 10**9
    p[max_next_p_index] = 0

print(ans)
 