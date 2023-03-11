'''Escribir una función que reciba el nombre del usuario y después muestre por pantalla
<NOMBRE> tiene <n> letras, donde <NOMBRE> es el nombre de usuario en
mayúsculas y <n> es el número de letras que tienen el nombre.'''

def contar_letras(nombre):
    nombre_may = nombre.upper()
    num_letras = len(nombre)

    print(f"{nombre_may} tiene {num_letras} letras.")
contar_letras("Goku")