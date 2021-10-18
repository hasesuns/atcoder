x = int(input())

if x < 100:
    print(0)
    exit()

shimo2 = int(str(x)[-2:])
ue = int(str(x)[:-2])

nums = [0]*6

for i in [5,4,3,2,1]:
    nums[i] = shimo2//i
    shimo2 -= nums[i]*i


if ue >= sum(nums):
    print(1)
else:
    print(0)