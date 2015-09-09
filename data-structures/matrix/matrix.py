m = [[1,2,3],
     [4,5,6],
     [7,8,9]]

tmp = 0

def transpose(m):
    b = [[x for x in range(len(m))] for y in range(len(m))]

    for i in range(len(m)):
        for j in range(len(m)):
            b[i][j] = m[j][i]

    return b

def rotate90(m):
    transposed_m = transpose(m)
    for i in range(len(transposed_m)):
        tmp = transposed_m[i][0]
        transposed_m[i][0] = transposed_m[i][2]
        transposed_m[i][2] = tmp

    return transposed_m

def rotate180(m):
    # broken
    transposed_m1 = transpose(m)
    transposed_m2 = zip(*transposed_m1[::-1])
    print transposed_m2

# print b
