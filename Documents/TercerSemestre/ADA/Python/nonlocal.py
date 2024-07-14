from array import *
# def counter():
#     num = 0
#     def incrementer():
#         num += 1
#         return num
#     return incrementer

# def counter():
#     num = 0
#     def incrementer():
#         nonlocal num
#         num += 1
#         return num
#     return incrementer()
# c = counter()
# print(c())

restaurants = ["McDonald's", "Burger King", "McDonald's", "Chicken Chicken"]
print(restaurants)
restaurantes = set(restaurants)
print(restaurantes)
unique_restaurants = set(restaurants)
print(list(restaurantes))
print(unique_restaurants)
print('1'+'0')

#Es una potencia 2**2+1
print(2<<2)

# Esto me da la cantidad de numeros que existen en el  array 
my_array = array('i', [1,2,3,3,5])
print(my_array.count(5))

my_array = array('i', [1,2,3,3,5])
print(my_array[2])

# los arreglos multidimensionales son dificiles de crear por que no los puedes crear como decirlo vacios
n = int(input('Da el numero de filas y columna que quieras crear'))
Array_multidimensional = [[0 for _ in range(n)] for _ in range(n)]



