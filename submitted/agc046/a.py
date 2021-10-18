x = int(input())

kaiten=360
while kaiten%x!=0:
  kaiten+=360
  
print(kaiten//x)