s = input() #sys.stdin.readlineは最後が改行
from collections import Counter
c = Counter(s)
print(c.most_common()[0][0])