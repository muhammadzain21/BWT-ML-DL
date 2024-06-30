# Function to read data from a text file and print its contents
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            print(f"Contents of {filename}:")
            print(data)
            return data
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from the file '{filename}'.")


# Function to write user input to a new file and handle exceptions
def write_to_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
            print(f"Successfully wrote to {filename}")
    except IOError:
        print(f"Error: Could not write to the file '{filename}'.")


# Function to count words in a file
def count_words(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()
            words = data.split()
            word_count = len(words)
            print(f"Number of words in {filename}: {word_count}")
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
    except IOError:
        print(f"Error: Could not read from the file '{filename}'.")


# Main program execution
if __name__ == "__main__":
    # Test reading from data.txt
    read_file('data.txt')

    # Test writing user input to output.txt
    user_input = input("Enter content to write to output.txt: ")
    write_to_file('output.txt', user_input)

    # Test counting words in data.txt
    count_words('data.txt')
