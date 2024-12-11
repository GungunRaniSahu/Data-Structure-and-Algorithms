#Linear Search for a Target Present in the List
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index  # Return the index of the found element
    return -1  # Return -1 if the target is not found

# Example List and Target
numbers = [5, 8, 2, 9, 10, 12]
target = 9

# Performing Linear Search
result = linear_search(numbers, target)

# Output Result
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
