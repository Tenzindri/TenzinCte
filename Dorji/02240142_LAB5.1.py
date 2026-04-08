def sequential_search(arr, target):
    comparisons = 0
    
    for index in range(len(arr)):
        comparisons += 1
        if arr[index] == target:
            return index, comparisons
            
    return -1, comparisons

# --- Testing the implementation ---
data_list = [23, 45, 12, 67, 89, 34, 56]
target_value = 67

print(f"List: {data_list}")
print(f"Searching for {target_value} using Sequential Search")

found_index, num_comparisons = sequential_search(data_list, target_value)

if found_index != -1:
    print(f"Found at index {found_index}")
else:
    print("Target not found in list")

print(f"Number of comparisons: {num_comparisons}")
