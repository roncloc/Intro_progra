import registro_viajes

vehiculos = "Proyecto_Final/vehiculos.txt"


def agregar_vehiculo(placa, marca, estilo, modelo, capacidad):
    with open(vehiculos, "a") as file:
        file.write(f"{placa},{marca},{estilo},{modelo},{capacidad}\n")


def registrar_vehiculo():
    print(
        "\nHola! Bienvenido a Auto Transportes La Unión, por favor ingrese los siguientes datos para registrar su vehiculo.\n"
    )
    placa = input("Número de Placa: ").lower()
    marca = input("Marca: ").lower()
    estilo = input("Estilo: ").lower()
    modelo = input("Modelo(año): ").lower()
    capacidad = int(input("Capacidad de pasajeros: "))

    agregar_vehiculo(placa, marca, estilo, modelo, capacidad)


def obtener_vehiculos():
    with open(vehiculos, "r") as file:
        lineas = [linea.strip().split(",") for linea in file.readlines()]

    return lineas


def guardar_vehiculos(lista_vehiculos):
    with open(vehiculos, "w") as file:
        for x in lista_vehiculos:
            file.write(f"{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},\n")


def consultar_vehiculo():
    lista_vehiculos = obtener_vehiculos()
    placa = input("Inserte la placa del vehiculo: \n").lower()
    vehiculos_encontrados = []

    for x in lista_vehiculos:
        if x[0] == placa:
            vehiculos_encontrados.append(x)

    if len(vehiculos_encontrados) == 0:
        print("No se encontro ningun vehiculo con la placa indicada")

    else:
        return vehiculos_encontrados


def consultar_vehiculo_informe(placa):
    lista_vehiculos = obtener_vehiculos()
    placa = placa

    for x in lista_vehiculos:
        if x[0] == placa:
            return x


def editar_vehiculo():
    lista_vehiculos = obtener_vehiculos()
    placa = input("Inserte la placa del vehiculo: \n").lower()
    vehiculos_encontrados = []

    for x in lista_vehiculos:
        if x[0] == placa:
            print("Inserte los nuevos valores del vehiculo: \n")
            x[1] = input("Marca: ").lower()
            x[2] = input("Estilo: ").lower()
            x[3] = input("Modelo(año): ").lower()
            x[4] = input("Capacidad de pasajeros: ").lower()
            vehiculos_encontrados.append(x)

    guardar_vehiculos(lista_vehiculos)

    if len(vehiculos_encontrados) == 0:
        print("No se encontro ningun vehiculo con la placa indicada.")


def eliminar_vehiculo():
    viajes_encontrados = registro_viajes.lista_viajes()
    lista_vehiculos = obtener_vehiculos()
    vehiculos_no_eliminados = []
    placa = input("Inserte la placa del vehiculo: \n").lower()
    vehiculos_encontrados = []

    for x in lista_vehiculos:
        if x[0] == placa:
            vehiculos_encontrados.append(x)

        else:
            vehiculos_no_eliminados.append(x)

    for x in viajes_encontrados:
        if placa == x[1]:
            print(
                "Lo siento no podemos eliminar el vehiculo ya que tiene un viaje asignado, o ya completo uno."
            )
            vehiculos_no_eliminados.append(vehiculos_encontrados[0])
            vehiculos_encontrados.pop()
            break

    guardar_vehiculos(vehiculos_no_eliminados)

    if len(vehiculos_encontrados) == 0:
        print(
            "Si no se ha informado que el vehiculo tiene un viaje asignado o pendiente y por lo tanto no puede ser eliminado, ver este mensaje significa que el vehiculo que se intento eliminar no existe"
        )

    else:
        print("Vehiculo eliminado exitosamente!")


def informe_vehiculo():
    lista_vehiculos = obtener_vehiculos()

    for x in lista_vehiculos:
        print(
            f"Placa: {x[0]}, Modelo: {x[1]}, Estilo: {x[2]}, Año: {x[3]}, Capacidad: {x[4]}"
        )
        print("\n")
