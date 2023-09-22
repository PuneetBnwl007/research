# research
# Function to reverse a string
def reverse_string(input_string):
    # Use string slicing to reverse the string
    reversed_string = input_string[::-1]
    return reversed_string

# Main function
def main():
    # Get a string from the user
    input_string = input("Enter a string: ")
    
    # Call the reverse_string function and display the result
    reversed_str = reverse_string(input_string)
    print(f"Reversed string: {reversed_str}")

# Entry point of the program
if __name__ == "__main__":
    main()

