import sys
from collections import Counter

n = int(raw_input().strip())
c = map(int,raw_input().strip().split(' '))
a = Counter(c)
count = 0

for i in a.values():
    for j in range(1,i+1):
        if j % 2 == 0:
            count += 1

print count
