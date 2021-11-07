import random
import os
import sys

TEXT_GAMEOVER = """
    ######      ###    ##     ## ########      #######  ##     ## ######## ########  
    ##    ##    ## ##   ###   ### ##           ##     ## ##     ## ##       ##     ## 
    ##         ##   ##  #### #### ##           ##     ## ##     ## ##       ##     ## 
    ##   #### ##     ## ## ### ## ######       ##     ## ##     ## ######   ########  
    ##    ##  ######### ##     ## ##           ##     ##  ##   ##  ##       ##   ##   
    ##    ##  ##     ## ##     ## ##           ##     ##   ## ##   ##       ##    ##  
    ######   ##     ## ##     ## ########      #######     ###    ######## ##     ## 
"""

TEXT_CONGRATS = """
    ######   #######  ##    ##  ######   ########     ###    ########  ######  
    ##    ## ##     ## ###   ## ##    ##  ##     ##   ## ##      ##    ##    ## 
    ##       ##     ## ####  ## ##        ##     ##  ##   ##     ##    ##       
    ##       ##     ## ## ## ## ##   #### ########  ##     ##    ##     ######  
    ##       ##     ## ##  #### ##    ##  ##   ##   #########    ##          ## 
    ##    ## ##     ## ##   ### ##    ##  ##    ##  ##     ##    ##    ##    ## 
    ######   #######  ##    ##  ######   ##     ## ##     ##    ##     ######  
"""

text_hangman = """
##     ##    ###    ##    ##  ######   ##     ##    ###    ##    ##           ######      ###    ##     ## ######## 
##     ##   ## ##   ###   ## ##    ##  ###   ###   ## ##   ###   ##          ##    ##    ## ##   ###   ### ##       
##     ##  ##   ##  ####  ## ##        #### ####  ##   ##  ####  ##          ##         ##   ##  #### #### ##       
######### ##     ## ## ## ## ##   #### ## ### ## ##     ## ## ## ##          ##   #### ##     ## ## ### ## ######   
##     ## ######### ##  #### ##    ##  ##     ## ######### ##  ####          ##    ##  ######### ##     ## ##       
##     ## ##     ## ##   ### ##    ##  ##     ## ##     ## ##   ###          ##    ##  ##     ## ##     ## ##       
##     ## ##     ## ##    ##  ######   ##     ## ##     ## ##    ##           ######   ##     ## ##     ## ######## """

HANGMANPICS = ['''
  +---+
      |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
      |
      |
      |
      |
=========''',
'''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


def leer():
    palabras = []
    with open("./archivos/data.txt", "r", encoding="utf-8") as data:
        for palabra in (data):
           palabras.append(palabra)
        palabra_aleatoria = str(random.choice (list(palabras)))
        palabra_aleatoria= palabra_aleatoria.strip()
        palabra_aleatoria= palabra_aleatoria.upper()
        cadena= str(palabra_aleatoria)
        mapeo= {
            ord('Á'): 'A',
            ord('É'): 'E',
            ord('Í'): 'I',
            ord('Ó'): 'O',
            ord('Ú'): 'U',        
        }
        cadena= cadena.translate(mapeo)
        return cadena    


def play():
    word = leer()
    
    palabrita = ["_"] * len(word)
    intentos = 7

    while intentos > 0:   
        os.system("clear")  
        print(text_hangman) 
        for spaces in palabrita:
            print(spaces, end=" ")
        print(" ")
        print(HANGMANPICS[intentos])
        letter = input("Ingresa una letra: ").upper()
        

        found = False
        for idx, character in enumerate(word):
            if character == letter:
                palabrita[idx] = letter 
                found = True 

        if not found :
            intentos = intentos - 1

        if "_" not in palabrita: 
            os.system("clear")
            print(TEXT_CONGRATS) 
            print("             ADIVINASTE LA PALABRA " + word + " FELICIDADES!!! ❤️ ❤️ ❤️ ❤️ ❤️ ❤️ ❤️")
            input()
            break
                 
        
        if intentos == 0 :
            os.system("clear")  
            print(TEXT_GAMEOVER)
            print("             La palabra era " + word)
            input()
            break
           


def run():

    OP = """
                Ingresa una opcion!!

 1) Desea ingresar al Juego          2) Desea Salir
    
    """
    
    while True:
        try:
            os.system("clear")
            print(text_hangman) 
            menu = int(input(OP))
            if menu == 1 :
                play()
            if menu == 2 :
                os.system("clear")
                sys.exit()
        except ValueError:
            print("solo tiene 2 opciones")
         
            

if __name__ == "__main__":
    run()