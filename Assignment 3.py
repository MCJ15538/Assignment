# Stack implemented using a Python list
stack = []

# Push elements onto the stack
def push(item):
    stack.append(item)

# Pop elements off the stack
def pop():
    if not is_empty():
        return stack.pop()
    return None

# Check if the stack is empty
def is_empty():
    return len(stack) == 0

# Peek at the top element of the stack
def peek():
    if not is_empty():
        return stack[-1]
    return None


def reverse_string(input_string):
    for char in input_string:
        push(char)

    reversed_str = ""
    while not is_empty():
        reversed_str += pop()

    return reversed_str


# Example usage
text = "hello"
print("Original:", text)
print("Reversed:", reverse_string(text))
