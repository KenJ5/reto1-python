def imprimir_resultado(func):
    def wrapper(n1, n2):
        resultado = func(n1, n2)
        print("El resultado es:", resultado)
    return wrapper

@imprimir_resultado
def suma(n1, n2):
    return n1 + n2

@imprimir_resultado
def resta(n1, n2):
    return n1 - n2

@imprimir_resultado
def multiplicacion(n1, n2):
    return n1 * n2

@imprimir_resultado
def division(n1, n2):
    if n2 == 0:
        return "No se puede dividir entre cero"
    else:
        return n1 / n2

def menu():
    print("Calculadora:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
    opcion = int(input("Seleccione una de las opciónes: "))
    return opcion

def calcular():
    n1 = float(input("Digite el primer número: "))
    n2 = float(input("Digite el segundo número: "))
    opcion = menu()
    while opcion != 5:
        if opcion == 1:
            suma(n1, n2)
        elif opcion == 2:
            resta(n1, n2)
        elif opcion == 3:
            multiplicacion(n1, n2)
        elif opcion == 4:
            division(n1, n2)
        else:
            print("Error, Intente nuevamente.")
        opcion = menu()
        
calcular()