
def validar_edad(edad):
    if edad >= 18:
        print("Te dejo pasar.")
    else:
        print("Voy a llamar a tu mamá")

def principal():
    edad_user = input("Ingrese su edad por favor. ")
    try:
        edad_int = int(edad_user)
        validar_edad(edad_int)
    except Exception as error:
        print("No ingresó un numero.")

if __name__ == '__main__':
    principal()