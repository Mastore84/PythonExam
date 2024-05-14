class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise ValueError("Name must be a string")

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if isinstance(value, int) and value > 0:
            self._age = value
        else:
            raise ValueError("Age must be a positive integer")

# Creating an instance of the Person class
person = Person("Alice", 30)

# Accessing and updating properties
print(person.name)  # Output: Alice
person.name = "Bob"
print(person.name)  # Output: Bob

print(person.age)   # Output: 30
person.age = 25
print(person.age)   # Output: 25