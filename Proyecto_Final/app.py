import registro_vehiculos
import registro_clientes
import registro_viajes


def accion_adicional():
    opcion_accion = input(
        "\n\nDesea realizar alguna accion adicional?\n\n1. Si\n\n2. No\n\n"
    )

    if opcion_accion == "1":
        menu_interno()

    elif opcion_accion == "2":
        print("Finalizando programa.....")
        return
    else:
        print("Ingrese una opcion valida")
        accion_adicional


def menu_vehiculos():
    opcion_Vehiculos = input(
        "\n\n***VEHICULOS***\n\n1. Nuevo\n\n2. Modificar\n\n3. Ver\n\n4. Elimnar\n\n5. Informe\n\n6. Regresar\n\n7. Salir\n\n"
    )

    if opcion_Vehiculos == "1":
        registro_vehiculos.registrar_vehiculo()
        accion_adicional()

    elif opcion_Vehiculos == "2":
        registro_vehiculos.editar_vehiculo()
        accion_adicional()

    elif opcion_Vehiculos == "3":
        vehiculos_encontrados = registro_vehiculos.consultar_vehiculo()
        print(
            f"Placa: {vehiculos_encontrados[0][0]}, Modelo: {vehiculos_encontrados[0][1]}, Estilo: {vehiculos_encontrados[0][2]}, Año: {vehiculos_encontrados[0][3]}, Capacidad: {vehiculos_encontrados[0][4]}\n\n"
        )
        accion_adicional()

    elif opcion_Vehiculos == "4":
        registro_vehiculos.eliminar_vehiculo()
        accion_adicional()

    elif opcion_Vehiculos == "5":
        registro_vehiculos.informe_vehiculo()
        accion_adicional()

    elif opcion_Vehiculos == "6":
        menu_interno()

    elif opcion_Vehiculos == "7":
        return

    else:
        print("Ingrese una opcion valida")
        menu_vehiculos()


def menu_cliente():
    opcion_cliente = input(
        "\n\n***CLIENTES***\n\n1. Nuevo\n\n2. Modificar\n\n3. Ver\n\n4. Eliminar\n\n5. Informe\n\n6. Regresar\n\n7. Salir\n\n"
    )

    if opcion_cliente == "1":
        registro_clientes.registrar_cliente()
        accion_adicional()

    elif opcion_cliente == "2":
        registro_clientes.editar_cliente()
        accion_adicional()

    elif opcion_cliente == "3":
        clientes_encontrados = registro_clientes.consultar_cliente()
        print(f"Id:{clientes_encontrados[0][0]}, Nombre: {clientes_encontrados[0][1]}")
        accion_adicional()

    elif opcion_cliente == "4":
        registro_clientes.eliminar_cliente()
        accion_adicional()

    elif opcion_cliente == "5":
        registro_clientes.informe_cliente()
        accion_adicional()

    elif opcion_cliente == "6":
        menu_interno()

    elif opcion_cliente == "7":
        return

    else:
        print("Ingrese una opcion valida")
        menu_cliente()


def menu_viajes():
    opcion_viajes = input(
        "\n\n***VIAJES***\n\n1. Nuevo\n\n2. Modificar\n\n3. Ver\n\n4. Eliminar\n\n5. Informe\n\n6. Regresar\n\n7.Salir\n\n"
    )

    if opcion_viajes == "1":
        registro_viajes.registrar_viaje()
        accion_adicional()

    elif opcion_viajes == "2":
        registro_viajes.editar_viaje()
        accion_adicional()

    elif opcion_viajes == "3":
        viajes_encontrado = registro_viajes.consultar_viaje()
        print(
            f"ID= {viajes_encontrado[0][0]}, Placa= {viajes_encontrado[0][1]}, Destino= {viajes_encontrado[0][2]}, Capacidad= {viajes_encontrado[0][3]}, Precio= {viajes_encontrado[0][4]}, ID Cliente= {viajes_encontrado[0][5]}, Estado Viaje= {viajes_encontrado[0][6]}"
        )
        accion_adicional()

    elif opcion_viajes == "4":
        registro_viajes.eliminar_viaje()
        accion_adicional()

    elif opcion_viajes == "5":
        registro_viajes.informe_viaje()
        accion_adicional()

    elif opcion_viajes == "6":
        menu_interno()

    elif opcion_viajes == "7":
        return

    else:
        print("Ingrese una opcion valida")
        menu_viajes()


def menu_interno():
    opcion_interna = input(
        "\n\n1. Vehiculos\n\n2. Clientes\n\n3. Viajes\n\n4. Regresar\n\n5. Salir\n\n"
    )

    if opcion_interna == "1":
        menu_vehiculos()

    elif opcion_interna == "2":
        menu_cliente()

    elif opcion_interna == "3":
        menu_viajes()

    elif opcion_interna == "4":
        menu()

    elif opcion_interna == "5":
        return

    else:
        print("Ingrese una opcion valida.")
        menu_interno()


def menu():
    opcion = input(
        "\n\nIndique el numero asociado a la opcion que desea ejecutar.\n\n1. Configuracion\n\n2. Salir\n"
    )

    if opcion == "1":
        menu_interno()

    elif opcion == "2":
        return

    else:
        print("Ingrese una opcion valida.")
        menu()


menu()
