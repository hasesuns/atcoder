import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline

t = int(input())
as_list = [tuple(map(int,input().split())) for _ in range(t)]
ans_list = []

for a, s in as_list:
    target = s - 2 * a
    if target < 0:
        ans_list.append("No")
        continue

    used_list = []
    for index, is_used in enumerate(reversed(bin(a)[2:])):
        if is_used == "1":
            used_list.append(index)

    for index, is_used in enumerate(reversed(bin(target)[2:])):
        if is_used == "1" and index in used_list:
            ans_list.append("No")
            break
    else:
        ans_list.append("Yes")

print(*ans_list, sep='\n')