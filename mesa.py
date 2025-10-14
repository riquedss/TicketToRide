from typing import List
from carta import CartaTrem, CartaRota
from baralho import Baralho
from carta import CartaTrem, CartaRota  
from enums import CorTrem

class Mesa:
    def __init__(self):   
        cartasTrem = self.cartasTremDoJogo()
        cartasRota = self.cartasRotaDoJogo()
        baralhoTrem = Baralho(cartasTrem)
        baralhoRota = Baralho(cartasRota) 

        self.baralhoTrem: Baralho = baralhoTrem
        self.baralhoRota: Baralho = baralhoRota
        self.ofertaTrem: List[CartaTrem] = []
        self.ofertaRota: List[CartaRota] = []

    def cartasTremDoJogo(self):
         #Inicializa o baralho de trem
        cartas_trem = []
        for cor in CorTrem:
            for _ in range(10):
                # Crie uma nova carta de trem com a cor atual
                nova_carta = CartaTrem(cor)
                cartas_trem.append(nova_carta)

        # Adicione mais 6 cartas de locomotiva
        for _ in range(6):
            nova_carta = CartaTrem(CorTrem.LOCOMOTIVA)
            cartas_trem.append(nova_carta)
        return cartas_trem

    def cartasRotaDoJogo(self):
        #Inicializa o baralho de rota
        cartas_rota = []
        cartas_rota = [
        # 35 cartas com 2 cores
        CartaRota([CorTrem.VERMELHO, CorTrem.LARANJA], 5),
        CartaRota([CorTrem.AMARELO, CorTrem.AZUL], 5),
        CartaRota([CorTrem.ROXO, CorTrem.VERDE], 6),
        CartaRota([CorTrem.BRANCO, CorTrem.PRETO], 6),
        CartaRota([CorTrem.VERMELHO, CorTrem.AZUL], 6),
        CartaRota([CorTrem.LARANJA, CorTrem.VERDE], 6),
        CartaRota([CorTrem.ROXO, CorTrem.AMARELO], 6),
        CartaRota([CorTrem.BRANCO, CorTrem.AZUL], 6),
        CartaRota([CorTrem.PRETO, CorTrem.VERDE], 5),
        CartaRota([CorTrem.VERMELHO, CorTrem.BRANCO], 5),
        CartaRota([CorTrem.LARANJA, CorTrem.AZUL], 6),
        CartaRota([CorTrem.ROXO, CorTrem.PRETO], 6),
        CartaRota([CorTrem.LARANJA, CorTrem.BRANCO], 5),
        CartaRota([CorTrem.VERMELHO, CorTrem.PRETO], 5),
        CartaRota([CorTrem.AZUL, CorTrem.VERDE], 6),
        CartaRota([CorTrem.ROXO, CorTrem.LARANJA], 6),
        CartaRota([CorTrem.AMARELO, CorTrem.VERMELHO], 5),
        CartaRota([CorTrem.VERDE, CorTrem.BRANCO], 5),
        CartaRota([CorTrem.AZUL, CorTrem.PRETO], 6),
        CartaRota([CorTrem.AMARELO, CorTrem.ROXO], 6),
        CartaRota([CorTrem.LARANJA, CorTrem.VERMELHO], 5),
        CartaRota([CorTrem.PRETO, CorTrem.BRANCO], 5),
        CartaRota([CorTrem.ROXO, CorTrem.AZUL], 6),
        CartaRota([CorTrem.AMARELO, CorTrem.VERDE], 6),
        CartaRota([CorTrem.AZUL, CorTrem.VERMELHO], 5),
        CartaRota([CorTrem.VERDE, CorTrem.LARANJA], 5),
        CartaRota([CorTrem.BRANCO, CorTrem.ROXO], 6),
        CartaRota([CorTrem.PRETO, CorTrem.AMARELO], 6),
        CartaRota([CorTrem.VERMELHO, CorTrem.VERDE], 5),
        CartaRota([CorTrem.BRANCO, CorTrem.LARANJA], 5),
        CartaRota([CorTrem.AZUL, CorTrem.AMARELO], 6),
        CartaRota([CorTrem.PRETO, CorTrem.ROXO], 6),
        CartaRota([CorTrem.AMARELO, CorTrem.BRANCO], 5),
        CartaRota([CorTrem.VERDE, CorTrem.AZUL], 5),
        CartaRota([CorTrem.LARANJA, CorTrem.PRETO], 6),

        # 11 cartas com 3 cores
        CartaRota([CorTrem.ROXO, CorTrem.VERMELHO, CorTrem.AZUL], 10),
        CartaRota([CorTrem.LARANJA, CorTrem.VERDE, CorTrem.BRANCO], 11),
        CartaRota([CorTrem.AMARELO, CorTrem.PRETO, CorTrem.ROXO], 11),
        CartaRota([CorTrem.AZUL, CorTrem.BRANCO, CorTrem.VERMELHO], 10),
        CartaRota([CorTrem.VERDE, CorTrem.ROXO, CorTrem.LARANJA], 11),
        CartaRota([CorTrem.PRETO, CorTrem.AMARELO, CorTrem.BRANCO], 10),
        CartaRota([CorTrem.VERMELHO, CorTrem.AZUL, CorTrem.ROXO], 11),
        CartaRota([CorTrem.LARANJA, CorTrem.VERDE, CorTrem.PRETO], 10),
        CartaRota([CorTrem.AMARELO, CorTrem.BRANCO, CorTrem.VERMELHO], 11),
        CartaRota([CorTrem.AZUL, CorTrem.PRETO, CorTrem.VERDE], 10),
        CartaRota([CorTrem.ROXO, CorTrem.LARANJA, CorTrem.AMARELO], 11),
        ]
        return cartas_rota
    
    def get_baralhoTrem(self):
        return self.baralhoTrem
    
    def get_baralhoRota(self):
        return self.baralhoRota
    
    def get_ofertaTrem(self):
        return self.ofertaTrem
    
    def get_ofertaRota(self):
        return self.ofertaRota
    
    def set_ofertaTrem(self):
        self.ofertaTrem = [self.get_baralhoTrem().pegar_carta_topo() for _ in range(5)]

    def set_ofertaRota(self):
        self.ofertaRota = [self.get_baralhoRota().pegar_carta_topo() for _ in range(3)]
    
    def pegar_oferta_trem(self, posicao, qtd):
        if(self.ofertaTrem[posicao].locomotiva() and qtd > 0):
            print("\nNão pode comprar locomotiva")
            return None
        carta = self.ofertaTrem.pop(posicao)
        self.ofertaTrem.append(self.baralhoTrem.pegar_carta_topo())
        return carta

    def mostrar_mesa(self):

        print("\nCartas de Trem na mesa:")
        for i, c in enumerate(self.ofertaTrem, 1):
            print(f"Trem {i}: {c.cor.value}")

        #print("Cartas de Trem na mesa:".join(c.cor.value for c in self.ofertaTrem))

        print("\nCartas de Rota na mesa:")
        for i, c in enumerate(self.ofertaRota, 1):
            cores = [c2.value for c2 in c.requisitos]
            if len(cores) > 1:
                requisitos = ", ".join(cores[:-1]) + " e " + cores[-1]
            else:
                requisitos = cores[0]
            print(f"Rota {i}: {requisitos}")

        #print("Cartas de Rota na mesa:".join(f"{c2.value}" for c in self.ofertaRota for c2 in c.requisitos))
