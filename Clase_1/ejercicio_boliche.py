# Solicito al user su edad
# Y con el int, convierto lo que ingresa en numero entero
edad = int(input("Ingrese su edad por favor. "))

# Imprimo su edad
print(type(edad))
# type imprime el tipo de variable

# Condiciono el valor de la variable edad

if edad > 60:
    print('Anda a tu casa anciano')
elif edad >= 18: # Si es verdad
    print("Te dejo pasar.")
else:
    print("Voy a llamar a tu mamá")
