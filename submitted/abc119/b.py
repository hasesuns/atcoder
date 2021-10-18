from sys import stdin

n= int(stdin.readline().rstrip())
S = 0
for i in range(n):
  n = stdin.readline().rstrip().split()
  if n[1] == "JPY":
    S += int(n[0])
  else:
    S += float(n[0])*380000.0
    
print(S)
      