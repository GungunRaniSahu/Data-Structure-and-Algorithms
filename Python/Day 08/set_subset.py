set1 = {1, 2, 3, 4}
set2 = set([3, 4, 5, 6])
subset = {3, 4}
print(subset.issubset(set2))  # Output: True
print(set2.issuperset(subset))  # Output: True
