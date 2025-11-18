from enums import CorTrem, CidadeBonus 
from typing import List, Dict, Optional  
from abc import ABC, abstractmethod
from collections import Counter

class Carta(ABC):
    @abstractmethod
    def __repr__(self) -> str:
        pass

class CartaTrem(Carta):
    # Representa uma carta de Trem, que possui uma cor.
    def __init__(self, cor: CorTrem):
        self.cor = cor

    def __repr__(self) -> str:
        return f"CartaTrem(cor={self.cor.value})"

    def locomotiva(self) -> bool:
        # Verifica se a carta é uma locomotiva.
        return self.cor == CorTrem.LOCOMOTIVA

class CartaRota(Carta):
    # Representa uma carta de Rota, que possui requisitos e valor.
    def __init__(self, 
                 requisitos: List[CorTrem], 
                 valor: int, 
                 cidade_bonus: Optional[CidadeBonus] = None): # NOVO
        
        self.requisitos = requisitos
        self.valor = valor
        self.cidade_bonus = cidade_bonus # NOVO

    def __repr__(self) -> str:
        cores = [c.value for c in self.requisitos]
        repr_str = f"CartaRota(requisitos={cores}, valor={self.valor}"
        
        if self.cidade_bonus:
            repr_str += f", bonus={self.cidade_bonus.value}"
            
        repr_str += ")"
        return repr_str

    def contar_requisitos(self) -> Dict[CorTrem, int]:
        # Conta quantas cartas de cada cor são necessárias para esta rota.
        return Counter(self.requisitos)