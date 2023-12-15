import registro_viajes

clientes = "Proyecto_Final/clientes.txt"


def agregar_cliente(id, nombre):
    with open(clientes, "a") as file:
        file.write(f"{id},{nombre}\n")


def registrar_cliente():
    print(
        "\nHola! Bienvenido a Auto Transportes La Unión, por favor ingrese los siguientes datos para registrar al cliente.\n"
    )
    id = input("Id: ").lower()
    nombre = input("Nombre: ").lower()

    agregar_cliente(id, nombre)


def obtener_cliente():
    with open(clientes, "r") as file:
        lineas = [linea.strip().split(",") for linea in file.readlines()]

    return lineas


def guardar_cliente(lista_clientes):
    with open(clientes, "w") as file:
        for x in lista_clientes:
            file.write(f"{x[0]},{x[1]}\n")


def consultar_cliente():
    lista_clientes = obtener_cliente()
    id = input("Inserte el ID del usuario: \n").lower()
    clientes_encontrados = []

    for x in lista_clientes:
        if x[0] == id:
            clientes_encontrados.append(x)

    if len(clientes_encontrados) == 0:
        print("No se encontro ningun vehiculo con la placa indicada")

    else:
        return clientes_encontrados
        print(f"Id:{clientes_encontrados[0][0]}, Nombre: {clientes_encontrados[0][1]}")


def consultar_cliente_informe(id_cliente):
    lista_clientes = obtener_cliente()
    id = id_cliente

    for x in lista_clientes:
        if x[0] == id:
            return x


def editar_cliente():
    lista_clientes = obtener_cliente()
    id = input("Inserte el id del cliente: \n").lower()
    clientes_encontrados = []

    for x in lista_clientes:
        if x[0] == id:
            print("Inserte los nuevos valores del cliente: \n")
            x[1] = input("Nombre: ").lower()
            clientes_encontrados.append(x)

    guardar_cliente(lista_clientes)

    if len(clientes_encontrados) == 0:
        print("No se encontro ningun cliente con el ID indicado.")


def eliminar_cliente():
    viajes_encontrados = registro_viajes.lista_viajes()
    lista_clientes = obtener_cliente()
    clientes_no_eliminados = []
    id = input("Inserte el id del cliente: \n").lower()
    clientes_encontrados = []

    for x in lista_clientes:
        if x[0] == id:
            clientes_encontrados.append(x)

        else:
            clientes_no_eliminados.append(x)

    for x in viajes_encontrados:
        if id == x[5]:
            print(
                "Lo siento no podemos eliminar el cliente ya que tiene un viaje pendinte de realizar o ya se le realizo uno."
            )

            clientes_no_eliminados.append(clientes_encontrados[0])
            clientes_encontrados.pop()
            break

    guardar_cliente(clientes_no_eliminados)

    if len(clientes_encontrados) == 0:
        print(
            "Si no se ha informado ya que el cliente tiene un viaje asignado o pendiente y por lo tanto no puede ser eliminado, ver este mensaje significa que el vehiculo que se intento eliminar no existe"
        )
    else:
        print("Cliente eliminado exitosamente!")


def informe_cliente():
    lista_clientes = obtener_cliente()

    for x in lista_clientes:
        print(f"Id:{x[0]}, Nombre: {x[1]}")
        print("\n")
