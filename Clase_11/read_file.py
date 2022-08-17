archivo = open("archivo.txt")
"""
linea = archivo.readline()

while linea != '':
    print(linea)
    linea = archivo.readline()

for linea in archivo:
    print(linea)
"""
lineas = archivo.readlines()
print(lineas[0])
print(lineas[-1])

archivo.close()