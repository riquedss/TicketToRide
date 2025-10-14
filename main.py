from partida import Partida
import os


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
    input(f"\nJogador {partida.get_jogador_atual()}, pressione enter para iniciar seu turno.")
    partida.get_mesa().mostrar_mesa()
    print("\nSua mão:")
    jogador.mostrar_cartas()
    while True:
        match partida.exibir_acoes():
            case 1:
                limpar_terminal()

                print(f"Jogador {partida.get_jogador_atual()}, você deve escolher duas cartas não locomotiva ou 1 locomotiva da mesa.")
                while partida.qtd_cartas_selecionadas_turno() < 2:
                    partida.get_mesa().mostrar_mesa()
                    carta = None

                    escolha_carta = input(f"\nJogador {partida.get_jogador_atual()}, digite (1) para escolher uma carta do topo do baralho e (2) para pegar as ofertadas na mesa.")
                    if escolha_carta == "1":
                        carta = partida.get_mesa().get_baralhoTrem().pegar_carta_topo()
                    elif escolha_carta == "2":
                        index_carta_mesa = int(input("Escolha qual carta da mesa você quer pegar de 1 - 5\n"))
                        carta = partida.get_mesa().pegar_oferta_trem(index_carta_mesa - 1)

                        if not partida.eh_escolha_valida_no_turno(carta):
                            print("Escolha inválida neste turno! Tente outra carta.")
                            continue
                    else:
                        print("Opção inválida")

                    partida.registrar_carta_escolhida(carta)
                
                
                partida.passar_turno()
                break

            case 2:
                partida.get_mesa().mostrar_mesa()
            case 3:
                jogador.mostrar_cartas()
            case 4:
                partida.passar_turno()
                break
    
    
    
    