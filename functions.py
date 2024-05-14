# Example of a simple function
def greet(name):
    return f"Hello, {name}!"

print(greet("Alice"))  # Output: Hello, Alice!

# Example of using a decorator
def uppercase_decorator(func):
    def wrapper(name):
        result = func(name)
        return result.upper()
    return wrapper

@uppercase_decorator
def upper_greet(name):
    return f"Hello, {name}!"

print(upper_greet("Bob"))  # Output: HELLO, BOB!