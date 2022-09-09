# micro-mini-banco virtual.
import csv
import time

def obtener_cuentas():
    cuentas = []
    archivo = open("cuentas.csv", "r")
    print("Leyendo info de sistema.")
    time.sleep(2)
    archivo_csv_leido = csv.reader(archivo)
    primera_linea = True

    for nro_de_cuenta, titular, saldo, activa in archivo_csv_leido:
        if not primera_linea:
            # Con el False, entran 
            cuentas.append([nro_de_cuenta, titular, saldo, activa])
        else:
            # primera vez, entra acá y cambio a False
            # para poder omitir la 1° linea
            primera_linea = False
    archivo.close()
    print("Info procesada... Aplicando débito.")
    time.sleep(2)

    # -------------------------
    fl = True
    gastos_discount = {}
    gastos = open("gastos.csv", "r")
    gastos_csv = csv.reader(gastos)
    for cta,importe in gastos_csv:
        if not fl:
            gastos_discount[cta] = importe
        else:
            fl = False
    gastos.close()
    cuentas_actualizadas = []
    cuentas_actualizadas.append(['nro_de_cuenta', 'titular', 'saldo', 'activa'])
    for cta in cuentas:
        nro_cta = cta[0]
        saldo = float(cta[2])
        gastos = float(gastos_discount.get(nro_cta, None))
        saldo_restante = saldo - gastos
        cuentas_actualizadas.append([nro_cta, cta[1], str(saldo_restante), cta[3]])
    print("Cuentas actlualizadas")
    time.sleep(3)
    return cuentas_actualizadas


def guardar_cuentas(cuentas_actualizadas):
    archivo_final = open("cuentas_actualizadas.csv", "w")
    archivo_final_csv = csv.writer(archivo_final)
    archivo_final_csv.writerows(cuentas_actualizadas)
    archivo_final.close()
    print("Información actualizada correctamente.")

if __name__ == '__main__':
    ctas = obtener_cuentas()
    guardar_cuentas(ctas)