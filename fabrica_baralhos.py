from carta import CartaTrem, CartaRota
from enums import CorTrem, CidadeBonus
from baralho import Baralho
from typing import List

def _criar_lista_cartas_trem() -> List[CartaTrem]:
    # Cria a lista de todas as 96 cartas de trem
    cartas_trem = []
    
    cores = [
        CorTrem.PRETO, CorTrem.BRANCO, CorTrem.VERMELHO, CorTrem.AZUL,
        CorTrem.VERDE, CorTrem.AMARELO, CorTrem.ROXO, CorTrem.LARANJA
    ]
    for cor in cores:
        for _ in range(10):
            cartas_trem.append(CartaTrem(cor))

    for _ in range(16):
        cartas_trem.append(CartaTrem(CorTrem.LOCOMOTIVA))
        
    return cartas_trem

def _criar_lista_cartas_rota() -> List[CartaRota]:

    
    # Cria as 46 cartas de rota com cidades bônus atribuídas
    cidades_bonus_lista = [
        CidadeBonus.CHICAGO,
        CidadeBonus.DALLAS,
        CidadeBonus.LOS_ANGELES,
        CidadeBonus.MIAMI,
        CidadeBonus.NEW_YORK,
        CidadeBonus.SEATTLE
    ]
    
    # Define os dados brutos das 46 cartas (requisitos, valor)
    dados_rotas = [
        # 35 cartas com 2 cores
        ([CorTrem.VERMELHO, CorTrem.LARANJA], 5),
        ([CorTrem.AMARELO, CorTrem.AZUL], 5),
        ([CorTrem.ROXO, CorTrem.VERDE], 6),
        ([CorTrem.BRANCO, CorTrem.PRETO], 6),
        ([CorTrem.VERMELHO, CorTrem.AZUL], 6),
        ([CorTrem.LARANJA, CorTrem.VERDE], 6),
        ([CorTrem.ROXO, CorTrem.AMARELO], 6),
        ([CorTrem.BRANCO, CorTrem.AZUL], 6),
        ([CorTrem.PRETO, CorTrem.VERDE], 5),
        ([CorTrem.VERMELHO, CorTrem.BRANCO], 5),
        ([CorTrem.LARANJA, CorTrem.AZUL], 6),
        ([CorTrem.ROXO, CorTrem.PRETO], 6),
        ([CorTrem.LARANJA, CorTrem.BRANCO], 5),
        ([CorTrem.VERMELHO, CorTrem.PRETO], 5),
        ([CorTrem.AZUL, CorTrem.VERDE], 6),
        ([CorTrem.ROXO, CorTrem.LARANJA], 6),
        ([CorTrem.AMARELO, CorTrem.VERMELHO], 5),
        ([CorTrem.VERDE, CorTrem.BRANCO], 5),
        ([CorTrem.AZUL, CorTrem.PRETO], 6),
        ([CorTrem.AMARELO, CorTrem.ROXO], 6),
        ([CorTrem.LARANJA, CorTrem.VERMELHO], 5),
        ([CorTrem.PRETO, CorTrem.BRANCO], 5),
        ([CorTrem.ROXO, CorTrem.AZUL], 6),
        ([CorTrem.AMARELO, CorTrem.VERDE], 6),
        ([CorTrem.AZUL, CorTrem.VERMELHO], 5),
        ([CorTrem.VERDE, CorTrem.LARANJA], 5),
        ([CorTrem.BRANCO, CorTrem.ROXO], 6),
        ([CorTrem.PRETO, CorTrem.AMARELO], 6),
        ([CorTrem.VERMELHO, CorTrem.VERDE], 5),
        ([CorTrem.BRANCO, CorTrem.LARANJA], 5),
        ([CorTrem.AZUL, CorTrem.AMARELO], 6),
        ([CorTrem.PRETO, CorTrem.ROXO], 6),
        ([CorTrem.AMARELO, CorTrem.BRANCO], 5),
        ([CorTrem.VERDE, CorTrem.AZUL], 5),
        ([CorTrem.LARANJA, CorTrem.PRETO], 6),
        # 11 cartas com 3 cores
        ([CorTrem.ROXO, CorTrem.VERMELHO, CorTrem.AZUL], 10),
        ([CorTrem.LARANJA, CorTrem.VERDE, CorTrem.BRANCO], 11),
        ([CorTrem.AMARELO, CorTrem.PRETO, CorTrem.ROXO], 11),
        ([CorTrem.AZUL, CorTrem.BRANCO, CorTrem.VERMELHO], 10),
        ([CorTrem.VERDE, CorTrem.ROXO, CorTrem.LARANJA], 11),
        ([CorTrem.PRETO, CorTrem.AMARELO, CorTrem.BRANCO], 10),
        ([CorTrem.VERMELHO, CorTrem.AZUL, CorTrem.ROXO], 11),
        ([CorTrem.LARANJA, CorTrem.VERDE, CorTrem.PRETO], 10),
        ([CorTrem.AMARELO, CorTrem.BRANCO, CorTrem.VERMELHO], 11),
        ([CorTrem.AZUL, CorTrem.PRETO, CorTrem.VERDE], 10),
        ([CorTrem.ROXO, CorTrem.LARANJA, CorTrem.AMARELO], 11),
    ]

    cartas_rota_finais = []
    
    # Atribui uma cidade bônus a cada carta
    for i, (requisitos, valor) in enumerate(dados_rotas):
        cidade = cidades_bonus_lista[i % len(cidades_bonus_lista)]
        nova_carta = CartaRota(requisitos, valor, cidade_bonus=cidade)
        cartas_rota_finais.append(nova_carta)

    return cartas_rota_finais

def criar_baralho_trem(shuffle_limit: int) -> Baralho:
    cartas = _criar_lista_cartas_trem()
    return Baralho(cartas, shuffle_limit=shuffle_limit) 

def criar_baralho_rota() -> Baralho:
    cartas = _criar_lista_cartas_rota()
    return Baralho(cartas)