categoria = input("Por favor introduzca su categoria (debe ser un numero del 1 al 4): ")
salario = int(input("Indique su salario: "))

if categoria == str(1):
    salario = salario*1.10

else:
    if categoria == str(2):
        salario = salario*1.12

    else:
        if categoria == str(3):
            salario = salario*1.15

        else:
            if categoria == str(4):
                salario = salario*1.20

            else:
                print("Por favor indique una categoria válida")


print(f"Segun la categoria indicada, su salario con el incremento respectivo es de {salario}")