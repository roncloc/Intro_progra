semana = [
    ["lunes", "monday"],
    ["martes", "tuesday"],
    ["miercoles", "wednesday"],
    ["jueves", "thursday"],
    ["viernes", "friday"],
    ["sabado", "saturday"],
    ["domingo", "sunday"],
]

mes = [
    ["enero", "january"],
    ["febrero", "february"],
    ["marzo", "march"],
    ["abril", "april"],
    ["mayo", "may"],
    ["junio", "june"],
    ["julio", "july"],
    ["agosto", "august"],
    ["setiembre", "september"],
    ["octubre", "october"],
    ["noviembre", "november"],
    ["diciembre", "december"],
]

dia_usuario = input("Que dia de la semana quieres traducir?\n\n").lower()
mes_usuario = input("\nQue dia del mes quieres traducir?\n\n").lower()

output_ingles = []

for x in semana:
    if dia_usuario == x[0]:
        output_ingles.append(x[1])

for x in mes:
    if mes_usuario == x[0]:
        output_ingles.append(x[1])

print(
    f"\n\nLa traducción del día de la semana es {output_ingles[0].title()}\nLa traducción del mes es  {output_ingles[1].title()}"
)
