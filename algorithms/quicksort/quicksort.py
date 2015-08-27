# full credit to http://www.pythonschool.net/data-structures-algorithms/quicksort/

# the leftmark has to be greater than the pivot and the right has to be less than the pivot in order for an swap to occur
# once that step is complete than you exchange the left and right, hence the swap

# the final partition comes when you find the leftmarks that is greater than pivot
# and the right marks that is less than the pivot. Than you exhange the pivot with the rightmarks position
# finally you partition at the pivot and that will create 2 different sides. Than you repeat the steps on 2 separate arrays
# through recurison until they are sorted

# sidenote a pivot can be any element, but its much easier to pick the starting element

def quicksort(myList, start, end):
    if start < end:
        # partition the list
        pivot = part(myList, start, end)
        # sort both halves
        quicksort(myList, start, pivot-1)
        quicksort(myList, pivot+1, end)

    return myList

def part(myList, start, end):
    pivot = myList[start]
    left = start+1
    right = end
    done = False

    while not done:
        # once the right becomes less than pivot it stops else you keep decreasing the right
        while myList[right] >= pivot and right >= left:
            right = right - 1
        # once the left becomes greater than the pivot it stops else you keep increasing the left
        while myList[left] <= pivot and right >= left:
            left = left + 1
        if right < left:
            done= True
        else:
            # swap places
            temp=myList[left]
            myList[left]=myList[right]
            myList[right]=temp
    # swap start with myList[right]
    temp=myList[start]
    myList[start]=myList[right]
    myList[right]=temp
    return right

alist = [54,26,93,17,77,31,44,55,20]

print quicksort(alist,0,len(alist)-1)
