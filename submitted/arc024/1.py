import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

L, R = map(int, input().split())
l = list( map(int, input().split()))
r = list( map(int, input().split()))

def intersect_list(lst1, lst2):
    arr = []
    lst = lst1.copy()
    for element in lst2:
        try:
            lst.remove(element)
        except ValueError:
            pass
        else:
            arr.append(element)
    return arr


print(len(intersect_list(l,r)))