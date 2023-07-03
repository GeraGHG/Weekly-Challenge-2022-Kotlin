oracion = input("Escriba una oración: ")
palabra_usuario = input("Escriba una palabra que se encuentre en la oración para saber cuántas veces se repite: ")
oracion_lower = oracion.lower()
palabra_usuario_lower = palabra_usuario.lower()

contador = 0
palabras = oracion_lower.split()

for palabra in palabras:
    if palabra == palabra_usuario_lower:
        contador += 1

print(f"La palabra '{palabra_usuario}' se repite {contador} veces en la oración.")
