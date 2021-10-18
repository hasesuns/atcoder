import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

a, b,c = map(int, input().split())
abc = [a,b,c]

print(len(set(abc)))