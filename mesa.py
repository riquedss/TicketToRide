from typing import List
from carta import CartaTrem, CartaRota
from baralho import Baralho
from enums import CorTrem, CidadeBonus 
import fabrica_baralhos

class Mesa:
    def __init__(self):   
        self.baralhoTrem: Baralho = fabrica_baralhos.criar_baralho_trem()
        self.baralhoRota: Baralho = fabrica_baralhos.criar_baralho_rota()
        self.ofertaTrem: List[CartaTrem] = []
        self.ofertaRota: List[CartaRota] = []

    def get_baralhoTrem(self) -> Baralho:
        return self.baralhoTrem
    
    def get_baralhoRota(self) -> Baralho:
        return self.baralhoRota
    
    def get_ofertaTrem(self) -> List[CartaTrem]:
        return self.ofertaTrem
    
    def get_ofertaRota(self) -> List[CartaRota]:
        return self.ofertaRota
    
    def set_ofertaTrem(self):
        self.ofertaTrem = [self.get_baralhoTrem().pegar_carta_topo() for _ in range(5)]
        # Remove Nones se o baralho for menor que 5
        self.ofertaTrem = [carta for carta in self.ofertaTrem if carta]
        # Garante a regra das locomotivas na inicialização
        self._verificar_e_repor_oferta_trem()

    def set_ofertaRota(self):
        self.ofertaRota = [self.get_baralhoRota().pegar_carta_topo() for _ in range(3)]
        # Remove Nones se o baralho for menor que 3
        self.ofertaRota = [carta for carta in self.ofertaRota if carta]
    
    def _verificar_e_repor_oferta_trem(self):
        # Verifica se há 3 ou mais locomotivas na oferta de trem
        cartas_validas = [c for c in self.ofertaTrem if c]
        
        while sum(1 for c in cartas_validas if c.locomotiva()) >= 3:
            print("\n(!) 3 ou mais locomotivas na mesa! Descartando e repondo...")
            
            for carta in self.ofertaTrem:
                self.baralhoTrem.descartar(carta)
                
            self.ofertaTrem = [self.baralhoTrem.pegar_carta_topo() for _ in range(5)]
            cartas_validas = [c for c in self.ofertaTrem if c]
            
            if len(cartas_validas) < 3:
                break


    def pegar_oferta_trem(self, posicao: int) -> CartaTrem | None:
        # Pega uma carta da oferta de trem na posição e a repõe.
        if not (0 <= posicao < len(self.ofertaTrem)):
            print("\nPosição inválida na oferta.")
            return None
            
        carta_comprada = self.ofertaTrem.pop(posicao)
        
        carta_nova = self.baralhoTrem.pegar_carta_topo()
        if carta_nova:
            self.ofertaTrem.insert(posicao, carta_nova)
        
        self._verificar_e_repor_oferta_trem()
        
        return carta_comprada

    def pegar_oferta_rota(self, posicao: int) -> CartaRota | None:
        # Pega uma carta da oferta de rota na posição e a repõe.
        if not (0 <= posicao < len(self.ofertaRota)):
            print("\nPosição inválida na oferta.")
            return None
        
        carta_comprada = self.ofertaRota.pop(posicao)
        
        carta_nova = self.baralhoRota.pegar_carta_topo()
        if carta_nova:
            self.ofertaRota.insert(posicao, carta_nova)
            
        return carta_comprada


    def mostrar_mesa(self):
        print("\n" + "="*30)
        print(" " * 9 + "MESA DO JOGO" + " " * 9)
        print("="*30)
        print("\n--- OFERTA DE TREM (MESA) ---")
        if not self.ofertaTrem:
            print("  (Vazio)")
        for i, c in enumerate(self.ofertaTrem, 1):
            print(f"  [{i}] - {c.cor.value:<10}")
        print("\n--- OFERTA DE ROTA (MESA) ---")
        if not self.ofertaRota:
            print("  (Vazio)")
        for i, c in enumerate(self.ofertaRota, 1):
            cores = " e ".join([c2.value for c2 in c.requisitos])
            bonus = f" (BÔNUS: {c.cidade_bonus.value})" if c.cidade_bonus else ""
            print(f"  [{i}] - {c.valor:<2} pts | {cores}{bonus}")
        print("="*30)