from collections import Counter

a = [4,4,1,2,1]

# arr = Counter(a)
#
# for k, v in arr.iteritems():
#     if v == 1:
#         print k

init = 0

for i in range(len(a)):
    init = init ^ a[i]
    print init

print init
