#Ecriba un codigo que pueda contar todas las palabras mayusculas de un archivo:

archivo = './ejemplo.txt'

with open(archivo) as fh:
    count = 0
    text = fh.read()

    for character in text:
        if character.isupper():
            count += 1  

print(count)