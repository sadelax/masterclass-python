from custom_hypes import Word, Histogram

def count_words(words:list)->dict[Word:int]:
    """
    recibe una lista de palabras y devuelve un diccionario
    con cada palabra como clave, y como valor el número de ocurrencias
    de la misma palabra
    """
    # recorro lista de palabras
    # cada palabra q encuentro, si está en el diccionario, es q ya la he visto en el pasado.
        # en ese caso, incremento el valor a 1
    # si no estaba, añado una nueva entrada al diccionario con la palabra y un 1 como valor

    diccionario = {}
    for word in words:
        if word in diccionario:
            diccionario.update({word: diccionario[word] + 1})
        else:
            diccionario[word] = 1

    return diccionario

# def make_histogram(occs: dict[Word:int], total_occs: int) -> Histogram:
