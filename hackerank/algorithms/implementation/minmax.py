import sys

a,b,c,d,e = raw_input().strip().split(' ')
arr = [int(a),int(b),int(c),int(d),int(e)]

s = sum(arr)
mi, ma = sum(arr), 0

for i in arr:
    n = s - i
    if n > ma:
        ma = n
    elif n < mi:
        mi = n

print mi, ma
