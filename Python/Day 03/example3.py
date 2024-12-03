#Find the Largest Number in a List
numbers = [3, 5, 7, 2, 8, 1]
largest = numbers[0]
for num in numbers:
    if num > largest:
        largest = num

print(f"The largest number is {largest}.")
