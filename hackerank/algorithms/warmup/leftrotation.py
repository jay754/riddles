import sys

def rotate(l, x):
    return l[-x:] + l[:-x]

n,k,q = raw_input().strip().split(' ')
n,k,q = [int(n),int(k),int(q)]
a = map(int,raw_input().strip().split(' '))
r = rotate(a, k)

for a0 in xrange(q):
    m = int(raw_input().strip())
    print r[m]
