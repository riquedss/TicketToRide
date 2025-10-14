from typing import List
from carta import CartaRota, CartaTrem, Carta

class Mao:
    def __init__(self):
        self.cartasRota: List[CartaRota] = []
        self.cartasTrem: List[CartaTrem] = []
        
class Jogador:
    def __init__(self, num: int):
        self.num = num
        self.mao = Mao()
        self.pontos = 0

    def descartar_rota(self, descartada: CartaRota) -> CartaRota:
        if descartada in self.mao.cartasRota:
            self.mao.cartasRota.remove(descartada)
            return descartada
        return None

    def comprar_carta(self, carta: Carta):
        if isinstance(carta, CartaTrem):
            self.mao.cartasTrem.append(carta)

    def mostrar_cartas(self):
        print(f"Jogador {self.num} - Cartas de Trem: {[c.cor.value for c in self.mao.cartasTrem]}")
        print(f"Jogador {self.num} - Cartas de Rota: [{', '.join([f'{c.cidadeOrigem}-{c.cidadeDestino}' for c in self.mao.cartasRota])}]")
