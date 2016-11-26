import sys

def theSum(aList):
    count = 0
    for i in aList:
       if i <= 0:
           count += 1
    return count

t = int(raw_input().strip())

for a0 in xrange(t):
    n,k = raw_input().strip().split(' ')
    n,k = int(n),int(k)
    a = map(int,raw_input().strip().split(' '))
    count = theSum(a)

    if count >= k:
        print "NO"
    elif count < k:
        print "YES"
