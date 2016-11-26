import sys

n = long(raw_input().strip())

b = bin(n)[2:].count("0")

if b:
    print 2**b
else:
    print 1
