import pandas as pd
import re
import string
from collections import Counter

# Simulating dataset
data = {
    'id': [101, 102, 103, 104, 105],
    'occupation_description': [
        'OKADA RIDER, Motorcycle driver', # Mixed case
        'Cultivating Maize & Rice in his farm (farmer)', # Parentheses, punctuation
        'Food-seller by roadside ',# Hyphenated, trailing spaces
        'Medical Dr. at Gen.Hospital', # Abbreviations, mixed case, punctuation
        'Prof. lecturer at UNI ABUJA', # # Abbreviations, mixed case, punctuation
    ]
        }

df = pd.DataFrame(data)
df

# Define simple stopwords
simple_stopwords = set(['in', 'his', 'by', 'at'])

# Cleaning text
def clean_text(text):
    text = text.lower()  # convert to lowercase
    text = re.sub(r'\d+', '', text)  # remove digits
    text = text.translate(str.maketrans('', '', string.punctuation))  # remove punctuation
    tokens = text.split()
    tokens = [word for word in tokens if word not in simple_stopwords]
    return tokens

# Get most frequent words
all_tokens = []
for text in df['occupation_description']:
    all_tokens.extend(clean_text(text))
    
word_freq = Counter(all_tokens)
print("Most frequent words:", word_freq.most_common(10))

#  Simple occupation keyword dictionary that maps common terms to ISCO codes.
occupation_dict = {
    'driver': '8321',
    'okada': '8321',
    'dr': '2211',
    'doctor': '2211',
    'foodseller': '5212',
    'farmer': '6111',
    'lecturer': '2310',
    'professor': '2310',
    'prof': '2310',
    }

# Function that assigns ISCO codes based on keyword matching
def assign_isco(text):
    tokens = clean_text(text)
    for token in tokens:
        if token in occupation_dict:
            return occupation_dict[token]
    return '0000'  # unknown

# Apply function to dataset and create a new column ISCO_code.
df['ISCO_code'] = df['occupation_description'].apply(assign_isco)
df

# Export the updated dataset
df.to_csv('data\siyudi_labour_force_coded.csv', index=False)