def max_sep(i, arr, k):
    # Base case 1: If we've reached the end of the array
    if i == len(arr):
        return 0
    
    # Base case 2: If no valid pairs left that meet the separation condition
    valid_pair_found = any(abs(arr[i] - arr[j]) >= k for j in range(i + 1, len(arr)))
    if not valid_pair_found:
        return 0
    
    # Base case 3: If only one element remains (no pairs possible)
    if i == len(arr) - 1:
        return 0
    
    max_distance = 0
    
    # Recursive exploration of valid pairs
    for j in range(i + 1, len(arr)):
        # Calculate the difference
        pair = arr[j] - arr[i]
        
        # If the difference meets the condition, proceed with recursion
        if pair >= k:
            # Recursive call from the next index `j`, and track the max distance
            max_distance = max(max_distance, pair + max_sep(j, arr, k))
    
    return max_distance

# Example usage
arr = [1, 2, 5, 10, 5, 15]
K = 4
result = max_sep(0, arr, K)
print("Maximum separation:", result)
