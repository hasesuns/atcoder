S = input()
ans = 0

for i in range(3):
  if S[i] == S[i+1]:
  	ans = 1
    
if ans == 1:
  print('Bad')
else:
  print('Good')