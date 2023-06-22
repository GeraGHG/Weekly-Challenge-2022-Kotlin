'''
Crea una única función (importante que sólo sea una) que sea capaz
de calcular y retornar el área de un polígono.
- La función recibirá por parámetro sólo UN polígono a la vez.
- Los polígonos soportados serán Triángulo, Cuadrado y Rectángulo.
- Imprime el cálculo del área de un polígono de cada tipo.

'''
def poligono(poligono: str):
    poligono = poligono.lower()
    area_triangulo = lambda base, altura: (base * altura) / 2
    area_cuadrado = lambda lado: pow(lado, 2)
    area_rectangulo = lambda largo, ancho: largo * ancho

    match poligono:
        case "triángulo", "triangulo":
            base = int(input("Ingrese la \"base\" del triángulo: "))
            altura = int(input("Ingrese la \"altura\" del triángulo: "))
            print(f"El área del triángulo es: {area_triangulo(base, altura)}")
        case "cuadrado":
            lado = int(input("Ingrese un \"lado\" del cuadrado: "))
            print(f"El área del cuadrado es: {area_cuadrado(lado)}")
        case "rectángulo", "rectangulo":
            largo = int(input("Ingrese el \"largo\" del rectángulo: "))
            ancho = int(input("Ingrese el \"ancho\" del rectángulo: "))
            print(f"El área del rectángulo es: {area_rectangulo(largo, ancho)}")
        case _:
            print("Polígono no reconocido")

poligono("CUADRADO")



