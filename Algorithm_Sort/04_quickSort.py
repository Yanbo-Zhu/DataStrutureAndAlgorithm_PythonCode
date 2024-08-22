def quicksort(a, left, right):
    if left > right:  # Recursion base case: end condition
        return

    pivotkey = a[left]  # Choose the pivot element
    i = left
    j = right

    while i < j:
        # Start searching from the right side
        while a[j] >= pivotkey and i < j:
            j -= 1
        a[i] = a[j]  # Place the smaller element to the left

        # Now search from the left side
        while a[i] <= pivotkey and i < j:
            i += 1
        a[j] = a[i]  # Place the larger element to the right

    # Place the pivot element in its correct position
    a[i] = pivotkey

    # Recursively sort the left and right parts
    quicksort(a, left, i - 1)  # Left side
    quicksort(a, i + 1, right)  # Right side

# Example usage:
arr = [64, 25, 12, 22, 11]
quicksort(arr, 0, len(arr) - 1)
print("Sorted array is:", arr)