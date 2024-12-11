#Linear Search for a Target Not Present in the List
# Example List and Target
numbers = [5, 8, 2, 9, 10, 12]
target = 7

# Performing Linear Search
result = linear_search(numbers, target)

# Output Result
if result != -1:
    print(f"Target {target} found at index {result}.")
else:
    print(f"Target {target} not found in the list.")
