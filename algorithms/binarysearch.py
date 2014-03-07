"""

http://en.wikipedia.org/wiki/Binary_search_algorithm

Finds the position of a specific element within an array

"""

def binarysearch(a, value):
    low = 0
    high = len(a) - 1

    while(low <= high):

        mid = (low + high)/2

        if a[mid] > value:
            high = mid - 1
        else:
            low = mid + 1

    return low

print binarysearch([1, 3, 4, 8, 6], 6)