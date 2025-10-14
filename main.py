from partida import Partida
import os
import time

def limpar_terminal():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


partida = Partida()
partida.iniciar()
input("\nPressione Enter para continuar...")

while True:
    limpar_terminal()
    jogador = partida.get_jogadores()[partida.get_jogador_atual() - 1]
    input(f"\nJogador {partida.get_jogador_atual()}, pressione enter para iniciar sua jogada.")
    partida.get_mesa().mostrar_mesa()
    while True:
        match partida.exibir_acoes():
            case 1:
                jogador.comprar_carta()
            case 2:
                partida.passar_turno()
                break
    
    
    
    