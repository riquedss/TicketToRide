from enums import CorTrem
from typing import List

class Carta:
    pass

class CartaTrem(Carta):
    def __init__(self, cor: CorTrem):
        self.cor = cor

class CartaRota(Carta):
    def __init__(self, requisitos: List[CorTrem], valor: int):
        self.requisitos = requisitos
        self.valor = valor