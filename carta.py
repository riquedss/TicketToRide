from enums import CorTrem
from typing import List

class Carta:
    pass

class CartaTrem(Carta):
    def __init__(self, cor: CorTrem):
        self.cor = cor

    def locomotiva(self):
        return self.cor.value == "Locomotiva"

class CartaRota(Carta):
    def __init__(self, requisitos: List[CorTrem], valor: int):
        self.requisitos = requisitos
        self.valor = valor

    def items(self) -> dict:
        items = {}
        
        for requisito in self.requisitos:
            if requisito in items:
                items[requisito] += 1
            else:
                items[requisito] = 1

        return items
