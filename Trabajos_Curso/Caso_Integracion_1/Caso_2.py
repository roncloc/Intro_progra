saldo = float(10000)


cuenta = "0"
contraseña = "0"
x= 1


while len(cuenta) != 10:
    cuenta = input("\nIngrese el numero de cuenta: ")

    if len(cuenta) != 10:

        print("\nPor favor inserte un numero de cuenta valido de 10 digitos.")


while len(contraseña) != 6:
    contraseña = input("\nIngrese su contraseña: ")

    if len(contraseña) != 6:

        print("\nPor favor recuerde que se contraseña debe contener solo 6 digitos")



while x == 1:

    retiro = float(input("\nIngrese la cantidad de dinero a retirar: "))

    if retiro < saldo:

        print(f"\nProcesando.....\n\nSaldo actual: {saldo}\n\nSaldo despues del retiro: {saldo - retiro}\n")

        x = 0

    else:

        print(f"\nEl monto seleccionado es mayor que su saldo disponible de {saldo}, favor ingresar un monto de retiro menor que su saldo disponible.")
