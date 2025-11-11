from typing import List
from carta import CartaRota, CartaTrem
from enums import CorTrem

class Jogador:
    def __init__(self, num: int):
        self.num = num
        self.cartasRota: List[CartaRota] = []
        self.cartasTrem: List[CartaTrem] = []
        self.pontos = 0

    def descartar_rota(self, pos: int) -> CartaRota:
        self.cartasRota.pop(pos)

    def comprar_carta(self):
        print("Comprando carta")

    def reivindicar_rota(self, rota_num: int):
        carta_rota = self.cartasRota[rota_num - 1]

        if rota_num < 1 or rota_num > len(self.cartasRota):
            print("Número de rota inválido.")
            return False

        if not self._reivindicacao_valida(carta_rota):
            print("Não possui cartas suficientes para reivindicar esta rota.")
            return False

        self.remover_cartas_usadas(carta_rota)
        self.descartar_rota(rota_num - 1)
        return True

    def add_carta_mao(self, carta):
        self.cartasTrem.append(carta)

    def mostrar_cartas(self):
        print("\nCartas de Trem na sua mão:")
        for i, c in enumerate(self.cartasTrem, 1):
            print(f"Trem {i}: {c.cor.value}")

        self.mostrar_cartas_rotas()

    def mostrar_cartas_rotas(self):
        print("\nCartas de Rota na sua mão:")
        for i, c in enumerate(self.cartasRota, 1):
            cores = [c2.value for c2 in c.requisitos]
            if len(cores) > 1:
                requisitos = ", ".join(cores[:-1]) + " e " + cores[-1]
            else:
                requisitos = cores[0]
            print(f"Rota {i}: {requisitos}")

    def set_cartas_trem(self, cartas):
        self.cartasTrem = cartas
        
    def set_cartas_rota(self, cartas):
        self.cartasRota = cartas

    def _reivindicacao_valida(self, carta_rota: CartaRota) -> bool:
        cartas_trem = {}
        for carta in self.cartasTrem:
            cartas_trem[carta.cor] = cartas_trem.get(carta.cor, 0) + 1

        requisitos = carta_rota.items()
        locomotivas = cartas_trem.get(CorTrem.LOCOMOTIVA, 0)

        for cor, qtd in requisitos.items():
            disponiveis = cartas_trem.get(cor, 0)
            if disponiveis < qtd:
                deficit = qtd - disponiveis
                if deficit > locomotivas:
                    return False
                locomotivas -= deficit
        return True


    def remover_cartas_usadas(self, carta_rota: CartaRota):
        requisitos = carta_rota.items()
        usadas = []

        cartas_restantes = self.cartasTrem.copy()

        for cor, qtd in requisitos.items():
            for carta in cartas_restantes[:]:
                if qtd == 0:
                    break
                if carta.cor == cor:
                    usadas.append(carta)
                    cartas_restantes.remove(carta)
                    qtd -= 1

            if qtd > 0:
                for carta in cartas_restantes[:]:
                    if qtd == 0:
                        break
                    if carta.cor == CorTrem.LOCOMOTIVA:
                        usadas.append(carta)
                        cartas_restantes.remove(carta)
                        qtd -= 1

        
        self.cartasTrem = cartas_restantes
        print(f"Cartas usadas: {[c.cor.value for c in usadas]}")
        return usadas
