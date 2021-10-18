import collections

n = int(input())
v = list( map(int, input().split()))

v0 = v[0::2]
v1 = v[1::2]

c0 = collections.Counter(v0)
c1 = collections.Counter(v1)

ans0 = n//2 - c0.most_common()[0][1]
ans1 = n//2 - c1.most_common()[0][1]

if c0.most_common()[0][0] == c1.most_common()[0][0]:
    if len(c0.most_common()) > 1:
        ans0_1 = n//2 - c0.most_common()[1][1]
    else:
        ans0_1 = n//2

    if len(c1.most_common()) > 1:
            ans1_1 = n//2 - c1.most_common()[1][1]
    else:
        ans1_1 = n//2

    ans = min(ans0 + ans1_1, ans0_1 + ans1)
else:
    ans = ans0 + ans1

print(ans)