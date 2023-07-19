"""
1. leer la jugada del humano
2. generar jugada aleatoria
3. comparar resultados el resultado
4. imprimir resultado
5. reiniciar el bucle
"""

from enum import Enum
from random import choice

class GameChoice(Enum):
    INVALID = -1
    PAPER = 1
    ROCK = 2
    SCISSORS = 3
    QUIT = 4

def game_loop():
    """
    arranca el bucle del juego
    """
    while True:
        # leer selección de usuario
        user_choice = read_user_choice()
                
        if not is_exit(user_choice):
            # genero la jugada del ordenador
            comp_choice = generate_computer_choice()

            # evalúo la jugada
            result = evaluate_move(user_choice, comp_choice)

            # muestro el resultado
            print_result(result)
        
        else:
            break


def read_user_choice()->GameChoice:
    """
    imprime un menú de opciones y lee la respuesta del usuario
    mediante una llamada a input.
    devuelve lo q haya escrito el usuario
    """
    user_choice = GameChoice.INVALID

    while user_choice == GameChoice.INVALID:
        print("Select one number:")
        print(f"{GameChoice.PAPER.value} paper")
        print(f"{GameChoice.ROCK.value} rock")
        print(f"{GameChoice.SCISSORS.value} scissors")
        print("-----------")
        print(f"{GameChoice.QUIT.value} quit")

        try:
            user_choice = GameChoice(int(input('Enter your choice: ')))
        except ValueError:
            user_choice = GameChoice.INVALID

    return user_choice

def is_exit(user_choice: GameChoice)->bool:
    """
    predicado q recibe la respuesta del usuario y devuelve True
    si ha pedido salir del juego
    """
    return user_choice == GameChoice.QUIT

def generate_computer_choice()->GameChoice:
    """
    devuelve al azar una selección del ordenador: piedra, papel o tijera
    """
    # return choice([GameChoice.PAPER, GameChoice.ROCK, GameChoice.SCISSORS])
    # return GameChoice.PAPER
    return GameChoice.ROCK
    # return GameChoice.SCISSORS

def evaluate_move(user_choice: GameChoice, computer_choice: GameChoice)->str:
    """
    compara dos selecciones (tienen q ser piedra, papel o tijera)
    y devuelve un resultado: 'papel envuelve a piedra'
    """
    assert user_choice != GameChoice.INVALID and user_choice != GameChoice.QUIT
    assert computer_choice != GameChoice.INVALID and computer_choice != GameChoice.QUIT
    
    result = ""
    if user_choice == computer_choice:
        result = "tú ganas! empate"
    else:
        if user_choice == GameChoice.PAPER and computer_choice == GameChoice.ROCK:
            result = "tú ganas! papel envuelve a roca"
        elif user_choice == GameChoice.ROCK and computer_choice == GameChoice.SCISSORS:
            result = "tú ganas! piedra rompe tijeras"
        elif user_choice == GameChoice.SCISSORS and computer_choice == GameChoice.PAPER:
            result = "tú ganas! tijera corta papel"
        else:
            result = "perdiste", computer_choice.name, "gana a ", user_choice.name
    return result

def print_result(result: str)->None:
    """
    imprime en plan bonito el resultado. no devuelve nada
    """
    return None

# def test():
#     print('Arrancó!')

# if __name__ == "__main__":
#     # me llaman desde la línea de comandos
#     test()
# else:
#     # me están importando
#     print('me importaron y mi nombre no será __main__, sino __game__')

if __name__ == "__main__":
    game_loop()
