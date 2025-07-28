#creating variabes of different types
Age = 69                     # whole number (integer)
Percentage = 45.9              # decimal number (float)
Country = "poland"            # text (string)
Is_Africa = False               # True or False (boolean)


#output

print(type(Age))
print(type(Percentage))
print(type(Country))
print(type(Is_Africa))

# A list of five Nigerian states.

Nigerian_States = ["Taraba", "Niger", "Osun", "Oyo", "Edo"]
print(Nigerian_States)

# A tuple with three currency code.

Currency_Code = ("USD", "YEN", "GBP")       #USDollar, Yen, Great British Pound
print(Currency_Code)

# A set of unique student IDs.

Student_IDs = {12, 23, 16, 44, 71}           #Student IDs
print(Student_IDs)

# A dictionary mapping students name to scores.

Student_Scores = dict({"Amyrah": 500, "Stanley": 500, "Ibrahim": 140, "Amina": 99, "Salihijo": 450})
print(Student_Scores)

Student_Scores =  [
    {"Name": "Amyrah", "Score": 500},
    {"Name": "Stanley", "Score": 500},
    {"Name": "Ibrahim", "Score": 140},
    {"Name": "Amina", "Score": 99},
    {"Name": "Salihijo", "Score":450}
]
print(Student_Scores)

for Student in Student_Scores:
    print(Student["Name"], "has", Student["Score"], "scores")