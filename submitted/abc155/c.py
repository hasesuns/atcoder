import collections

n = int(input())
s = list(input() for i in range(n))


c = collections.Counter(s)

cm = c.most_common()

ans = []


max_num = cm[0][1]
for string, num in cm:
    if max_num == num:
        ans.append(string)

ans.sort()

print(*ans,sep='\n')