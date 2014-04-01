def gnomesort(arr)
    i = 1
    j = 2
    while i < arr.length
        if arr[i-1] <= arr[i]
            i = j
            j = j + 1
        else
            arr[i-1], arr[i] = arr[i], arr[i-1]
            i -= 1
            if i == 0
                i = j
                j = j + 1
            end
        end
    end

    return arr
end

puts gnomesort([5,4,3])