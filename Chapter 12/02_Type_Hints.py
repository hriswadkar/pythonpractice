
# Variable type hints
age: int = 45

# Function type hints
def greeting(name: str) -> str:
    return f"Hello, {name}"

# Usage
print(greeting("Harshad"))
print(age)
print(age.is_integer())
print(age.bit_count())
print(age.bit_length())


