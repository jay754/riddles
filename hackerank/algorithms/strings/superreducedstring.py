def reducedstring(s):
    count = 0
    a = list(s)
    while len(a) > count:
        if len(a) == 0:
            return "Empty String"

        if a[count] == a[count+1]:
            del a[count]
            del a[count]
            print a
            count = 0
        else:
            count += 1

    return "".join(a)
