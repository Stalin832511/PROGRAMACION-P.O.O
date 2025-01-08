# Clase para modelar una Habitación en el hotel
class Habitacion:
    def __init__(self, numero, tipo, precio_por_noche):
        """Inicializa los atributos de una habitación."""
        self.numero = numero  # Número de la habitación
        self.tipo = tipo  # Tipo de habitación: Simple, Doble, Suite
        self.precio_por_noche = precio_por_noche  # Precio por noche
        self.ocupada = False  # Estado: False = Disponible, True = Ocupada

    def __str__(self):
        """Devuelve una representación legible de la habitación."""
        estado = "Ocupada" if self.ocupada else "Disponible"
        return f"Habitación {self.numero} ({self.tipo}): ${self.precio_por_noche}/noche - {estado}"

# Clase para modelar una Reserva
class Reserva:
    def __init__(self, huesped, habitacion, noches):
        """Inicializa los atributos de una reserva."""
        self.huesped = huesped  # Nombre del huésped
        self.habitacion = habitacion  # Objeto de clase Habitacion
        self.noches = noches  # Número de noches de la estadía
        self.costo_total = self.calcular_costo_total()  # Costo de la reserva
        habitacion.ocupada = True  # Marca la habitación como ocupada

    def calcular_costo_total(self):
        """Calcula el costo total de la reserva."""
        return self.noches * self.habitacion.precio_por_noche

    def __str__(self):
        """Devuelve una representación legible de la reserva."""
        return (f"Reserva de {self.huesped}: {self.habitacion.tipo}, "
                f"Habitación {self.habitacion.numero}, "
                f"{self.noches} noches, Total: ${self.costo_total}")

# Clase principal para gestionar el sistema de reservas
class SistemaReservas:
    def __init__(self):
        """Inicializa el sistema con una lista de habitaciones y reservas."""
        self.habitaciones = []  # Lista de objetos Habitacion
        self.reservas = []  # Lista de objetos Reserva

    def agregar_habitacion(self, habitacion):
        """Agrega una nueva habitación al sistema."""
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        """Muestra todas las habitaciones disponibles."""
        print("Habitaciones disponibles:")
        for habitacion in self.habitaciones:
            if not habitacion.ocupada:
                print(habitacion)

    def crear_reserva(self, huesped, numero_habitacion, noches):
        """Crea una nueva reserva para un huésped."""
        for habitacion in self.habitaciones:
            if habitacion.numero == numero_habitacion and not habitacion.ocupada:
                nueva_reserva = Reserva(huesped, habitacion, noches)
                self.reservas.append(nueva_reserva)
                print(f"Reserva creada con éxito para {huesped}.")
                return
        print("Error: La habitación no está disponible o no existe.")

    def mostrar_reservas(self):
        """Muestra todas las reservas activas."""
        print("Reservas activas:")
        for reserva in self.reservas:
            print(reserva)

# Programa principal para usar las clases
if __name__ == "__main__":
    # Crear el sistema de reservas
    sistema = SistemaReservas()

    # Agregar habitaciones
    sistema.agregar_habitacion(Habitacion(101, "Simple", 50))
    sistema.agregar_habitacion(Habitacion(102, "Doble", 75))
    sistema.agregar_habitacion(Habitacion(201, "Suite", 120))

    # Mostrar habitaciones disponibles
    sistema.mostrar_habitaciones_disponibles()

    # Crear reservas
    sistema.crear_reserva("Juan Pérez", 102, 3)
    sistema.crear_reserva("María López", 201, 2)

    # Intentar reservar una habitación ocupada
    sistema.crear_reserva("Carlos Ruiz", 102, 1)

    # Mostrar habitaciones disponibles después de las reservas
    sistema.mostrar_habitaciones_disponibles()

    # Mostrar reservas activas
    sistema.mostrar_reservas()
