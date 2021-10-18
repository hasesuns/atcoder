import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x,t = map(int, input().split())

kaisu = -(-n//x)
print(kaisu*t)