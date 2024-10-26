def largest_in_tuple(num_tuple):
    largest = num_tuple[0]  # Start with the first element
    for num in num_tuple:
        if num > largest:
            largest = num
    return largest

# Example usage
numbers = (10, 20, 30, 40, 50)
print(largest_in_tuple(numbers))  # Output: 50
