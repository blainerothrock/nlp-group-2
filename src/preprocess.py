import nltk
from nltk.tokenize import RegexpTokenizer
from nltk.stem import WordNetLemmatizer, PorterStemmer
from nltk import word_tokenize
import re

lemmatizer = WordNetLemmatizer()
stemmer = PorterStemmer()   

def preprocess(corps):
    # nltk.download('punkt')
    corps = str(corps)
    corps = corps.lower()
    # rid tags
    corps = corps.replace('{html}',"") 
    cleanr = re.compile('<.*?>')
    cleantext = re.sub(cleanr, '', corps)
    # rid url
    rid_url = re.sub(r'http\S+', '',cleantext)
    # rid numbers
    rid_num = re.sub('[0-9]+', '', rid_url)
    # tokenizing
    tokenizer = RegexpTokenizer(r'\w+')
    tokens = tokenizer.tokenize(rid_num)  
    filtered_words = [w for w in tokens if len(w) > 2] 
    stem_words = [stemmer.stem(w) for w in filtered_words]
    lemma_words = [lemmatizer.lemmatize(w) for w in stem_words]

    return filtered_words
