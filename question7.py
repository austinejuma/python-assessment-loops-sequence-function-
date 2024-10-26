def remove_duplicates(input_list):
    new_list = []
    for item in input_list:
        if item not in new_list:
            new_list.append(item)
    return new_list

# Example usage
nums = [1, 2, 2, 3, 4, 4, 5]
print(remove_duplicates(nums))  # Output: [1, 2, 3, 4, 5]
