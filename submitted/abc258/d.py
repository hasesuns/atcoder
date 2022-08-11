import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, x = map(int, input().split())
ab = [tuple(map(int, input().split())) for _ in range(n)]

def dfs(stage, nokori, time):
    if nokori < 0:
        return float("inf")
    if stage < n - 1:
        return min(
            dfs(stage + 1, nokori - 1, time + ab[stage][0] + ab[stage][1]),
            time + ab[stage][0] + ab[stage][1] * nokori
            )
    else:
        return time + ab[stage][0] + ab[stage][1] * nokori


ans = dfs(0, x, 0)

print(ans)