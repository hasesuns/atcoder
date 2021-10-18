import fractions
a,b=map(int, input().split())
n = fractions.gcd(a,b)


def divisor(n):
    ass = []
    for i in range(1,int(n**0.5)+1):
        if n%i == 0:
            ass.append(i)
            ass.append(n//i)
    return ass

def is_prime(n):
    if n == 1:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True


divs = divisor(n)
ans = 0

for d in divs:
    ans += is_prime(d)


print(ans+1)