from math import gcd


a, b = map(int, input().split())
lcm = a // gcd(a, b) * b
print(lcm) if lcm <= 10**18 else print("Large")