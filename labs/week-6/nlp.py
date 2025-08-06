# Simulate your dataset.
# Clean the text:
# Convert to lowercase.
# Remove punctuation, numbers, and stopwords.
# Tokenize text and calculate most frequent words.
# Create a simple occupation keyword dictionary that maps common terms to ISCO codes.
# Write a function that assigns ISCO codes based on keyword matching.
# Apply the function to the dataset and create a new column ISCO_code.
# Export the updated dataset as firstname_labour_force_coded.csv.


import pandas as pd
import string
from collections import Counter

# Simulate a dataset
data = {
    'id': [1, 2, 3, 4, 5],
    'name': ['Ann', 'Akpos', 'Sultan', 'Akanmu', 'Okadigbo'],
    'occupation': [
        'AEDC, Nepa Elect Engr2 AEDC',
        'Civil servant, (account)',
        'buying and selling, market trader',
        'Graphic Designer - Printing press',
        'Gaenacology Spec'
    ]
}   

# Create DataFrame
df = pd.DataFrame(data)
df.head()

# Clean text , Tokenize text and calculate most frequent words
def clean_text(text):
    # Convert to lowercase
    text = str(text.lower())

    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))

    replacements = {
        'engr': 'engineer',
        'spec': 'specialist',
        'elect': 'electrician',
        'account': 'accountant',
    }
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)
    
    # Remove numbers
    text = ''.join([char for char in text if not char.isdigit()])   
    # Remove stopwords 
    stopwords = set(['and', 'the', 'a', 'to', 'in', 'of', 'for', 'is', 'it', 'that', 'this'])
    text = ' '.join([word for word in text.split() if word not in stopwords])
    text = text.strip()  # Remove leading and trailing spaces
    text = text.replace('-', ' ')  # Replace hyphens with spaces
    temp_text = text
    # Tokenize text and calculate most frequent words
    word_count = Counter(text.split()).most_common(10)

    # Prepare 'text' for 'cleaned_occupation' (unique words only) 
    # Convert the words to a set to get unique words, then convert back to a list.
    # Using sorted() ensures consistent order, as sets are unordered.
    text = sorted(list(set(temp_text.split())))
    
    # Join the unique words back into a single string
    text = ' '.join(text)
    
    return text, word_count


# Apply cleaning function to the occupation column
df[['cleaned_occupation', 'word_count']] =  df['occupation'].apply(clean_text).apply(pd.Series)
print(df[['name','occupation', 'cleaned_occupation', 'word_count']])



# create ISCO code dictionary
isco_codes = {
    'engineer': 'ISCO-213',
    'electrician': 'ISCO-7411',
    'accountant': 'ISCO-2411',
    'specialist': 'ISCO-2211',
    'trader': 'ISCO-5221',
    'designer': 'ISCO-2166',
    'servant': 'ISCO-4110',
}

# Function to assign ISCO codes based on keyword matching
def assign_isco_code(tokens):
    for keyword, code in tokens:
        if keyword in isco_codes:
            return isco_codes[keyword]        
    return '0000'  # Default code if no match 

# Apply the function to the dataset and create a new column ISCO_code
df['ISCO_code'] = df['word_count'].apply(assign_isco_code)
print(df[['name', 'occupation', 'cleaned_occupation', 'ISCO_code']])

# Export the updated dataset
df.to_csv('data\lucky_labour_force_coded.csv', index=False)