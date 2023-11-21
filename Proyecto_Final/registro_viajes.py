import registro_vehiculos
import registro_clientes


viajes = "Proyecto_Final/viajes.txt"


def agregar_viaje(id, placa, destino, capacidad, precio, id_cliente, estado_viaje):
    with open(viajes, "a") as file:
        file.write(
            f"{id},{placa},{destino},{capacidad},{precio},{id_cliente},{estado_viaje}\n"
        )


def registrar_viaje():
    print(
        "\nHola! Bienvenido a Auto Transportes La Unión, por favor ingrese los siguientes datos para registrar el viaje.\n"
    )
    id = input("Ingrese el ID del viaje: \n").lower()
    id_cliente = input("Ingrese el ID del usuario: \n").lower()
    destino = input("Ingrese el destino del viaje: \n").lower()
    precio = int(input("Ingrese el precio del tiquete pata este viaje: \n"))
    estado_viaje = "Pendiente"

    datos_vehiculo = registro_vehiculos.consultar_vehiculo()

    placa = datos_vehiculo[0][0]
    capacidad = int(
        input(
            f"Su vehiculo cuenta con {datos_vehiculo[0][4]} asientos, ingrese la cantidad de tiquetes que desea reservar: \n"
        )
    )

    while capacidad > int(datos_vehiculo[0][4]):
        print(
            f"La cantidad de tiquetes reservados es mayor que la cantidad disponible de asientos en el vehiculo: {datos_vehiculo[4]}"
        )

        capacidad = int(input("Ingrese la cantidad de tiquetes que desea reservar: \n"))

    agregar_viaje(id, placa, destino, capacidad, precio, id_cliente, estado_viaje)


def obtener_viaje():
    with open(viajes, "r") as file:
        lineas = [linea.strip().split(",") for linea in file.readlines()]

    return lineas


def guardar_viaje(lista_viajes):
    with open(viajes, "w") as file:
        for x in lista_viajes:
            file.write(f"{x[0]},{x[1]},{x[2]},{x[3]},{x[4]},{x[5]},{x[6]},\n")


def consultar_viaje():
    lista_viajes = obtener_viaje()
    id = input("Inserte ID del viaje: \n").lower()
    viajes_encontrados = []

    for x in lista_viajes:
        if x[0] == id:
            viajes_encontrados.append(x)

    if len(viajes_encontrados) == 0:
        print("No se encontro ningun viaje con el ID indicado")

    else:
        return viajes_encontrados


def editar_viaje():
    lista_viajes = obtener_viaje()
    id = input("Inserte el ID del viaje: \n").lower()
    viajes_encontrados = []

    for x in lista_viajes:
        if x[0] == id:
            print("Inserte el nuevo estado del viaje: \n")
            x[6] = input("Indique si el viaje ha sido Finalizado (Si/No):  ").lower()

            if x[6] == "si":
                x[6] = "Finalizado"
            elif x[6] == "no":
                x[6] = "Pendiente"
            else:
                print("Favor ingresar una opcion valida")

            viajes_encontrados.append(x)

    guardar_viaje(lista_viajes)

    if len(viajes_encontrados) == 0:
        print("No se encontro ningun viaje con el id indicad0.")


def eliminar_viaje():
    lista_viajes = obtener_viaje()
    viajes_no_eliminados = []
    id = input("Inserte el ID del viaje: \n").lower()
    viajes_encontrados = []

    for x in lista_viajes:
        if x[0] == id and x[6] == "Finalizado":
            print("No es posible eliminar el viaje ya que ya fue Finalizado")

        else:
            for x in lista_viajes:
                if x[0] == id:
                    viajes_encontrados.append(x)

            for x in lista_viajes:
                if x[0] != id:
                    viajes_no_eliminados.append(x)

            lista_viajes = viajes_no_eliminados

            guardar_viaje(lista_viajes)

            if len(viajes_encontrados) == 0:
                print("No se encontro ningun vehiculo con la placa indicada.")

            else:
                print("Viaje eliminado exitosamente!")


def informe_viaje():
    detalles_viaje = consultar_viaje()
    id_cliente = detalles_viaje[0][5]
    placa = detalles_viaje[0][1]
    destino = detalles_viaje[0][2]
    costo = int(detalles_viaje[0][3]) * int(detalles_viaje[0][4])

    detalles_auto = registro_vehiculos.consultar_vehiculo_informe(placa)

    marca = detalles_auto[1]
    estilo = detalles_auto[2]

    detalles_cliente = registro_clientes.consultar_cliente_informe(id_cliente)

    nombre = detalles_cliente[1]

    print(
        f"\n\nLa placa del vehiculo es {placa}. Es un {marca}, modelo {estilo}.\n\nNombre del cliente: {nombre}\n\nDestino {destino}\n\nEl costo del viaje fue de {costo}"
    )


def lista_viajes():
    lista_viajes = obtener_viaje()
    viajes_encontrados = []

    for x in lista_viajes:
        viajes_encontrados.append(x)

    return viajes_encontrados
