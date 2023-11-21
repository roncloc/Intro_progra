x=0

total_salarios = 0

salario_500_todos_empleados = 7500

while x < 15:
    salario_empleado = int(input(f"Indique el salario de su empleado {x + 1}: "))

    if salario_empleado < 500 and salario_empleado > 0:
        total_salarios += salario_empleado
        x+= 1
    elif salario_empleado >= 500:
        salario_500_todos_empleados -= 500
        x+= 1
    else:
        print("Por favor indique un salario valido")



print(f"La suma total de los salarios de todos los empleados que ganan menos de $500 es: {total_salarios}, para que todos estos empleados ganen al menos $500 se necesita {salario_500_todos_empleados - total_salarios} ")