import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

x = int(input())

h1000 = x//500
x -= h1000*500

h5 = x//5

print(h1000*1000+h5*5)