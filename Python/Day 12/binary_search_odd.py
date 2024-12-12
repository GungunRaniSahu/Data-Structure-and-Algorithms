#Binary Search for Lists with Odd Number of Elements
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

odd_elements_list = [1, 3, 5, 7, 9, 11, 13]

odd_target = 9

odd_result = binary_search(odd_elements_list, odd_target)

if odd_result != -1:
    print(f"Odd Target {odd_target} found at index {odd_result}")
else:
    print(f"Odd Target {odd_target} not found")
