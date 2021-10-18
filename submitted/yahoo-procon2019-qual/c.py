k,a,b = map(int, input().split())
ans = 1+k
if b-a<=2:
    print(ans)
    exit()

ans = max(ans,(k-(a-1))//2*(b-a)+(k-(a-1))%2+a)

print(ans)