def divisors(num):
    divisors =[]
    for i in range(1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    num = input("Ingresa un numero: ")
    assert num.isnumeric() and num.isnumeric() > 0, "Introduce un número positivo"
    print(divisors(int(num)))
    print("Terminó el programa")

if __name__=="__main__":
    run()