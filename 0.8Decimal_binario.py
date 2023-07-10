# numero = int(input("Ingrese un número decimal y el programa lo combierte en binario: "))
# potencias = {
#     1: "2**0",
#     2: "2**1",
#     4: "2**2",
#     8: "2**3",
#     16: "2**4",
#     32: "2**5",
#     64: "2**6",
#     128: "2**7",
#     256: "2**8",
#     512: "2**9",
#     1024: "2**10" 
# }
# resultado = []
# claves = sorted(potencias.keys(), reverse=True)
# for clave in claves:
#     if numero >= clave:
#         resultado.append("1")
#         numero -= clave
#     else:
#         resultado.append("0")
# binario = "".join(resultado)
# print(f"El número {numero} en binario es: {binario}")


numero = int(input("Ingrese un número decimal y el programa lo convierte en binario: "))
binario = ""
while numero > 0:
    uno_cero = numero % 2
    binario = str(uno_cero) + binario
    numero = numero // 2
print("El número en binario es:", binario)


    
