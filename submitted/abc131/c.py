A, B, C, D =  (int(j) for j in input().split()) 
import fractions

n = B - A + 1

CD = (C*D//fractions.gcd(C,D))

if A == B:
  print(int(not( A%C==0 or A%D==0 )))
elif C != D:
  print( n- ( (B//C - (A-1)//C) + (B//D - (A-1)//D) - (B//CD - (A-1)//CD) ) )
else:
  print( n- ( (B//C - (A-1)//C) ) )
  