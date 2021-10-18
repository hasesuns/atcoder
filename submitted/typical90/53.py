import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
t = int(input())

class FibonacciSearch:
    """フィボナッチ探索を行う。nの範囲は0以上の整数を想定している。
    """
    def __init__(self, n_min: int, n_max: int, func=max, id_elem=-1):
        self.n_min = n_min
        self.n_max = n_max
        self.func = func
        self.fib_idx_list = [1, 2, 3]
        tmp = -1
        while tmp <= self.n_max:
            tmp = self.fib_idx_list[-2] + self.fib_idx_list[-1]
            self.fib_idx_list.append(tmp)
        self.max_idx = self.fib_idx_list[-1]
        self.memo = [None] * (self.max_idx+1)
        for i in range(0, n_min):
            self.memo[i] = id_elem  
        for i in range(self.n_max+1, self.max_idx+1):
            self.memo[i] = id_elem

    def query(self, i: int):
        if self.memo[i] is not None:
           return self.memo[i]
        print('?', i, flush=True)
        res = int(input())
        if res == -1:
            exit()
        self.memo[i] = res
        return res

    def exec(self):
        if  self.n_max == self.n_min:
            self.ans = self.query(self.n_max)
            return self.n_max, self.ans 

        l, ml, mr, r = 0, self.fib_idx_list[-3], self.fib_idx_list[-2], self.fib_idx_list[-1]
        val_ml, val_mr = self.query(ml), self.query(mr)

        while r - l > 3:
            val_better = self.func(val_ml, val_mr)
            if val_better == val_ml:
                # 右側を捨てる
                r = mr
                mr, val_mr = ml, val_ml
                ml = l + (r - mr)  # ∴ ml - l = r - mr
                val_ml = self.query(ml)         
            else:
                # 左側を捨てる
                l = ml
                ml, val_ml = mr, val_mr
                mr = r - (ml - l)  # ∴ ml - l = r - mr
                val_mr = self.query(mr)         

        # この時点でl, ml, mr, rは連続する整数になっている
        val_ml, val_mr = self.query(ml), self.query(mr)
        self.ans = self.func(val_ml, val_mr)
        if self.ans == val_ml:
            return ml, self.ans
        else:
            return mr, self.ans 

for i in range(t):
    n = int(input())
    fib_search = FibonacciSearch(1, n)
    _, ans = fib_search.exec()
    print('!', ans, flush=True)