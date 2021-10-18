from math import sqrt
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N = int(input())

def solv_quadratic_equation(a, b, c):
    D2 = b**2 - 4*a*c
    if D2<0:
        return 0.1, 0.1
    D = sqrt(D2)
    x_1 = (-b + D) / (2 * a)
    x_2 = (-b - D) / (2 * a)

    return x_1, x_2

for n in range(1,N+1):
    ans=0
    if n < 6:
        print(0)
        continue
    for x in range(1,int(sqrt(n-3))+1):
        for y in range(1,int(sqrt(n-3))+1):
            z1,z2=solv_quadratic_equation(1,x+y, x**2+y**2+x*y-n)
            if z1.is_integer() and z1>=1:
                ans+=1
            if z2.is_integer() and z2>=1:
                ans+=1

    print(ans)