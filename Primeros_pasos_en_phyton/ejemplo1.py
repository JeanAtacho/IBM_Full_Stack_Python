"""
#Realizar un programa sencillo que pida una nota por consola y evalue si el alumno ha aprobado o no en funcion de dicha nota es al menos un 5
"""

notaIn=int(input("Introduzca nota:"))

if notaIn<5:
    calificacion="Suspenso"
else: calificacion="Aprobado"

print(calificacion)