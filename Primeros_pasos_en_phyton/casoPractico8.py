#Escriba un programa para producir la serie Fibonacci en Python:

n=int(input("Introduzca el numero de valores de 'n' : "))
first=0
second=1
sum=0
count=1
print("Secuencia de Fibonacci: ")
while(count<=n):
    print(sum)
    count+=1
    first=second
    second=sum
    sum=first+second