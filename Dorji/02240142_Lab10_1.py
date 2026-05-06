# Task 1: Implementation of Counting Sort 

def counting_sort(arr):
    """
    Part 1: Standard Counting Sort Implementation.
    Suitable for arrays where values fall within a limited range.
    """
    if not arr:
        return arr
        
    max_val = max(arr)
    min_val = min(arr)
    range_of_elements = max_val - min_val + 1
    
    count_arr = [0] * range_of_elements
    output_arr = [0] * len(arr)

    # Store the count of each element
    for i in range(len(arr)):
        count_arr[arr[i] - min_val] += 1

    # Change count_arr[i] to store actual position
    for i in range(1, len(count_arr)):
        count_arr[i] += count_arr[i - 1]

    # Build the output array
    for i in range(len(arr) - 1, -1, -1):
        output_arr[count_arr[arr[i] - min_val] - 1] = arr[i]
        count_arr[arr[i] - min_val] -= 1

    return output_arr


# --- Example Usage & Testing ---
if __name__ == "__main__":
    # Test Counting Sort
    arr1 = [4, 2, 2, 8, 3, 3, 1]
    print("Counting Sort Input:", arr1)
    print("Counting Sort Output:", counting_sort(arr1))

