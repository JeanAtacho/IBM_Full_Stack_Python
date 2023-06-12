#Escribir un programa en Python para comprobar si un número es capicúa. Es decir, si se lee igual de derecha a izquierda que de izquierda a derecha.

a=input("introduzca un numero: ")
b=a[::-1]
if a==b:
    print("Es capicua")
else:
    print("No es capicua")