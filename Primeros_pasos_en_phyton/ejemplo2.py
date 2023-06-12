"""
Crear un programa que pide una edad por consola y valora si el usuario es mayor de edad o no en funcion de si dicha variable es menor de 18 se mostrara un mensaje prohibiendo la entrada, si es mayor de 18 se admitira. Ademas, en el caso de que la edad indtroducida sea mayor que 100 se considerara erronea.
"""
edad=int(input("Introduce edad:"))

if edad<18:
    print("No puedes pasar")
elif edad>100:
    print("Edad incorrecta")
else:
    print("Adelante")