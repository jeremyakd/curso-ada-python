# Lista de reproducción
'''
Crear un programa que pida al usuario ingresar, por separado, 
el nombre de una playlist y el título de tres canciones, 
y al finalizar se muestre un mensaje que diga, p. ej.:
 "Se ha creado la playlist 'Hits de los 80s' con las canciones 'Africa', 'Maniac', 'Final Countdown'".
'''

playlist = input("Ingrese nombre de la playlist por favor: ")

cancion_1 = input("Ingrese nombre de la cancion por favor: ")
cancion_2 = input("Ingrese nombre de la cancion por favor: ")
cancion_3 = input("Ingrese nombre de la cancion por favor: ")

print("Se ha creado la playlist {} con las canciones {}, {}".format(playlist, cancion_1, cancion_2)) 
