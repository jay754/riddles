"""

http://www.reddit.com/r/dailyprogrammer/comments/1kphtf/081313_challenge_136_easy_student_management/

"""

fileObj = file("easy136.txt", "r")

stats = []

for i in fileObj.readlines():
	line = i.split()
	averages = round(sum(map(float, line[1:]))/len(line[1:]), 3)
	stats.append([line[0], averages])

for i in range(len(stats)):
	print "student Name: " + str(stats[i][0]) +  " , " + "student Average: " + str(stats[i][1])
