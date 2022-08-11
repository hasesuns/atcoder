# Ref: https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, List, TypeVar, Union

T = TypeVar("T")


class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> List[List[T]]:
        "Evenly divide `a` into buckets."
        if a is None:
            a = list(self)
        bucket_size = int(math.ceil(math.sqrt(self.size / self.BUCKET_RATIO)))
        return [a[self.size * i // bucket_size : self.size * (i + 1) // bucket_size] for i in range(bucket_size)]

    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self.size = len(a)
        self.bucket_list = self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.bucket_list:
            for j in i:
                yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.bucket_list):
            for j in reversed(i):
                yield j

    def __len__(self) -> int:
        return self.size

    def __repr__(self) -> str:
        return "SortedSet" + str(self.bucket_list)

    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for bucket in self.bucket_list:
            if x <= bucket[-1]:
                return bucket
        return self.bucket_list[-1]

    def __contains__(self, x: T) -> bool:
        if self.size == 0:
            return False
        bucket = self._find_bucket(x)
        i = bisect_left(bucket, x)
        return i != len(bucket) and bucket[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.bucket_list = [[x]]
            self.size = 1
            return True
        bucket = self._find_bucket(x)
        i = bisect_left(bucket, x)
        if i != len(bucket) and bucket[i] == x:
            return False
        bucket.insert(i, x)
        self.size += 1
        if len(bucket) > len(self.bucket_list) * self.REBUILD_RATIO:
            self.bucket_list = self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0:
            return False
        bucket = self._find_bucket(x)
        i = bisect_left(bucket, x)
        if i == len(bucket) or bucket[i] != x:
            return False
        bucket.pop(i)
        self.size -= 1
        if len(bucket) == 0:
            self.bucket_list = self._build()
        return True

    def lt(self, x: T) -> Union[T, None]:
        "Find the largest element < x, or None if it doesn't exist."
        for bucket in reversed(self.bucket_list):
            if bucket[0] < x:
                return bucket[bisect_left(bucket, x) - 1]

    def le(self, x: T) -> Union[T, None]:
        "Find the largest element <= x, or None if it doesn't exist."
        for bucket in reversed(self.bucket_list):
            if bucket[0] <= x:
                return bucket[bisect_right(bucket, x) - 1]

    def gt(self, x: T) -> Union[T, None]:
        "Find the smallest element > x, or None if it doesn't exist."
        for bucket in self.bucket_list:
            if bucket[-1] > x:
                return bucket[bisect_right(bucket, x)]

    def ge(self, x: T) -> Union[T, None]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for bucket in self.bucket_list:
            if bucket[-1] >= x:
                return bucket[bisect_left(bucket, x)]

    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0:
            x += self.size
        if x < 0:
            raise IndexError
        for bucket in self.bucket_list:
            if x < len(bucket):
                return bucket[x]
            x -= len(bucket)
        raise IndexError

    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for bucket in self.bucket_list:
            if bucket[-1] >= x:
                return ans + bisect_left(bucket, x)
            ans += len(bucket)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for bucket in self.bucket_list:
            if bucket[-1] > x:
                return ans + bisect_right(bucket, x)
            ans += len(bucket)
        return ans


import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

n, k = map(int, input().split())
p = list(map(int, input().split()))

ans = [-1] * n
from collections import defaultdict

yama = defaultdict(list)

s = SortedSet()
for i, x in enumerate(p):
    key = s.ge(x)
    if key is not None:
        yama[x] = yama.pop(key)
        s.discard(key)
    yama[x].append(x)
    res = s.add(x)
    if len(yama[x]) == k:
        for y in yama.pop(x):
            ans[y - 1] = i + 1
        s.discard(x)
print(*ans, sep="\n")