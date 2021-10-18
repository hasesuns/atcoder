n = int(input())
print(0,flush=True)

prev = input()
if prev=='Vacant': exit()
zero = prev
now=[]

def isok(ans, odd_diff):
    print(ans,flush=True)
    now = input()

    if now == 'Vacant': exit()

    if (now==zero and odd_diff)or(now!=zero and not odd_diff):
        return True
    else:
        return False

ok = n-1 #ok以前にVacantが存在
ng = 0 #ng以前にVacantは存在しない

while ok - ng > 1:
    m = (ok+ng)//2
    odd_diff = (m%2==1)
    if isok(m, odd_diff):
        ok = m
    else:
        ng = m

print(ok,flush=True)
exit()