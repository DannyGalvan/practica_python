def divisor(num):
    divisors = [i for i in range (1, num+1) if num % i == 0 ]
    return divisors

def run():
    try:
        num = input("ingresa un número: ")
        assert num.isnumeric()
        assert int(num) > 0
        print(divisor(int(num)))
        print("termino el programa")  
    except AssertionError:
        print("no puedes ingresar texto ni numero negativos")

if __name__ == "__main__":
    run()