from typing import List
from carta import Carta

class Baralho:
    def __init__(self, cartas: List[Carta]):
        self.cartas: List[Carta] = cartas
        self.descarte: List[Carta] = []

    def pegar_carta_topo(self) -> Carta:
        if self.cartas:
            return self.cartas.pop()
        return None

    def embaralhar(self):
        import random
        random.shuffle(self.cartas)

    def esta_vazio(self) -> bool:
        return len(self.cartas) == 0

    def tamanho(self) -> int:
        return len(self.cartas)
    