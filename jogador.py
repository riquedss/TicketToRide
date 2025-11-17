from typing import List, Dict, Tuple
from carta import CartaRota, CartaTrem
from enums import CorTrem, CidadeBonus
from collections import Counter

class Jogador:
    def __init__(self, num: int):
        self.num = num
        self.cartasRota: List[CartaRota] = []
        self.cartasTrem: List[CartaTrem] = []
        self.rotas_completadas: List[CartaRota] = []
        self.pontos = 0

    def __repr__(self) -> str:
        return f"Jogador(num={self.num}, pontos={self.pontos})"

    def _contar_cartas_trem(self) -> Counter:
        return Counter(c.cor for c in self.cartasTrem)

    def reivindicar_rota(self, rota_num: int) -> List[CartaTrem] | None:
        # Verifica se a reinvindicação é válida
        if not (1 <= rota_num <= len(self.cartasRota)):
            print("Número de rota inválido.")
            return None

        carta_rota = self.cartasRota[rota_num - 1]

        if not self._reivindicacao_valida(carta_rota):
            print("Não possui cartas suficientes para reivindicar esta rota.")
            return None

        cartas_usadas, cartas_restantes = self._remover_cartas_usadas(carta_rota)
        
        self.cartasTrem = cartas_restantes
        
        self.rotas_completadas.append(self.cartasRota.pop(rota_num - 1))
        
        self.pontos += carta_rota.valor
        print(f"Rota reivindicada! Você ganhou {carta_rota.valor} pontos.")
        print(f"Cartas usadas: {[c.cor.value for c in cartas_usadas]}")
        
        return cartas_usadas

    def add_carta_mao(self, carta: CartaTrem | CartaRota):
        # Adiciona uma carta à mão do jogador
        if isinstance(carta, CartaTrem):
            self.cartasTrem.append(carta)
        elif isinstance(carta, CartaRota):
            self.cartasRota.append(carta)
        else:
            print(f"Tipo de carta desconhecido: {type(carta)}")

    def mostrar_cartas(self):
        # Exibe todas as cartas na mão do jogador
        print(f"\n--- MÃO DO JOGADOR {self.num} (Pontos: {self.pontos}) ---")
        
        print("\nCartas de Trem (Contagem):")
        contagem_trem = self._contar_cartas_trem()
        if not contagem_trem:
            print("(Vazio)")
        itens_formatados = []
        for cor, qtd in sorted(contagem_trem.items(), key=lambda item: item[0].value):
            itens_formatados.append(f"{cor.value}: {qtd}")
        print(" | ".join(itens_formatados))


        self.mostrar_cartas_rotas() # Mostra rotas na mão

        print("\nRotas Completadas:")
        if not self.rotas_completadas:
            print("(Nenhuma)")
        for i, c in enumerate(self.rotas_completadas, 1):
            cores = " e ".join([c2.value for c2 in c.requisitos])
            bonus = f" (BÔNUS: {c.cidade_bonus.value})" if c.cidade_bonus else ""   
            print(f"  [{i}] - {c.valor} pts | {cores}{bonus}")


    def mostrar_cartas_rotas(self):
        # Exibe as cartas de rota na mão do jogador
        print("\nCartas de Rota (na Mão):")
        if not self.cartasRota:
            print("(Vazio)")
        for i, c in enumerate(self.cartasRota, 1):
            cores = " e ".join([c2.value for c2 in c.requisitos])
            bonus = f" (BÔNUS: {c.cidade_bonus.value})" if c.cidade_bonus else ""
            print(f"  [{i}] - {c.valor} pts | {cores}{bonus}")

    def set_cartas_trem(self, cartas: List[CartaTrem]):
        self.cartasTrem = cartas
        
    def set_cartas_rota(self, cartas: List[CartaRota]):
        self.cartasRota = cartas

    def _reivindicacao_valida(self, carta_rota: CartaRota) -> bool:
        contagem_mao = self._contar_cartas_trem()
        requisitos = carta_rota.contar_requisitos()
        
        locomotivas_disponiveis = contagem_mao.get(CorTrem.LOCOMOTIVA, 0)

        for cor, qtd_necessaria in requisitos.items():
            qtd_na_mao = contagem_mao.get(cor, 0)
            
            if qtd_na_mao >= qtd_necessaria:
                continue
            
            deficit = qtd_necessaria - qtd_na_mao
            if locomotivas_disponiveis >= deficit:
                locomotivas_disponiveis -= deficit
            else:
                return False
                
        return True


    def _remover_cartas_usadas(self, carta_rota: CartaRota) -> Tuple[List[CartaTrem], List[CartaTrem]]:
        requisitos = carta_rota.contar_requisitos()
        cartas_usadas = []
        cartas_restantes = []
        
        locomotivas_na_mao = []
        cartas_coloridas = []
        for carta in self.cartasTrem:
            if carta.locomotiva():
                locomotivas_na_mao.append(carta)
            else:
                cartas_coloridas.append(carta)

        for cor_req, qtd_req in requisitos.items():
            qtd_paga = 0
            
            for carta in cartas_coloridas[:]: 
                if carta.cor == cor_req:
                    cartas_usadas.append(carta)
                    cartas_coloridas.remove(carta) 
                    qtd_paga += 1
                    if qtd_paga == qtd_req:
                        break
            
            if qtd_paga < qtd_req:
                deficit = qtd_req - qtd_paga
                
                for _ in range( deficit ):
                    if locomotivas_na_mao:
                        carta_locomotiva = locomotivas_na_mao.pop()
                        cartas_usadas.append(carta_locomotiva)
                    else:
                        raise Exception("Lógica de remoção falhou: Faltaram locomotivas.")

        cartas_restantes.extend(cartas_coloridas)
        cartas_restantes.extend(locomotivas_na_mao)
        
        return (cartas_usadas, cartas_restantes)