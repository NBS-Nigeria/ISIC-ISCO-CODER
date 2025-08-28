#exercise
import pandas as pd
import re
import string
import nltk
print(nltk.__version__)

# Step 1: Simulate your dataset


mydf = pd.DataFrame({
    'person_id': [1001, 1002, 1003, 1004, 1005],
    'occupation_response': [
        "TEACHER, at a private secondary school",   #Mixed case, punctuation
        "sells clothes on street (informal)", # Parentheses, missing 'the'
        "MEDICAL Dr. hospital",    # Abbreviations, mixed case, punctuation
        " CIVIL ENGR  ",     # All caps, trailing spaces
        "gold-miner"   # Hyphenated
    ]
})

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
        'dr': 'doctor',
    }
    for wrong, right in replacements.items():
        text = text.replace(wrong, right)
    
    # Fix all spacing issues (including removing hyphens)
    text = text.replace('-', ' ')  # Replace hyphens with spaces
    text = ' '.join(text.split())  # This handles all whitespace normalization
    
    return text
# Apply cleaning
mydf["cleaned_occupation"] = mydf["occupation_response"].apply(clean_text)

# Show results
mydf[["person_id", "occupation_response", "cleaned_occupation"]]
print(mydf[["person_id", "occupation_response", "cleaned_occupation"]])

## Tokenization + Lemmatization (spaCy)

#Break into words and reduce to their base forms:s

import spacy

nlp = spacy.load("en_core_web_sm")

def tokenize_lemmatize(text):
    doc = nlp(text)
    return [token.lemma_ for token in doc if not token.is_stop and token.is_alpha]

mydf["tokens"] = mydf["cleaned_occupation"].apply(tokenize_lemmatize)
mydf[["cleaned_occupation", "tokens"]]
print(mydf[["cleaned_occupation", "tokens"]])

## ISCO Code Matching (Keyword Method) Define known keywords and their ISCO-08 major group codes:

isco_keywords = {
    "teacher": "2341",        # Secondary school teachers
    "doctor": "2221",         # Medical professionals
    "vendor": "5211",         # Street and market vendors
    "miner": "8111",          # Miners and quarriers
    "engineer": "2142"        # Civil engineers
}

def keyword_match(tokens):
    for token in tokens:
        if token in isco_keywords:
            return isco_keywords[token]
    return "0000"  # No match

mydf["isco_keyword"] = mydf["tokens"].apply(keyword_match)
mydf[["cleaned_occupation", "tokens", "isco_keyword"]]
print(mydf[["cleaned_occupation", "tokens", "isco_keyword"]])

## Fuzzy Matching for Spelling Variants Support imperfect matches using RapidFuzz:

from rapidfuzz import process

def fuzzy_match(text, mapping, threshold=80):

    # extractOne returns(best_match, score, index)
    result = process.extractOne(text, mapping.keys())
    if result and result[1] >= threshold: # result[1] is the score

        return mapping[result[0]] # result[0] is the best match
    return "0000" # Default code when no match found

mydf["isco_fuzzy"] = mydf["cleaned_occupation"].apply(lambda x: fuzzy_match(x, isco_keywords))
mydf[["cleaned_occupation", "isco_keyword", "isco_fuzzy"]]



## Final ISCO Assignment Use keyword match unless unavailable, then fall back to fuzzy match:

mydf["isco_final"] = mydf["isco_keyword"].where(mydf["isco_keyword"] != "0000", mydf["isco_fuzzy"])
mydf[["person_id", "cleaned_occupation", "isco_final"]]