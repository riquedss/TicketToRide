from typing import List
from carta import Carta
import random  # Movido para o topo do arquivo

class Baralho:
    # Responsável por gerenciar a pilha de compra e descarte de cartas.
    def __init__(self, cartas: List[Carta]):
        self.cartas: List[Carta] = cartas  # Pilha de compra
        self.descarte: List[Carta] = []    # Pilha de descarte
        self.embaralhar()

    def pegar_carta_topo(self) -> Carta | None:
        # Pega a carta do topo da pilha de compra.
        if self.esta_vazio():
            print("Baralho de compra vazio. Reembaralhando o descarte...")
            self._reembaralhar_do_descarte()

        if not self.esta_vazio():
            return self.cartas.pop()
        
        print("Baralho e descarte estão vazios.")
        return None

    def _reembaralhar_do_descarte(self):
        # Reembaralha as cartas da pilha de descarte para a pilha de compra.
        if not self.descarte:
            return

        self.cartas = self.descarte
        self.descarte = []
        random.shuffle(self.cartas)

    def descartar(self, carta: Carta):
        if carta:
            self.descarte.append(carta)

    def colocar_no_fundo(self, carta: Carta):
        if carta:
            self.cartas.insert(0, carta)

    def embaralhar(self):
        random.shuffle(self.cartas)

    def esta_vazio(self) -> bool:
        return len(self.cartas) == 0

    def tamanho(self) -> int:
        return len(self.cartas)