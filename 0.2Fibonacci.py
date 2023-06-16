'''
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...

'''
def fibonacci(n):
    a, b = 0, 1
    lista = list()
    while(a < n):
        lista.append(a)
        a, b = b, a+b
    print(lista)

def fibonacci2(x):
    a = 0
    b = 1
    aux = a + b
    lista = []
    while a < x:
        lista.append(a)
        aux = a + b
        a = b
        b = aux
    print(lista)
fibonacci(50)
fibonacci2(50)