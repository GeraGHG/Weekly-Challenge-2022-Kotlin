'''
/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */

'''
# primer forma
palabra = "Hola mundo"
palabra_invertida = palabra[::-1]
print(palabra_invertida)

# segunda forma
palbra = "hola"
palabra_nueva = ""
for l in range(len(palbra)- 1, -1, -1):
    palabra_nueva += palbra[l]
print(palabra_nueva)