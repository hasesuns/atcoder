import itertools

s1 = list(input())
s2 = list(input())
s3 = list(input())

ss = set(s1+s2+s3)

def string2int(s:str, alph2int: dict):
    val = 0
    for i in range(1, len(s)+1):
        val += alph2int[s[-i]] * 10**(i-1)
        # print(val)

    return val

for c in itertools.permutations([0,1,2,3,4,5,6,7,8,9], len(ss)):
    alph2int = {}

    for i, s in enumerate(ss):
        alph2int[s] = c[i]

    if alph2int[s1[0]] == 0 or alph2int[s2[0]] == 0 or alph2int[s3[0]] == 0:
        continue

    if (alph2int[s1[-1]] + alph2int[s2[-1]]) %10 != alph2int[s3[-1]]:
        continue

    s1_int = string2int(s1, alph2int)
    s2_int = string2int(s2, alph2int)
    s3_int = string2int(s3, alph2int)

    if s1_int + s2_int == s3_int:
        print(s1_int)
        print(s2_int)
        print(s3_int)
        exit()

print("UNSOLVABLE")