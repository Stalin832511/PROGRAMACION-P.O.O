class Personaje:

    def __init__(self, nombre, fuerza, destreza, resistencia, vida):
        self.nombre = nombre
        self.fuerza = fuerza
        self.destreza = destreza
        self.resistencia = resistencia
        self.vida = vida

    def atributos(self):
        print(f"\n{self.nombre}:")
        print(f"· Fuerza: {self.fuerza}")
        print(f"· Destreza: {self.destreza}")
        print(f"· Resistencia: {self.resistencia}")
        print(f"· Vida: {self.vida}")

    def esta_vivo(self):
        return self.vida > 0

    def recibir_daño(self, daño):
        daño_real = max(daño - self.resistencia, 0)
        self.vida -= daño_real
        print(f"{self.nombre} recibe {daño_real} puntos de daño.")
        if not self.esta_vivo():
            print(f"{self.nombre} ha caído en combate.")

    def curar(self, cantidad):
        self.vida += cantidad
        print(f"{self.nombre} recupera {cantidad} puntos de vida. Vida actual: {self.vida}")


class Cazador(Personaje):

    def __init__(self, nombre, fuerza, destreza, resistencia, vida, arco):
        super().__init__(nombre, fuerza, destreza, resistencia, vida)
        self.arco = arco

    def atributos(self):
        super().atributos()
        print(f"· Arco: {self.arco} de daño base")

    def atacar(self, enemigo):
        daño = self.destreza * self.arco
        print(f"{self.nombre} dispara una flecha causando {daño} de daño.")
        enemigo.recibir_daño(daño)


class Hechicero(Personaje):

    def __init__(self, nombre, fuerza, destreza, resistencia, vida, poder_magico):
        super().__init__(nombre, fuerza, destreza, resistencia, vida)
        self.poder_magico = poder_magico

    def atributos(self):
        super().atributos()
        print(f"· Poder Mágico: {self.poder_magico}")

    def lanzar_hechizo(self, enemigo):
        daño = self.poder_magico * 2
        print(f"{self.nombre} lanza un hechizo causando {daño} de daño.")
        enemigo.recibir_daño(daño)

    def curar_aliado(self, aliado):
        cantidad_cura = self.poder_magico * 3
        print(f"{self.nombre} lanza un hechizo de curación.")
        aliado.curar(cantidad_cura)


def combate(jugador_1, jugador_2):
    turno = 1
    while jugador_1.esta_vivo() and jugador_2.esta_vivo():
        print(f"\n--- Turno {turno} ---")
        if turno % 2 == 1:
            print(f"{jugador_1.nombre} ataca.")
            jugador_1.atacar(jugador_2)
        else:
            print(f"{jugador_2.nombre} ataca.")
            jugador_2.lanzar_hechizo(jugador_1)
        turno += 1

    if jugador_1.esta_vivo():
        print(f"\n{jugador_1.nombre} es el vencedor.")
    elif jugador_2.esta_vivo():
        print(f"\n{jugador_2.nombre} es el vencedor.")
    else:
        print("\nAmbos combatientes han caído. Es un empate.")


# Crear los personajes
cazador = Cazador("Robin", fuerza=10, destreza=15, resistencia=5, vida=100, arco=4)
hechicero = Hechicero("Merlín", fuerza=5, destreza=8, resistencia=4, vida=100, poder_magico=6)

# Mostrar atributos
cazador.atributos()
hechicero.atributos()

# Iniciar combate
combate(cazador, hechicero)
