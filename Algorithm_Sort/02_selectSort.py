# ????0~n-1?????????????????0??
# ???1~n-1????????????1??
# ??????????????????????
def select_sort(array):
    n = len(array)
    for i in range(n-1):
        min_index = i  # Assume the minimum is the first element
        for j in range(i+1, n):
            if array[min_index] > array[j]:
                min_index = j  # Update the index of the minimum element

        if min_index != i:
            # Swap the found minimum element with the first element of the unsorted part
            array[i], array[min_index] = array[min_index], array[i]

# Example usage:
arr = [64, 25, 12, 22, 11]
select_sort(arr)
print("Sorted array is:", arr)