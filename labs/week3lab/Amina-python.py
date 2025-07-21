print('hello')
#creating variabes of different types.
age = 71                        # whole number (int)
population = 5576900000.0       # decimal number (float)
country = "China"             # text (string)
is_Asia = True                # True or False (boolean)

print(type(age))
print(type(population))
print(type(country))
print(type(is_Asia))

# A list of five Nigerian states.

Nigerian_states = ["Abia", "Adamawa", "Akwa-ibom", "Anambra", "Bauchi"]
print(Nigerian_states)

# A tuple with three currency code.

currency_code = ("USD", "EUR", "NGN")
print(currency_code)

# A set of unique student IDs.

Student_ids = {101, 102, 103, 104, 105}
print(Student_ids)

# A dictionary mapping students name to scores.

Student_scores = dict({"Amira": 0, "Stanley": 200, "Isaac": 50, "Amina": 500, "Salihijo": 300})
print(Student_scores)

Student_scores =  [
    {"Name": "Amira", "Score": 0},
    {"Name": "Stanley", "Score": 200},
    {"Name": "Isaac", "Score": 50},
    {"Name": "Amina", "Score": 500},
    {"Name": "Salihijo", "Score":300}
]
print(Student_scores)

for student in Student_scores:
    print(student["Name"], "has", student["Score"], "scores")