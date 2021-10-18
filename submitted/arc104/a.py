import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, m = map(int, input().split())

a = (n+m)/2
b = (n-m)/2

print(int(a),int(b))