'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''

def es_primo(n):
    if n == 0: return False
    for i in range(2, n):
        if n % i == 0: return False
    return True

def rango_numeros(m):
    lista_numeros_primos = [1]
    for i in range(2, m):
        if es_primo(i):
            lista_numeros_primos.append(i)
    print(lista_numeros_primos)

rango_numeros(100)