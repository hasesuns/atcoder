from heapq import heappop, heappush
from operator import itemgetter


def branchAndBound(N: int, M: int, V: list, W: list, R: list) -> int:
    def upperbound(w, v, i):
        #i番目の荷物まで選択済み。i+1番目から順番に取っていく。
        #vは価値の最大値の目安。_vは緩和問題の解（上界）に相当。
        rest = M - w
        _v = v
        for j in range(i + 1, N):
            if W[j] >= rest:
                rest -= W[j]
                v += V[j]
                _v = v
            else:
                _v += R[j] * rest
                break
        return v, _v

    prov, tmp = upperbound(0, 0, -1) #provは暫定解
    h = [(tmp, W[0], V[0] * (W[0] >= M), 0), (upperbound(0, 0, 0)[1], 0, 0, 0)]
    #上界が大きい順に確かめる。
    while h:
        _v, w, v, cur = heappop(h)
        if _v > prov or cur == N - 1:
            #-上界>暫定解(枝刈り)あるいは荷物の選択が完了したとき
            continue
        nxtw, nxtv = w + W[cur + 1], v + V[cur + 1]
        if nxtw >= M:
            #次の荷物を入れる場合
            heappush(h, (_v, nxtw, nxtv, cur + 1))
        _prov, ub = upperbound(w, v, cur)
        if _prov < prov:
            #暫定解を更新
            prov = _prov
        if ub < prov:
            #次の荷物を入れない場合
            heappush(h, (ub, w, v, cur + 1))
    return -prov


import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

N, W = map(int, input().split())
t=[0]*N
for i in range(N):
    v, w = map(int, input().split())
    t[i]=(v, w, v / w) # 整数計画問題から線形計画問題に緩和（線形緩和）したい
t.sort(key=itemgetter(2), reverse=True) #価値/重さが大きい順にソート
vlist, wlist, rlist = [], [], []
for v, w, r in t:
    vlist += [-v] #符号を反転している点に注意
    wlist += [-w]
    rlist += [r]
ans = branchAndBound(N, -W, vlist, wlist, rlist)
print(ans)
 