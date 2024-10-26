def has_pair_with_sum(input_list, target_sum):
    for i in range(len(input_list)):
        for j in range(i + 1, len(input_list)):
            if input_list[i] + input_list[j] == target_sum:
                return True
    return False

# Example usage
numbers = [1, 2, 3, 4, 5]
target = 8
print(has_pair_with_sum(numbers, target))  # Output: True (3 + 5)
