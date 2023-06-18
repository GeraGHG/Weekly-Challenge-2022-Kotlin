'''
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
'''
numero = int(input("Ingrese un número para comprobar si es primo o no: "))
if numero % 2 == 1: print(f"\t\"{numero}\" es primo")
print(f"Los números primos del 1 al 100 son:\n {[x for x in range(1, 101) if x % 2 == 1]}")

