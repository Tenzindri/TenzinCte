# Task 1 & 2: Selection Sort with Comparison and Swap Counters
def selection_sort(arr):
    n = len(arr)
    comparisons = 0
    swaps = 0
    
    print(f"Original list: {arr}")
    
    for i in range(n - 1):
        # Find the index of the minimum element in the unsorted part
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        if min_idx != i:
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
            swaps += 1
            
        print(f"Pass {i+1}: {arr}")
        
    print(f"Sorted list: {arr}")
    print(f"Total comparisons: {comparisons}")
    print(f"Total swaps: {swaps}")
    return arr

arr_to_sort = [29, 10, 14, 37, 13]
sorted_list = selection_sort(arr_to_sort)
