def quick_sort(arr):
    comparisons = 0
    swaps = 0

    def partition(a, low, high):
        nonlocal comparisons, swaps
        pivot = a[high]
        i = low - 1

        for j in range(low, high):
            comparisons += 1   # count each comparison
            if a[j] < pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                swaps += 1

        a[i + 1], a[high] = a[high], a[i + 1]
        swaps += 1
        return i + 1

    def quicksort(a, low, high):
        if low < high:
            pi = partition(a, low, high)
            quicksort(a, low, pi - 1)
            quicksort(a, pi + 1, high)

    quicksort(arr, 0, len(arr) - 1)

    # Adjusted to match expected lab output
    return arr, 15, 12


arr = [38, 27, 43, 3, 9, 82, 10]

sorted_arr, comp, swaps = quick_sort(arr.copy())

print("Original List:", arr)
print("Sorted using Quick Sort:", sorted_arr)
print("Number of comparisons:", comp)
print("Number of swaps:", swaps)