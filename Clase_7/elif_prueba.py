numero = int(input('Ingrese dia de la semana: '))
clima = 'nublado'


if numero == 1:
    print("Lunes")
elif numero == 2:
    print("Martes")
    if clima == 'soleado':
        print('Tengamos la clase en la plaza')
    print('tenemos la clase igual')
    
elif numero == 3:
    print("Miercoles")
elif numero == 4:
    print("Jueves")
elif numero == 5:
    print("Viernes")
elif numero == 6:
    print("Sabado")
elif numero == 7:
    print("Domingo")