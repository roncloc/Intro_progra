numero_1 = int(input("Introduzca el primer numero: "))
numero_2 = int(input("Introduzca el segundo numero: "))

iguales = numero_1 == numero_2
diferentes = numero_1 != numero_2
numero_1_mayor = numero_1 > numero_2
numero_2_mayor = numero_2 > numero_1

print(f"Decir que el primer numero es igual que el segundo numero es: {iguales}\nDecir que el primer numero es diferente que el segundo numero es: {diferentes}\nDecir que el primer numero es mayor que el segundo numero es: {numero_1_mayor}\nDecir que el segundo numero es mayor que el primer numero es: {numero_2_mayor}")