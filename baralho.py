from typing import List
from carta import Carta
import random

class Baralho:
    def __init__(self, cartas: List[Carta], shuffle_limit: int = 100): 
        self.cartas: List[Carta] = cartas
        self.descarte: List[Carta] = []
        self.shuffle_limit: int = shuffle_limit 
        self.shuffle_count: int = 0        
        self.embaralhar()

    def pegar_carta_topo(self) -> Carta | None:
        if self.esta_vazio():
            
            if self.shuffle_count < self.shuffle_limit: 
                print("Baralho de compra vazio. Reembaralhando o descarte...")
                self._reembaralhar_do_descarte()
            else:
                print(f"Baralho vazio e limite de {self.shuffle_limit} reabastecimentos atingido.")
                return None

        if not self.esta_vazio():
            return self.cartas.pop()
    
        return None

    def _reembaralhar_do_descarte(self):
        # Reembaralha o descarte de volta para o baralho de compra
        if not self.descarte:
            return

        self.cartas = self.descarte
        self.descarte = []
        random.shuffle(self.cartas)
        self.shuffle_count += 1 

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