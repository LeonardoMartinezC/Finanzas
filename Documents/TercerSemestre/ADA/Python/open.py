import os
import sys
import fileinput
# Primer paso debemos pedir la ruta donde estara el archivo que queremos leer
archivo = input("Dame la ruta del archivo:\nRuta==:")
# Solo se puede montar en archivos con txt
with open(archivo,'r') as file:
    lines = file.read()
    

    print(lines)
texto  = input("Que quieres agregar al texto::")

# Con esta funcion solo podemos sobre escribir en el archivo 

with open(archivo,'a') as file:
    file.write('\n')
    file.write(texto)
    file.close()

# queremos cambiar la funcion de arriba para que solo agregue archivos cada que se corra este programa
# con sys podemos mdar entradas con line
# Este se parece al stdin de C que igual podias escribir en el archivo

# print("Escribe un texto con sys.stdin ")
# for line in sys.stdin:
#     print(line)

# # Ahora probaremos el file inut para que propcese nuestra entrada y vaya sobre escribiendo en el archivo
# for line in fileinput.input():
#     fileinput.process(line)



