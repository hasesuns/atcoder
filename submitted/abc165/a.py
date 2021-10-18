import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

k = int(input())
n, m = map(int, input().split())

if n%k==0:
    print('OK')
    exit()

if m%k==0:
    print('OK')
    exit()

mm= m//k
nn= n//k

if mm>nn:
    print('OK')
else:
    print('NG')