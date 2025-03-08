class ConjuntoNumeros:
    def __init__(self):
        self.numeros = set()

    def agregar_numero(self, numero):
        self.numeros.add(numero)

    def mostrar_numeros(self):
        print(self.numeros)


# Uso de la clase
conjunto = ConjuntoNumeros()
conjunto.agregar_numero(5)
conjunto.agregar_numero(10)
conjunto.agregar_numero(5)
conjunto.mostrar_numeros()
