from unicodedata import normalize
from custom_hypes import Word, Stopwords
import string
from stopwords import is_stopword

def load_text(file_name: str)-> Stopwords:
    """
    recibe un nombre de fichero, lo lee y devuelve una lista
    de palabras, en minúsculas, con unicode normalizado
    y sin signos de puntuación
    """
    # abro el fichero, lo leo y carga en una string
    # paso todo a minus
    # tokenizo
    # normalizo el unicode de cada palabra
    # compruebo si quedan signos de puntuación
    # (si los hay, quitarlos)
    # devuelve la lista limpia de polvo y paja

    with open(file_name, 'r') as alice_file:
        buff = alice_file.read().lower()
        words = buff.split()

        normalized_words = map(lambda word: normalize('NFC', word), words)
        clean_words = map(lambda word: word.translate(str.maketrans('', '', string.punctuation)),normalized_words)
        meaningful_words = filter(lambda word: not is_stopword(word), clean_words)
        
        return meaningful_words

if __name__ == "__main__":
    print(load_text('alice_full_text.txt'))
