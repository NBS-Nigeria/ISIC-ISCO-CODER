#creating variabes of different types
Age = 80                       # whole number (integer)
Percentage = 99.9              # decimal number (float)
Country = "Nigeria"            # text (string)
Is_Africa = True               # True or False (boolean)


#output

print(type(Age))
print(type(Percentage))
print(type(Country))
print(type(Is_Africa))

# A list of five Nigerian states.

Nigerian_States = ["Kogi", "Kwara", "Ogun", "Oyo", "Lagos"]
print(Nigerian_States)

# A tuple with three currency code.

Currency_Code = ("USD", "EUR", "GBP")       #USDollar, Euro, Great British Pound
print(Currency_Code)

# A set of unique student IDs.

Student_IDs = {17, 18, 19, 20, 21}           #Student IDs
print(Student_IDs)

# A dictionary mapping students name to scores.

Student_Scores = dict({"Amira": 100, "Stanley": 500, "Isaac": 200, "Amina": 200, "Salihijo": 300})
print(Student_Scores)

Student_Scores =  [
    {"Name": "Amira", "Score": 100},
    {"Name": "Stanley", "Score": 500},
    {"Name": "Isaac", "Score": 200},
    {"Name": "Amina", "Score": 200},
    {"Name": "Salihijo", "Score":300}
]
print(Student_Scores)

for Student in Student_Scores:
    print(Student["Name"], "has", Student["Score"], "scores")