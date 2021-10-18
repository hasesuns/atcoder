N, L =  (int(j) for j in input().split())  

taste = [L+i-1 for i in range(1,N+1)]

if L > 0:
  print(sum(taste)-taste[0])
elif L + N - 1 <= 0:
  print(sum(taste)-taste[N-1])
else:
  print(sum(taste))