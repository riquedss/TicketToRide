from partida import Partida
import os

def limpar_terminal():
    """Limpa o console do terminal."""
    if os.name == 'nt': # Windows
        _ = os.system('cls')
    else: # Mac/Linux
        _ = os.system('clear')

# --- Início do Jogo ---
partida = Partida()
partida.iniciar()
input("\nPressione Enter para continuar...")

# --- Loop Principal do Jogo ---
while True:
    limpar_terminal()
    
    jogador = partida.get_jogador_atual()
    
    print("--- ESTAÇÃO TERMINAL ---")
    print(f"Turno {partida.turno_atual} - Jogador {jogador.num} (Pontos: {jogador.pontos})")
    
    # Notificação de última rodada
    if partida.turno_final != -1:
        turnos_restantes = (partida.turno_final - partida.turno_atual) + 1
        print(f"(!) BARALHO VAZIO. Esta é a última rodada. Faltam {turnos_restantes} turnos.")

    
    # --- FASE 1: AÇÃO PRINCIPAL (Comprar Trem ou Rota) ---
    acao_principal_realizada = False
    acao_compra_trem = False
    
    while not acao_principal_realizada:
        try:
            acao = partida.exibir_acoes_principais()
            
            match acao:
                case 1: # 1. Comprar Cartas de Trem
                    acao_principal_realizada = True
                    acao_compra_trem = True # Sinaliza para ir para a Fase 2

                case 2: # 2. Comprar Cartas Rota do Baralho (Encerra o Turno)
                    limpar_terminal()
                    if partida.comprar_cartas_rota():
                        acao_principal_realizada = True
                        acao_compra_trem = False # Pula a fase de reivindicação
                    
                case 3: # 3. Exibir cartas da Mesa
                    limpar_terminal()
                    partida.get_mesa().mostrar_mesa()
                    input("\nPressione Enter para continuar...")

                case 4: # 4. Exibir minhas cartas
                    limpar_terminal()
                    jogador.mostrar_cartas()
                    input("\nPressione Enter para continuar...")
                
                case _:
                    print("Opção inválida, tente novamente.")

        except Exception as e:
            print(f"\nOcorreu um erro inesperado: {e}")
        
        # Limpa o terminal para a próxima fase
        limpar_terminal()

    # --- FASE 1.1: SUB-LOOP DE COMPRA DE TREM ---
    if acao_compra_trem:
        print(f"--- Jogador {jogador.num}: Fase de Compra de Trem ---")
        
        while partida.cartas_trem_compradas_no_turno < 2:
            try:
                partida.get_mesa().mostrar_mesa() # Mostra a mesa a cada compra
                acao_compra = partida.exibir_acoes_compra_trem()
                
                match acao_compra:
                    case 1: # Comprar do Baralho
                        partida.comprar_carta_trem_baralho()
                    
                    case 2: # Comprar da Oferta
                        try:
                            pos_str = input("\nQual carta da mesa você quer? (1-5 ou '0' para voltar): ")
                            if pos_str == '0':
                                continue # Volta ao menu de compra
                                
                            pos = int(pos_str)
                            partida.comprar_carta_trem_oferta(pos - 1)
                        except ValueError:
                            print("Entrada inválida.")
                    
                    case 3: # Exibir Mesa
                        limpar_terminal()
                        partida.get_mesa().mostrar_mesa()
                    
                    case 4: # Exibir Minhas Cartas
                        limpar_terminal()
                        jogador.mostrar_cartas()
                        
                    case _:
                        print("Opção inválida.")
                
                input("\nPressione Enter para continuar...")
                limpar_terminal()
            
            except Exception as e:
                print(f"\nOcorreu um erro inesperado: {e}")

    # --- FASE 2: SUB-LOOP DE REIVINDICAÇÃO  ---
    if acao_compra_trem:
        print(f"--- Jogador {jogador.num}: Fase de Reivindicação (Opcional) ---")
        
        while True: # Até o jogador passar o turno
            try:
                jogador.mostrar_cartas() # Mostra a mão para ajudar a decidir
                acao_reiv = partida.exibir_acoes_reivindicacao()
                
                match acao_reiv:
                    case 1: # 1. Reivindicar Rota da Mão
                        try:
                            rota_num_str = input("\nQual rota da mão você deseja reivindicar? (Digite o número ou '0' para voltar): ")
                            if rota_num_str == '0':
                                continue # Volta ao menu de reivindicação
                                
                            rota_num = int(rota_num_str)
                            partida.reivindicar_rota_jogador(rota_num)
                        except ValueError:
                            print("ID de rota inválido.")
                    
                    case 2: # 2. Reivindicar Rota da Oferta da Mesa
                        limpar_terminal()
                        partida.get_mesa().mostrar_mesa()
                        try:
                            pos_str = input("\nQual carta Rota da mesa você quer? (1-3 ou '0' para voltar): ")
                            if pos_str == '0':
                                continue # Volta ao menu de reivindicação

                            pos = int(pos_str)
                            partida.reivindicar_carta_rota_oferta(pos - 1)
                            
                        except ValueError:
                            print("Entrada inválida.")
                    
                    case 3: # 3. Exibir cartas da Mesa
                        limpar_terminal()
                        partida.get_mesa().mostrar_mesa()
                    
                    case 4: # 4. Exibir minhas cartas
                        limpar_terminal()
                        jogador.mostrar_cartas()
                    
                    case 5: # 5. FINALIZAR TURNO - Passar
                        print("Passando o turno...")
                        partida.passar_turno()
                        break # Quebra o loop de reivindicação
                    
                    case _:
                        print("Opção inválida.")
                
                input("\nPressione Enter para continuar...")
                limpar_terminal()

            except Exception as e:
                print(f"\nOcorreu um erro inesperado: {e}")
        
    else: # Se o jogador comprou rotas
        print("Ação de comprar rotas encerra o turno. Passando...")
        partida.passar_turno()
        input("\nPressione Enter para o próximo jogador...")