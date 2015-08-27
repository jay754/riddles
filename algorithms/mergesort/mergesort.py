#http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html
# this merge is done using recursion
# what recursion will do is break the array into smaller arrays.
# for example [54,26,93,17,77,31,44,55,20] will recurvely become [54,26], [93,17], [77,31], [55,20] which are 4 subarrays

def mergesort(array):
    if len(array) > 1:
        midpoint = len(array)/2
        left = array[:midpoint]
        right = array[midpoint:]

        mergesort(right)
        mergesort(left)

        a, b, c = 0, 0, 0

        while a < len(right) and b < len(left):
            if left[a] < right[b]:
                array[c] = left[a]
                a += 1
            else:
                array[c] = right[b]
                b += 1
            c += 1

        while a < len(left):
            array[c] = left[a]
            a += 1
            c += 1

        while b < len(right):
            array[c] = right[b]
            b += 1
            c += 1

    return array

alist = [54,26,93,17,77,31,44,55,20]
print mergesort(alist)
