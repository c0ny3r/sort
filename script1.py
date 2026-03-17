import random

def generate_random_list(size, min_val, max_val):
    """Generates a list of random integers within a specified range."""
    return [random.randint(min_val, max_val) for _ in range(size)]

my_list = generate_random_list(26500000, 1, 100000000000000000000000000000000000000000000000)
print(f"Original list: {my_list}")
number_to_find=19857495348573948579385437975839457947593457349
if number_to_find in my_list:
    print(f"{number_to_find} was found in the list.")
else:
    print(f"{number_to_find} was not found.")