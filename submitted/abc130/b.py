N,X=map(int, input().split()) 
L=list(map(int, input().split())) 
D = 0
for i in range(N):
  D = D + L[i]
  if D > X:
    print(i+1)
    break
  if D == X:
    print(i+2)
    break
  if D < X and i == N-1:
    print(i+2)
    break
  
 