'''
import matematicas

suma_de_numeros = matematicas.suma(1, 2)
print(suma_de_numeros)
resta_de_numeros = matematicas.resta(1, 2)
print(resta_de_numeros)
div_de_numeros = matematicas.div(1, 2)
print(div_de_numeros)
mul_de_numeros = matematicas.mul(1, 2)
print(mul_de_numeros)
'''
from matematicas import suma, resta, div, mul
import time
from time import sleep

num = int(input('ingrese un numero'))
num2 = int(input('ingrese otro numero'))

suma_de_numeros = suma(num, num2)
print(suma_de_numeros)

resta_de_numeros = resta(1, 2)
print(resta_de_numeros)

div_de_numeros = div(1, 2)
print(div_de_numeros)

mul_de_numeros = mul(1, 2)
print(mul_de_numeros)