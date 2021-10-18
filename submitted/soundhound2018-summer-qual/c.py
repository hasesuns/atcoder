n, m, d = map(int, input().split())
ans =0
if d!=0:
    ans = (m-1)*(n-d)*2*n**(-2)
else:
    ans = (m-1)*(n-d)*n**(-2)

print(ans)