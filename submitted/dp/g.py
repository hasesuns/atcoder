import sys
# 許容する再帰処理の回数を変更
sys.setrecursionlimit(10**5+10)
# input処理を高速化する
N, M = [int(_) for _ in input().split()]

# 隣接関係は隣接リストで管理する
lst_edge = [[] for _ in range(N)]

for _ in range(M):
  # indexを0スタートにする。
  x, y = [int(_)-1 for _ in input().split()] 
  lst_edge[x].append(y)
        
# dp[v] := ノードvを始点とした時の有向パスの長さの最大値
# -1 未訪問で初期化。
dp = [-1] * N

# メモ化再帰
def rec(v):
  # 既に更新済み
  if dp[v] != -1:
    return dp[v]
  ans = 0
  lst_nv = lst_edge[v] # ノードvからいけるノード
  for nv in lst_nv:
    ans = max(ans, rec(nv) + 1) # 一歩進む
  dp[v] = ans # ノードvを始点とした時の有向パスの長さの最大値
  return dp[v]
    
# 全ての点に対して更新する
ans = 0
for v in range(N):
  ans = max(ans, rec(v))
    
print(ans)
    