n = int(input())
a = list( map(int, input().split())) 

bunbo = 0
for i in range(n):
    bunbo += float(1/a[i]) 

print(1.0/bunbo)