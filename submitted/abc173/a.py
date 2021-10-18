import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n = int(input())

tmp = -(-n//1000)

print(tmp*1000-n)