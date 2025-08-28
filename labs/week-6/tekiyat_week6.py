## Load Survey Data (Mock NLFS Sample)

import pandas as pd

# Simulated sample based on real structure from NLFS Q2 2024 microdata
df = pd.DataFrame({
    "person_id": [1101, 1102, 1103, 1104, 1105],
    "occupation_response": [
        "Secondary Teacher, PUBLIC school",  # Mixed case, punctuation
        "REGISTERED NURSE  ",  # All caps, trailing spaces
        "sells fruit on roadside (informal)",  # Parentheses, missing 'the'
        "small-scale gold miner",  # Hyphenated
        "CIVIL ENGR. constr.site"  # Abbreviations, mixed case, punctuation
    ]
})
df.head()
print(df.head())

## Clean and Normalize the Text Remove punctuation and convert to lowercase:

import string

def clean_text(text):
    # Convert to string and lowercase
    text = str(text).lower()
    
    # Remove punctuation (keeping apostrophes)
    text = text.translate(str.maketrans('', '', string.punctuation.replace("'", "")))
    
    # Standardize abbreviations
    replacements = {
        'engr': 'engineer',
        'constr': 'construction',
        'site': ' site'  # Ensure space before 'site'
    }
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)
    
    # Fix all spacing issues (including removing hyphens)
    text = text.replace('-', ' ')  # Replace hyphens with spaces
    text = ' '.join(text.split())  # This handles all whitespace normalization
    
    return text
# Apply cleaning
df["cleaned_occupation"] = df["occupation_response"].apply(clean_text)

# Show results
df[["person_id", "occupation_response", "cleaned_occupation"]]
print(df[["person_id", "occupation_response", "cleaned_occupation"]])

## Tokenization + Lemmatization (spaCy)

#Break into words and reduce to their base forms:

import spacy

nlp = spacy.load("en_core_web_sm")

def tokenize_lemmatize(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

df["tokens"] = df["cleaned_occupation"].apply(tokenize_lemmatize)
df[["cleaned_occupation", "tokens"]]
print(df[["cleaned_occupation", "tokens"]])

## ISCO Code Matching (Keyword Method) Define known keywords and their ISCO-08 major group codes:

isco_keywords = {
    "teacher": "2341",        # Secondary school teachers
    "nurse": "2221",          # Nursing professionals
    "vendor": "5211",         # Street and market vendors
    "miner": "8111",          # Miners and quarriers
    "engineer": "2142"        # Civil engineers
}

def keyword_match(tokens):
    for token in tokens:
        if token in isco_keywords:
            return isco_keywords[token]
    return "0000"  # No match

df["isco_keyword"] = df["tokens"].apply(keyword_match)
df[["cleaned_occupation", "tokens", "isco_keyword"]]
print(df[["cleaned_occupation", "tokens", "isco_keyword"]])

## Fuzzy Matching for Spelling Variants Support imperfect matches using RapidFuzz:

from rapidfuzz import process

def fuzzy_match(text, mapping, threshold=80):

    # extractOne returns(best_match, score, index)
    result = process.extractOne(text, mapping.keys())
    if result and result[1] >= threshold: # result[1] is the score

        return mapping[result[0]] # result[0] is the best match
    return "0000" # Default code when no match found

df["isco_fuzzy"] = df["cleaned_occupation"].apply(lambda x: fuzzy_match(x, isco_keywords))
df[["cleaned_occupation", "isco_keyword", "isco_fuzzy"]]



## Final ISCO Assignment Use keyword match unless unavailable, then fall back to fuzzy match:

df["isco_final"] = df["isco_keyword"].where(df["isco_keyword"] != "0000", df["isco_fuzzy"])
df[["person_id", "cleaned_occupation", "isco_final"]]


#exercise
import pandas as pd
import re
import string
#import nltk
#from nltk.corpus import stopwords
#from collections import Counter
import nltk
print(nltk.__version__)


