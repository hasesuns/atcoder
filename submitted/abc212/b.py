n = input()

if len(set(n)) == 1:
    print("Weak")
    exit()

for i in range(3):
    if (int(n[i]) + 1)% 10 != int(n[i+1]):
        print("Strong")
        exit()

print("Weak")