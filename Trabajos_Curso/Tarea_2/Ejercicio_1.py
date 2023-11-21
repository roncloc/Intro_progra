cantidad_estudiantes = int(input("Ingrese la cantidad de estudiantes cuyas notas van a ser analizadas: "))

notas_0_50 = 0
notas_51_60 = 0
notas_61_70 = 0
notas_71_100 = 0
total_notas = 0

x = 1

while x < cantidad_estudiantes + 1:
    nota_estudiante = int(input(f"Ingrese la nota del estudiante {x}: "))

    if nota_estudiante >= 0 and nota_estudiante <= 50:
        notas_0_50 += 1
        x += 1

    elif nota_estudiante > 50 and nota_estudiante <= 60:
        notas_51_60 += 1
        x += 1

    elif nota_estudiante > 60 and nota_estudiante <= 70:
        notas_61_70 += 1
        x += 1

    elif nota_estudiante > 70 and nota_estudiante <= 100:
        notas_71_100 += 1
        x += 1
    
    else:
        print("Por favor ingrese una nota valida")

    total_notas += nota_estudiante



print(f"Las calificaciones entre 0 y 50 fueron: {notas_0_50}\nLas calificaciones entre 51 y 60 fueron: {notas_51_60}\nLas calificaciones entre 61 y 70 fueron: {notas_61_70}\nLas calificaciones entre 71 y 100 fueron: {notas_71_100}\nEl promedio de todas las notas fue {total_notas / cantidad_estudiantes}")