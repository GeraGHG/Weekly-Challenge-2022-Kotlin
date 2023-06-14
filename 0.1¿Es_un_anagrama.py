'''
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
Un Anagrama consiste en formar una palabra reordenando TODAS
las letras de otra palabra inicial.
NO hace falta comprobar que ambas palabras existan.
Dos palabras exactamente iguales no son anagrama.
 */

'''
# def anagrama(string1: str, string2: str) -> bool:
#     if string1 == string2:
#         return False
#     elif len(string1) == len(string2):
#         lista1 = list(string1)
#         lista2 = list(string2)
#         for letra in lista1:
#             if letra in lista2:
#                 lista2.remove(letra)
#             else:
#                 break
#         else:
#             return len(lista2) == 0
#     return False
# print(anagrama("amor", "roma"))

def anagram(palabra1: str, palabra2: str) -> bool:
    if palabra1 == palabra2: return False
    elif sorted(palabra1) == sorted(palabra2): return True
    else: return False
print(anagram("amo", "roma"))
