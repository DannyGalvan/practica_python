def divisor(num):
    try:
        if num <= 0 : 
            raise ValueError ("ingresa un numero positivo")   
        divisors = [i for i in range (1, num+1) if num % i == 0 ]
        return divisors
    except ValueError as ve:
        print(ve)
        return False


def run():
    try:
        num = int(input("ingresa un número: "))
        print(divisor(num))
        print("termino el programa")  
    except ValueError:
        print("No puedes ingresar texto")

if __name__ == "__main__":
    run()