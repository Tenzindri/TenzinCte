def binary_search_iterative(arr, target):
    low = 0
    high = len(arr) - 1
    comparisons = 0
    
    while low <= high:
        mid = (low + high) // 2
        
        # 1st Comparison: Check for equality
        comparisons += 1
        if arr[mid] == target:
            return mid, comparisons
        
        # 2nd Comparison: Check direction (less than)
        comparisons += 1
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return -1, comparisons

def binary_search_recursive(arr, target, low, high, comparisons=0):
    if low > high:
        return -1, comparisons
    
    mid = (low + high) // 2
    
    # 1st Comparison: Equality
    comparisons += 1
    if arr[mid] == target:
        return mid, comparisons
    
    # 2nd Comparison: Direction
    comparisons += 1
    if arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high, comparisons)
    else:
        return binary_search_recursive(arr, target, low, mid - 1, comparisons)

# --- Execution ---
sorted_list = [12, 23, 34, 45, 56, 67, 89]
target = 67

print(f"Sorted List: {sorted_list}")
print(f"Searching for {target} using Binary Search")

# Test Iterative
index, total_comp = binary_search_iterative(sorted_list, target)

if index != -1:
    print(f"Found at index {index}")
    print(f"Number of comparisons: {total_comp}")
