def get_user_input():
    while True:
        user_input = input("Enter a word (type 'exit' to quit): ")
        if user_input.lower() == "exit":
            break
        print(user_input)

# Call the function to start getting user input
get_user_input()
