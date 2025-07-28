# example of data types
age = 40  #integer
average_temp = 28.5  #float,
name = "Tekiyat" #string
is_enrolled = True  #boolean

print(type(age))
print(type(average_temp))
print(type(name))
print(type(is_enrolled))

print("Age:", age)
print("average_temp:", average_temp)
print("name:", name)
print("is_enrolled:", is_enrolled)

## Strings (Text)

##Strings store words or sentences. You can look at parts of them:

name = "Tekiyat"

print(name[0])      # First letter
print(name[-1])     # Last letter
print(name[0:4])    # First 4 letters: 'Teki'
print(name[0:])     # Letters from position 0 onwards

# List of five Nigerian states
states = ["Lagos", "Kano", "Kaduna", "Rivers", "Enugu"]

print("states:", states)

# Tuple with three currency codes
currencies = ("NGN", "USD", "EUR")

# Set of unique student IDs
staff_ids = {"NBS001", "NBS002", "NBS003", "NBS004", "NBS005"}

# Dictionary mapping student names to scores
rank = {
    "Aisha": "senior statistician",
    "Bola": "statistician 1",
    "Chinedu": "program analyst",
    "Fatima": "program analyst"
}
print(rank)

