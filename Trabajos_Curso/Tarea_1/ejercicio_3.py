texto = input("Introduzca el texto que desee para asi calcular su longitud: ")

largo_texto = len(texto)

if largo_texto >= 3 and largo_texto < 10:
    print("El texto introducido posee una longitud mayor o igual que 3, pero es menor que 10")

else:
    print("El largo del texto indroducido es menor que 3, o es mayor que 9.")