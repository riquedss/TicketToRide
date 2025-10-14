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
        # mais tarde.
        pass
