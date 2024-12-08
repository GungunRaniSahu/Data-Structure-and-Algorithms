set1 = {1, 2, 3, 4}
set1.remove(2)  # Removes 2, throws an error if not found
print(set1)  # Output: {1, 3, 4, 5}

set1.discard(6)  # Safely removes 6, no error if not found
print(set1)  # Output: {1, 3, 4, 5}
