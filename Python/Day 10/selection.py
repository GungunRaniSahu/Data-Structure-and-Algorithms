def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the smallest element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

numbers = [64, 25, 12, 22, 11]
print("Original List:", numbers)
selection_sort(numbers)
print("Sorted List:", numbers)
