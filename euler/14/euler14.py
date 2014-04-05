def Collatz(n):
    count = 0

    while n > 1:
        if n % 2 == 0:
            n = n / 2
        else:
            n = n*3 + 1
        count += 1

    return count

line_num = 0
max_num = 0

for i in range(1000000):
    count = Collatz(i)
    if count > line_num:
        line_num = count
        max_num = i

print max_num, line_num