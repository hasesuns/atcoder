n,m,v,p = map(int, input().split())
a = list( map(int, input().split()))

a.sort(reverse=True)

def isok(i):

    if i <= (p-1):
        return True

    points = a.copy()

    points[i] += m

    adding_point = m*v-m*p

    if points[i] < points[p-1]:
        return False

    j = n-1
    while adding_point > 0:

        if j <= p-2:
            return False

        if i == j:
            j -= 1
            continue
        adding_point -= min(m, points[i]- points[j])

        j -= 1

    return True

if isok(n-1):
    print(n)
    exit()

ok = p-1
ng = n-1

while ng - ok > 1:
    mid = (ok+ng)//2

    if isok(mid):
        ok = mid
    else:
        ng = mid
print(ok+1)
 