# Función para ingresar las temperaturas diarias
def ingresar_temperaturas():
    temperaturas = []
    for i in range(7):  # Para 7 días de la semana
        temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
        temperaturas.append(temperatura)
    return temperaturas

# Función para calcular el promedio semanal
def calcular_promedio(temperaturas):
    return sum(temperaturas) / len(temperaturas)

# Función principal que organiza el flujo del programa
def main():
    temperaturas = ingresar_temperaturas()
    promedio = calcular_promedio(temperaturas)
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()


# Definición de la clase Clima
class Clima:
    def __init__(self):
        self.temperaturas = []

    # Método para ingresar las temperaturas diarias
    def ingresar_temperaturas(self):
        for i in range(7):  # Para 7 días de la semana
            temperatura = float(input(f"Ingrese la temperatura del día {i+1}: "))
            self.temperaturas.append(temperatura)

    # Método para calcular el promedio semanal
    def calcular_promedio(self):
        return sum(self.temperaturas) / len(self.temperaturas)

# Función principal que organiza el flujo del programa
def main():
    clima = Clima()  # Crear un objeto de la clase Clima
    clima.ingresar_temperaturas()  # Ingresar las temperaturas
    promedio = clima.calcular_promedio()  # Calcular el promedio
    print(f"El promedio semanal de las temperaturas es: {promedio:.2f}°C")

if __name__ == "__main__":
    main()
