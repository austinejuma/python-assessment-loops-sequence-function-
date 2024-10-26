def reverse_strings(string_list):
    reversed_list = []
    for string in string_list:
        reversed_list.append(string[::-1])
    return reversed_list

# Example usage
strings = ["apple", "banana", "cherry"]
print(reverse_strings(strings))  
# Output: ['elppa', 'ananab', 'yrrehc']
