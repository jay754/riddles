"""

https://projecteuler.net/problem=99

log10 is different than log(10, value) remember this

"""

import math

fileObj = file("data.txt", "r")

data = [line.strip().split(",") for line in fileObj]

line = 0
num = 0

for i in range(len(data)):
    a = int(data[i][0])
    b = int(data[i][1])
    exp = b * math.log10(a)
    if exp > num:
        line, num = i, exp

print line + 1