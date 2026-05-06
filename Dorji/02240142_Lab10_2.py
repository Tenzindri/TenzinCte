def counting_sort_for_radix(arr, exp):
    """
    A modified Counting Sort subroutine used by Radix Sort 
    to sort elements based on the digit represented by exp.
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10

    # Store count of occurrences in count[]
    for i in range(n):
        index = arr[i] // exp
        count[index % 10] += 1

    # Change count[i] so that count[i] contains actual
    # position of this digit in output[]
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array (Stable sorting)
    i = n - 1
    while i >= 0:
        index = arr[i] // exp
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1

    # Copy the output array to arr, so that arr contains sorted numbers
    for i in range(len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    """
    Part 2: Radix Sort Implementation.
    Sorts numbers digit by digit using Counting Sort as a subroutine.
    """
    if not arr:
        return arr
        
    # Find the maximum number to know number of digits
    max1 = max(arr)

    # Do counting sort for every digit. 
    # exp is 10^i where i is current digit number
    exp = 1
    while max1 // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
    
    return arr

# --- Example Usage & Testing ---
if __name__ == "__main__":
    # Test Radix Sort
    arr2 = [170, 45, 75, 90, 802, 24, 2, 66]
    print("\nRadix Sort Input:", arr2)
    print("Radix Sort Output:", radix_sort(arr2))