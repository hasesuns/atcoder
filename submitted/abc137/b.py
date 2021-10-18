k, x = map(int, input().split())
start = x-k+1
end = x+k-1
ans =  list(range(start,end+1))
print(*ans)