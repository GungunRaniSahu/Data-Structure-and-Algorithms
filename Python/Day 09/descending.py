def bubble_sort_descending(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        # Last i elements are already sorted
        for j in range(0, n-i-1):
            if arr[j] < arr[j+1]:
                # Swap elements
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

numbers = [64, 34, 25, 12, 22, 11, 90]
sorted_numbers = bubble_sort_descending(numbers)
print("Sorted list (Descending):", sorted_numbers)
