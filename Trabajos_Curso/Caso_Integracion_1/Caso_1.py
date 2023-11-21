n = int(input("Ingrese la cantidad de números enteros a evaluar: "))

while n <= 0:
    print("Por favor ingreasr una cantidad de numeros mayor que 0")

    n = int(input("Ingrese la cantidad de números enteros a evaluar: "))



for i in range(n):
    numero = int(input("Ingrese un número entero: "))
    if numero == 0:
        print("Error: El número entero no puede ser cero. Intente de nuevo por favor.")
    elif numero > 0:
        numero = numero**2
        print(f"El cuadrado de este número es: {numero}")
    else:
        numero *= -1
        print("El número convertido a positivo es: {numero}")