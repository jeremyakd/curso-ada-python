def is_True():
    # pass
    pass

pepe = 'pepe argento'

"""
hola
hola
"""

# Lista
lista_de_mercado = [ 'leche','azucar',1000 ]

lista_de_mercado[1] = 'Pan'

# ----------------------------------------------------
# Trampa

lista_de_mercado_tuple = ( 'leche','azucar', )
lista_de_mercado_tuple[1] = 'Pan' # Error

# Me creo una lista de la tupla
lista_lista_de_mercado_tupla = list(lista_de_mercado_tuple)
# lista_de_mercado_tuple = [ 'leche','azucar', ]

# Modifico la lista
lista_lista_de_mercado_tupla[1] = 'Pan'

# [ 'leche','Pan', ]

# Lo convierto de vuelta en tupla

lista_lista_de_mercado_tupla_a_tupla = tuple(lista_lista_de_mercado_tupla)

# Me queda la tupla ( 'leche','Pan', )

lista_de_mercado = set([ 'leche','azucar', 'leche' ])
# [ 'leche','azucar']

my_dict = {
    'key':'value',
    'key':
        {
            'key':'value',
        }
}

