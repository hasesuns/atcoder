import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b = map(int, input().split())
p = list( map(int, input().split()))
q = list( map(int, input().split()))


pin = ['x']*10
for pp in p:
    pin[pp-1] = '.'

for qq in q:
    pin[qq-1] = 'o'

pin[0] = '   ' + pin[0]
pin[1] = '  '+ pin[1]
pin[3] = ' '+ pin[3]
print(*pin[6:],sep=' ')
print(*pin[3:6],sep=' ')
print(*pin[1:3],sep=' ')
print(*pin[0],sep = '')