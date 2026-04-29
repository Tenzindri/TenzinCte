def merge_sort(arr):
    # Base case: tracking variables
    stats = {"comparisons": 0, "accesses": 0}

    def sort_recursive(data):
        # Edge case: if list is empty or has one element
        if len(data) <= 1:
            return data

        mid = len(data) // 2
        
        # Note: Slicing in Python technically accesses every element.
        # However, in most academic contexts, we count manual indexing.
        left_half = sort_recursive(data[:mid])
        right_half = sort_recursive(data[mid:])

        return merge(left_half, right_half)

    def merge(left, right):
        merged = []
        i = j = 0

        while i < len(left) and j < len(right):
            stats["comparisons"] += 1
            # Accessing left[i] and right[j]
            stats["accesses"] += 2
            
            if left[i] <= right[j]:
                merged.append(left[i])
                stats["accesses"] += 1 # Read from left
                i += 1
            else:
                merged.append(right[j])
                stats["accesses"] += 1 # Read from right
                j += 1

        # Collect remaining elements
        while i < len(left):
            merged.append(left[i])
            stats["accesses"] += 1
            i += 1

        while j < len(right):
            merged.append(right[j])
            stats["accesses"] += 1
            j += 1

        return merged

    sorted_list = sort_recursive(arr)
    return sorted_list, stats["comparisons"], stats["accesses"]

# --- Testing with the Example ---
original_list = [38, 27, 43, 3, 9, 82, 10]
sorted_arr, comps, accs = merge_sort(original_list)

print(f"Original List: {original_list}")
print(f"Sorted using Merge Sort: {sorted_arr}")
print(f"Number of comparisons: {comps}")
print(f"Number of array accesses: {accs}")
