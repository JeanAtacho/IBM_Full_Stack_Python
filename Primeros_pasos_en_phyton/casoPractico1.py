#Dado dos numero, escriba un codigo en python para encontrar el minimo de estos dos numeros:

def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

a = 2
b = 4

print(minimum(a, b))

def minimum(a, b):
    if a <= b:
        return a
    else:
        return b

a = -1
b = -4

print(minimum(a, b))