S = input()

A = S[0]
ans = 'No'

if A == S[1]:
    B = S[2]
    if B == S[3]:
        ans = 'Yes'
else:
    B = S[1]
    if A == S[2] and B == S[3]:
        ans = 'Yes'
    if B == S[2] and A == S[3]:
        ans = 'Yes'

if A == B:
    ans = 'No'

print(ans)