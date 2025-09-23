import joblib
import json
import pandas as pd
import numpy as np
import nltk
nltk.download('punkt')
nltk.download('stopwords')
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from tensorflow.keras.preprocessing.text import tokenizer_from_json
from tensorflow.keras.preprocessing.sequence import pad_sequences

def test_preprocessor(text):
    text=text.lower()
    translator=str.maketrans("","",string.punctuation)
    text=text.translate(translator)
    words=word_tokenize(text)
    stop=set(stopwords.words("english"))
    clean_words=[word for word in words if word not in stop]
    with open('tokenizer.json', 'r', encoding='utf-8') as f:
        tokenizer_json_str = f.read()
    tokenizer_json = json.loads(tokenizer_json_str)
    loaded_tokenizer = tokenizer_from_json(tokenizer_json)
    data=loaded_tokenizer.texts_to_sequences([clean_words])
    padded = pad_sequences(data, padding="post",maxlen=40)
    data=padded
    return data