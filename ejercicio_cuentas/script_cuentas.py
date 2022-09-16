import proceso_cuentas

def imprimir_cuentas(cuentas):
    for cuenta in cuentas:
        print("{} : {} : {}".format(
            cuenta[0],
            cuenta[1],
            cuenta[2]
        ))

def aplicar_gastos(cuentas, cuenta, monto):
    for c in cuentas:
        if c[0] == cuenta:
            total = float(c[2]) - monto
            if total < 0:
                print('Gasto todo el dinero, por favor recargar cuenta !!!!!\n'*3)
            c[2] = str(total)
            break
    return cuentas

def procesar_gastos(cuentas):
    archivo = open("gastos.csv")
    primera_linea = True
    for linea in archivo:
        if not primera_linea:
            nro_de_cuenta, importe_gasto = linea.replace('\n', '').split(',')
            importe_gasto_float = float(importe_gasto)
            cuentas_actualizadas = aplicar_gastos(cuentas, nro_de_cuenta, importe_gasto_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas

def aplicar_depositos(cuentas, nro_cuenta, deposito):
    for cuenta in cuentas:
        if cuenta[0] == nro_cuenta:
            cuenta[2] = str(float(cuenta[2]) + deposito)
            break
    return cuentas

def procesar_depositos(cuentas):
    archivo = open("depositos.csv")
    primera_linea = True
    for linea in archivo:
        if not primera_linea:
            nro_cuenta, monto_deposito = linea.replace('\n', '').split(',')
            importe_deposito_float = float(monto_deposito)
            cuentas_actualizadas = aplicar_depositos(cuentas, nro_cuenta, importe_deposito_float)
        else:
            primera_linea = False
    archivo.close()
    return cuentas_actualizadas


def main():
    print('Obteniendo cuentas . . . ')
    cuentas = proceso_cuentas.obtener_cuentas()
    imprimir_cuentas(cuentas)

    print('Aplicando gastos . . . ')
    cuentas_actualizadas = procesar_gastos(cuentas)
    imprimir_cuentas(cuentas_actualizadas)

    print('Aplicando depositos . . .')
    cuentas_actualizadas_ = procesar_depositos(cuentas)
    imprimir_cuentas(cuentas_actualizadas_)



if __name__ == '__main__':
    main()