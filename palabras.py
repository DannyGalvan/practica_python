import random
def run():
    palabra = []

    with open("./archivos/data.txt","r",encoding="utf-8") as palabrerillo:
        for palabrita in (palabrerillo):
            palabra.append(palabrita)  

        palabra_aleatoria = random.choice(palabra)
        palabra_aleatoria= palabra_aleatoria.strip()
        palabra_aleatoria= palabra_aleatoria.upper()
        typo = {
            ord("Á") : ("A"),
        }
        palabra_aleatoria = palabra_aleatoria.translate(typo)
        print(palabra_aleatoria)

if __name__ == "__main__":
    run()