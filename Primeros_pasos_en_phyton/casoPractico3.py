#Realizar una suma de elementos de una tupla:

test_tup = (7, 8, 9, 1, 10, 7)

print("The original tuple is : " + str(test_tup))

res = sum(list(test_tup))

print("The summation of tuple elements are : " + str(res))