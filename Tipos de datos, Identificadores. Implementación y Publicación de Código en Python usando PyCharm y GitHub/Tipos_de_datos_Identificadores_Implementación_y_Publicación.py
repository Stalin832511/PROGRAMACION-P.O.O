# Este programa calcula el área y el perímetro de un rectángulo
# utilizando la longitud y el ancho proporcionados por el usuario.
# Además, verifica si el rectángulo es un cuadrado.

def calcular_area(longitud, ancho):
    """
    Calcula el área de un rectángulo.

    Args:
        longitud (float): Longitud del rectángulo.
        ancho (float): Ancho del rectángulo.

    Returns:
        float: El área del rectángulo.
    """
    return longitud * ancho


def calcular_perimetro(longitud, ancho):
    """
    Calcula el perímetro de un rectángulo.

    Args:
        longitud (float): Longitud del rectángulo.
        ancho (float): Ancho del rectángulo.

    Returns:
        float: El perímetro del rectángulo.
    """
    return 2 * (longitud + ancho)


def es_cuadrado(longitud, ancho):
    """
    Verifica si un rectángulo es un cuadrado.

    Args:
        longitud (float): Longitud del rectángulo.
        ancho (float): Ancho del rectángulo.

    Returns:
        bool: True si el rectángulo es un cuadrado, False en caso contrario.
    """
    return longitud == ancho


def main():
    """
    Programa principal que solicita datos del usuario y muestra los resultados.
    """
    print("=== CÁLCULO DE ÁREA Y PERÍMETRO ===")

    # Solicitar entrada del usuario
    longitud = float(input("Ingresa la longitud del rectángulo: "))
    ancho = float(input("Ingresa el ancho del rectángulo: "))

    # Calcular área y perímetro
    area = calcular_area(longitud, ancho)
    perimetro = calcular_perimetro(longitud, ancho)
    es_rectangulo_cuadrado = es_cuadrado(longitud, ancho)

    # Mostrar resultados
    print("\n=== RESULTADOS ===")
    print(f"Área: {area:.2f} unidades cuadradas")
    print(f"Perímetro: {perimetro:.2f} unidades lineales")
    print(f"¿Es un cuadrado?: {'Sí' if es_rectangulo_cuadrado else 'No'}")


if __name__ == "__main__":
    main()
