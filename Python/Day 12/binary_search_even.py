#Binary Search for Lists with Even Number of Elements
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
       
        if arr[mid] == target:
            return mid
       
        elif arr[mid] > target:
            high = mid - 1
       
        else:
            low = mid + 1
    return -1


even_elements_list = [2, 4, 6, 8, 10, 12]


even_target = 8

even_result = binary_search(even_elements_list, even_target)

if even_result != -1:
    print(f"Even Target {even_target} found at index {even_result}")
else:
    print(f"Even Target {even_target} not found")
