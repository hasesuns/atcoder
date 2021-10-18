import math
a, b, x = map(int, input().split())

if 0 <= 2*x/a/a - b <= b:
    b_ =  2*x/a/a - b
    ans = 90 - math.degrees(math.atan2(a, b - b_) )
elif 0 <= 2*x/a/b <= a:
    a_ = 2*x/a/b
    ans = 90 - math.degrees(math.atan2(a_, b ) )

print(ans)