"""
Crear un programa que pide una nota por consola y valora las posibles calificaciones del alumno siendo suspenso menos de 5, aprobado entre 5 y 7, notable entre 7 y 9 y sobresaliente mayor de 9.
"""
nota=int(input("Introduce tu nota"))

if nota<5:
    print("Suspenso")
elif nota<7:
    print("Aprobado")
elif nota<9:
    print("Notable")
else:
    print("Sobresaliente")