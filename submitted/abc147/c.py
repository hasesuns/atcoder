n = int(input())
testimony_table = [[] for _ in range(n)]

for i_witness in range(n):
    ai = int(input())
    for _ in range(ai):
        xij, yij= map(int, input().split())
        testimony_table[i_witness].append((xij-1,yij))

ans = 0
for i in range(2**n):
    isConflict = False

    for j_witness in range(n): # それぞれの桁について0か1かを判断したいので
        if (i >> j_witness) & 1 == 0: # j桁目が1かどうかをジャッジ
            continue


        for x_suspect, y_testimony in testimony_table[j_witness]:
            if ((i >> x_suspect) & 1) != y_testimony:
                isConflict = True
                break

        if isConflict:
            break
    if isConflict == False:
        ans = max(ans, bin(i).count("1"))

print(ans)