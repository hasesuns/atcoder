n = int(input())
v = list( map(int, input().split())) 

v_ = sorted(v)

ans = v_[0]/(2**(n-1))
for i in range(1,n):
    ans += v_[i]/(2**(n-i))  

print(ans)