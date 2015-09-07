import random as r

def mat(height,width,k)

	n = [[False for i in range(height)] for j in range(width)]
	count = 0

	for i in range(len(n)):
    		for j in range(len(n)):
        		rand = r.uniform(0,1)
        		if rand > 0.5:
            			count += 1
            			n[i][j] = True
        		if count >= k:
            			break
