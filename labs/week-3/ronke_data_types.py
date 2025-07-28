#creating variabes of different types

age = 25                      # whole number (integer)
height = 5.3              # decimal number (float)
name = "Ronke"            # text (string)
is_student = True              # True or False (boolean)


#output

print(type(age))
print(type(height))
print(type(name))
print(type(is_student))

# A list of five Nigerian states.

Nigerian_States = ["Kogi", "Kwara", "Osun", "Ekiti", "Oyo"]
print(Nigerian_States)

# A tuple with three currency code.

Currency_Code = ("USD", "EUR", "YEN")       #USDollar, Euro, Yen
print(Currency_Code)

# A set of unique student IDs.

Student_IDs = {1, 3, 5, 8, 10, 12}           #Student IDs
print(Student_IDs)

# A dictionary mapping students name to scores.

Student_Scores = dict({"Ade": 100, "Deborah": 500, "Ernest": 200, "James": 250, "Betty": 300})
print(Student_Scores)

Student_Scores =  [
    {"Name": "Ade", "Score": 100},
    {"Name": "Deborah", "Score": 500},
    {"Name": "Ernest", "Score": 200},
    {"Name": "James", "Score": 200},
    {"Name": "Betty", "Score":300}
]
print(Student_Scores)

for Student in Student_Scores:
    print(Student["Name"], "has", Student["Score"], "scores")