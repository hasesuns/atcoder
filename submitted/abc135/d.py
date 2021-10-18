s = input()
invs = s[::-1] # 逆向きの方がdpとの対応的にしっくりくるんやけど 

MOD = 10 ** 9 + 7
 
dp = [[0]*13 for _ in range(len(s))] #dp[桁][あまり] 

if invs[0]=='?':
    for i in range(10): # 0~9までは1 10~12は0のまま
        dp[0][i] = 1
else:
    dp[0][int(invs[0])] = 1

mul = 10 # 桁数のための変数 mul = 10 ** order
for order in range(1,len(s)):
    for j in range(13):
        if invs[order] == '?':
            for number in range(10):
                dp[order][ (j+number * mul )%13  ]  += dp[order-1][j]%MOD #いわゆる貰うdpで書いた
        else:
            number = int(invs[order])
            dp[order][(j+number * mul )%13 ]  += dp[order-1][j]%MOD
        dp[order][(j+number * mul )%13 ] %= MOD
    mul *= 10
    mul %= 13
print(dp[-1][5]%MOD)

# dpは基本的にpythonだと通らないからpypy3で提出するのを忘れないようにしよう...