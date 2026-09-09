# Codewar Solution: Even or Odd
def even_or_odd(number):
    return "Even" if number % 2 == 0 else "Odd"


# Codewar Solution: Convert a Number to a String
def number_to_string(num):
    return str(num)

# Codewar Solution: Remove String Spaces
def no_space(x):
    return x.replace(" ", "")

# Codewar Solution: Vowel Count
def get_count(sentence):
    return sum(1 for char in sentence if char in "aeiou")