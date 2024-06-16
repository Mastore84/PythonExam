# Viser map() funktionen i brug
numbers = [1, 2, 3, 4, 5]

# Få kvadratet af hvert tal i listen
squared = map(lambda x: x ** 2, numbers)
print(list(squared))  # Output: [1, 4, 9, 16, 25]

# Viser filter() funktionen i brug
ages = [18, 25, 30, 15, 40]

# Filtrer alderen over 20
adults = filter(lambda age: age > 20, ages)
print(list(adults))  # Output: [25, 30, 40]

# Funktion til at beregne gennemsnit
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)

# Brug af funktionen
scores = [85, 90, 92, 88, 95]
average_score = calculate_average(scores)
print("Gennemsnitlig score:", average_score)  # Output: Gennemsnitlig score: 90.0

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

#lambda
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
