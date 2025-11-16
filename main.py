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
    if(partida.get_mesa().get_baralhoTrem().esta_vazio()):
        print("O baralho de Trem acabou. Esta será sua ultima jogada!")
    jogador = partida.get_jogadores()[partida.get_jogador_atual() - 1]
    input(f"\nJogador {partida.get_jogador_atual()}, pressione enter para iniciar seu turno.")
    partida.get_mesa().mostrar_mesa()
    jogador.mostrar_cartas()
    comprado = False
    while True:
        try: 
            match partida.exibir_acoes():
                case 1:
                    limpar_terminal()
                    if(not comprado):
                        print(f"Jogador {partida.get_jogador_atual()}, você pode escolher duas cartas não locomotiva ou 1 locomotiva da mesa.")
                        pegou_carta_locomotiva_mesa = False
                        while partida.qtd_cartas_selecionadas_turno() < 2 and not pegou_carta_locomotiva_mesa:
                            partida.get_mesa().mostrar_mesa()
                            carta = None

                            escolha_carta = input(f"\nJogador {partida.get_jogador_atual()}, digite (1) para escolher uma carta do topo do baralho e (2) para pegar as ofertadas na mesa.\n")
                            limpar_terminal()
                        
                            if escolha_carta == "1":
                                carta = partida.get_mesa().get_baralhoTrem().pegar_carta_topo()

                                if not carta:
                                    print("Baralho vazio! Escolha outra opção.")

                            elif escolha_carta == "2":
                                index_carta_mesa = int(input(f"Escolha qual carta da mesa você quer pegar de 1 - {len(partida.get_mesa().get_ofertaTrem())}\n"))
                                carta = partida.get_mesa().pegar_oferta_trem(index_carta_mesa - 1, partida.qtd_cartas_selecionadas_turno())

                                if carta and carta.locomotiva():
                                    pegou_carta_locomotiva_mesa = True
                            else:
                                print("Opção inválida.")

                            if carta != None:
                                partida.registrar_carta_escolhida(carta)
                                print(f"Comprou uma carta Trem {carta.cor.value}")
                        
                            input("Pressione enter para continuar.")
                        if carta != None:    
                            partida.add_cartas_mao_jogador(jogador)
                        
                        comprado = True
                    else:
                        print("\nVocê já executou compra neste turno.")
                    input("Pressione enter para finalizar compra.")
                    limpar_terminal()

                case 2:
                    limpar_terminal()
                    if(not comprado):
                        print(f"Escolha duas entre as quatro cartas rota.")
                        mesa = partida.get_mesa()
                        baralho_rota = mesa.get_baralhoRota()
                        cartas_mostradas = []

                        for _ in range(4):
                            carta = baralho_rota.pegar_carta_topo()
                            if carta:
                                cartas_mostradas.append(carta)

                        if not cartas_mostradas:
                            print("Baralho de rotas vazio!")
                        else:
                            print("\nCartas de Rota disponíveis:")
                            for i, c in enumerate(cartas_mostradas, 1):
                                cores = [c2.value for c2 in c.requisitos]
                                if len(cores) > 1:
                                    requisitos = ", ".join(cores[:-1]) + " e " + cores[-1]
                                else:
                                    requisitos = cores[0]
                                print(f"{i}: {requisitos} (Valor: {c.valor})")

                            escolhidas = set()

                            alvo = 2 if len(cartas_mostradas) >= 2 else len(cartas_mostradas)
                            while len(escolhidas) < alvo:
                                try:
                                    escolha = int(input(f"\nEscolha a carta rota #{len(escolhidas)+1} (1-{len(cartas_mostradas)}): "))
                                except ValueError:
                                    print("Entrada inválida.")
                                    continue
                                if escolha < 1 or escolha > len(cartas_mostradas):
                                    print("Opção inválida.")
                                    continue
                                if escolha in escolhidas:
                                    print("Você já escolheu essa carta.")
                                    continue
                                escolhidas.add(escolha)

                            for idx in sorted(escolhidas):
                                carta = cartas_mostradas[idx-1]
                                jogador.cartasRota.append(carta)
                                print(f"Adicionada à sua mão: rota de {carta.valor} pontos")

                            for i, c in enumerate(cartas_mostradas, 1):
                                if i not in escolhidas:
                                    baralho_rota.cartas.insert(0, c)

                        comprado = True
                    else:
                        print("\nVocê já executou compra neste turno.")
                    input("Pressione enter para finalizar compra.")
                    limpar_terminal()
                
                case 3:
                    limpar_terminal()
                    partida.get_mesa().mostrar_mesa()
                case 4:
                    limpar_terminal()
                    jogador.mostrar_cartas()
                case 5:
                    partida.passar_turno()
                    break
                case 6:
                    limpar_terminal()
                    jogador.mostrar_cartas_rotas()
                    try:
                        rota_num = int(input("\nQual rota você deseja reivindicar? (Digite o número da rota)\n"))
                        if jogador.reivindicar_rota(rota_num):
                            print(f"Rota {rota_num} reivindicada com sucesso!")
                        else:
                            print(f"Não foi possível reivindicar a rota {rota_num}.")
                    except ValueError:
                        print("ID de rota inválido.")

                case _:
                    print("Opção inválida")
                    break
        except Exception as e:
            print(f"Ocorreu um erro. Entre com uma ação válida. Detalhes do erro: {e}")
