def  maxXor(l,r):
  n = 0
  for i in range(l,r+1):
    for j in range(l,r+1):
       if n < i ^ j:
         n = i ^ j
  return n

l = int(raw_input())
r = int(raw_input())

res = maxXor(l, r)
print res
