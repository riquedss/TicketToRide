from typing import List
from carta import CartaRota, CartaTrem
        
class Jogador:
    def __init__(self, num: int):
        self.num = num
        self.cartasRota: List[CartaRota] = []
        self.cartasTrem: List[CartaTrem] = []
        self.pontos = 0

    def descartar_rota(self, descartada: CartaRota) -> CartaRota:
        # mais tarde.
        pass

    def comprar_carta(self):
        print("Comprando carta")

    def mostrar_cartas(self):
        print("\nCartas de Trem na sua mão:")
        for i, c in enumerate(self.cartasTrem, 1):
            print(f"Trem {i}: {c.cor.value}")

        print("\nCartas de Rota na sua mão:")
        for i, c in enumerate(self.cartasRota, 1):
            cores = [c2.value for c2 in c.requisitos]
            if len(cores) > 1:
                requisitos = ", ".join(cores[:-1]) + " e " + cores[-1]
            else:
                requisitos = cores[0]
            print(f"Rota {i}: {requisitos}")

    def set_cartas_trem(self, cartas):
        self.cartasTrem = cartas
        
    def set_cartas_rota(self, cartas):
        self.cartasRota = cartas
