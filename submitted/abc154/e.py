from functools import lru_cache

N = int(input())
K = int(input())

@lru_cache(None)
def rec(n, k):
    if k == 0:
        return 1
    if n < 10:
        if k == 1:
            return n
        else:
            return 0


    m,d = divmod(n,10)

    ret = 0
    ret += d * rec(m,k-1) # 最後の桁は1~dの数字。それより上は再帰
    ret += (9-d)*rec(m-1,k-1) # 最後の桁は(d+1)~9，N以下を守るため最後から2番目の桁から1引く
    ret += rec(m,k) # 最後の桁は0，それより上は再帰

    return ret

print(rec(N,K))