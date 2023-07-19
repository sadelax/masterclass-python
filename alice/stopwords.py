from unicodedata import normalize
from custom_hypes import Stopwords

def load_stopwords(file_name: str)-> Stopwords:
    with open(file_name, 'r') as stopwords_file:
        buff = stopwords_file.read().lower()
        words = buff.split()
    
    normalized_words = map(lambda word: normalize('NFC', word), words)
    wordset = set(normalized_words)
    return wordset

def is_stopword():
    for word in load_stopwords:
        return word in load_stopwords

if __name__ == "__main__":
    print(load_stopwords('alice_full_text.txt'))