def tuples_to_dict(tuples_list):
    result_dict = {}
    for string, number in tuples_list:
        result_dict[string] = number
    return result_dict

# Example usage
tuples_input = [("apple", 5), ("banana", 10), ("cherry", 15)]
print(tuples_to_dict(tuples_input))  # Output: {'apple': 5, 'banana': 10, 'cherry': 15}
