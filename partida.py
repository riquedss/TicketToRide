from typing import List, Dict
from jogador import Jogador
from mesa import Mesa
from carta import CartaTrem, CartaRota
from enums import CidadeBonus

class Partida:
    def __init__(self): 
        print("BEM VINDO AO ESTACAO TERMINAL")
        num_jogadores = 0
        while num_jogadores == 0:
            print("Entre com a quantidade de jogadores (2-4): ")
            try:
                num_jogadores = int(input().strip())
                if num_jogadores < 2 or num_jogadores > 4:
                    print("Número inválido de jogadores. Tente novamente.\n")
                    num_jogadores = 0
                    continue

                jogadores = [Jogador(i+1) for i in range(num_jogadores)]

            except ValueError:
                print("Entrada inválida. Tente novamente.\n")

        self.jogadores: List[Jogador] = jogadores
        self.mesa: Mesa = Mesa()
        self.turno_atual = 1
        self.turno_final = -1 
        self.idx_jogador_atual = 0 
        self.cartas_trem_compradas_no_turno = 0
        self.rota_da_mesa_reivindicada_neste_turno = False
    
    def get_mesa(self) -> Mesa:
        return self.mesa
    
    def get_jogadores(self) -> List[Jogador]:
        return self.jogadores

    def get_jogador_atual(self) -> Jogador:
        """Retorna o objeto Jogador do turno atual."""
        return self.jogadores[self.idx_jogador_atual]

    def iniciar(self):
        mesa = self.get_mesa()
        jogadores = self.get_jogadores()

        for j in jogadores:
            cartas_mao_trem = [mesa.get_baralhoTrem().pegar_carta_topo() for _ in range(6)]
            cartas_mao_rota = [mesa.get_baralhoRota().pegar_carta_topo() for _ in range(3)]
            
            j.set_cartas_trem([c for c in cartas_mao_trem if c]) 
            j.set_cartas_rota([c for c in cartas_mao_rota if c]) 

        mesa.set_ofertaTrem()
        mesa.set_ofertaRota()
        
        print("\n--- PARTIDA INICIADA ---")
        mesa.mostrar_mesa()

    # --- MENUS DE AÇÃO ---
    def exibir_acoes_principais(self) -> int:
        print("\nO que você deseja fazer?" \
        "\n1 - Comprar Cartas de Trem (Permite Reivindicar)" \
        "\n2 - Comprar Cartas Rota do Baralho (Encerra o Turno)" \
        "\n------------------" \
        "\n3 - Exibir cartas da Mesa" \
        "\n4 - Exibir minhas cartas")
        
        try:
            return int(input().strip())
        except ValueError:
            print("Entrada inválida.")
            return -1

    def exibir_acoes_compra_trem(self) -> int:
        print(f"\nCOMPRA DE TREM ({self.cartas_trem_compradas_no_turno}/2):" \
        "\n1 - Comprar carta de Trem do Baralho" \
        "\n2 - Comprar carta de Trem da Mesa (Oferta)" \
        "\n3 - Exibir cartas da Mesa" \
        "\n4 - Exibir minhas cartas")
        try:
            return int(input().strip())
        except ValueError:
            print("Entrada inválida.")
            return -1

    def exibir_acoes_reivindicacao(self) -> int:
        print("\nFASE DE REIVINDICAÇÃO (Opcional):" \
        "\n1 - Reivindicar Rota (da Mão)" \
        "\n2 - Reivindicar Rota (da Oferta da Mesa) (Max 1 por turno)" \
        "\n------------------" \
        "\n3 - Exibir cartas da Mesa" \
        "\n4 - Exibir minhas cartas" \
        "\n5 - FINALIZAR TURNO (Passar)")
        try:
            return int(input().strip())
        except ValueError:
            print("Entrada inválida.")
            return -1

    def passar_turno(self):
        if(self.get_mesa().get_baralhoTrem().esta_vazio()):
            if self.turno_final == -1:
                print("O baralho de Trem acabou. Iniciando rodada final!")
                self.turno_final = self.turno_atual + len(self.jogadores)
            
            if self.turno_atual >= self.turno_final:
                self._encerrar_jogo()
                return False 

        self.idx_jogador_atual = (self.idx_jogador_atual + 1) % len(self.jogadores)
        self.turno_atual += 1
        
        self.cartas_trem_compradas_no_turno = 0
        self.rota_da_mesa_reivindicada_neste_turno = False 
        
        print(f"\nTurno {self.turno_atual} - Jogador {self.get_jogador_atual().num}")
        return True

    def _encerrar_jogo(self):
        """Calcula e exibe as pontuações finais, incluindo pênaltis e bônus."""
        print("\n--- FIM DE JOGO ---")
        print("Calculando pontuações finais...")
        print("\nCalculando penalidades por rotas não completadas...")
        for j in self.jogadores:
            penalidade = 0
            for rota_na_mao in j.cartasRota:
                penalidade += rota_na_mao.valor
            
            if penalidade > 0:
                print(f"Jogador {j.num} perde {penalidade} pontos por {len(j.cartasRota)} rota(s) na mão.")
                j.pontos -= penalidade
            else:
                print(f"Jogador {j.num} não tem pênaltis.")

        # --- Lógica do Bônus de Mais Rotas ---
        print("\nCalculando bônus por mais rotas completadas...")
        
        max_rotas = -1
        jogadores_com_max_rotas = []

        for j in self.jogadores:
            num_rotas = len(j.rotas_completadas)
            print(f"Jogador {j.num} completou {num_rotas} rotas.")
            if num_rotas > max_rotas:
                max_rotas = num_rotas
        
        if max_rotas > 0:
            for j in self.jogadores:
                if len(j.rotas_compratadas) == max_rotas:jogadores_com_max_rotas.append(j)
        
        if jogadores_com_max_rotas:
            for j_bonus in jogadores_com_max_rotas:
                print(f"Jogador {j_bonus.num} ganha 15 pontos de bônus por {max_rotas} rotas!")
                j_bonus.pontos += 15
        else:
            print("Nenhum bônus de rotas aplicado (nenhuma rota completada).")

        # --- Lógica do Bônus "Big City" ---
        print("\nCalculando bônus de 'Big City'...")
        
        for cidade in CidadeBonus:
            print(f"\nAnalisando bônus para: {cidade.value}")
            contagem_cidade: Dict[Jogador, int] = {j: 0 for j in self.jogadores}
            max_cidade = 0
            
            for j in self.jogadores:
                for rota in j.rotas_completadas:
                    if rota.cidade_bonus == cidade:
                        contagem_cidade[j] += 1
                
                print(f"Jogador {j.num} completou {contagem_cidade[j]} rotas de {cidade.value}.")
                if contagem_cidade[j] > max_cidade:
                    max_cidade = contagem_cidade[j]

            if max_cidade > 0:
                for j in self.jogadores:
                    if contagem_cidade[j] == max_cidade:
                        print(f"Jogador {j.num} ganha 15 pontos de bônus por {cidade.value}!")
                        j.pontos += 15
            else:
                print(f"Nenhum bônus para {cidade.value} (ninguém completou).")
        
        # --- Fim dos Bônus ---

        print("\nPontuações finais (com pênaltis e bônus):")
        
        vencedor = None
        max_pontos = -999 # Iniciar com valor baixo para pegar pontos negativos
        
        for jogador in self.jogadores:
            print(f"Jogador {jogador.num}: {jogador.pontos} pontos")
            if jogador.pontos > max_pontos:
                max_pontos = jogador.pontos
                vencedor = jogador
        
        print(f"\nO vencedor é o Jogador {vencedor.num} com {max_pontos} pontos!")
        exit(0) 

    # --- Métodos de Ação do Controller ---

    def comprar_carta_trem_baralho(self) -> bool:
        if self.cartas_trem_compradas_no_turno >= 2:
            print("Você já comprou suas 2 cartas de trem.")
            return False

        carta = self.mesa.get_baralhoTrem().pegar_carta_topo()
        if not carta:
            print("O baralho de trem (e o descarte) estão vazios.")
            return False
        
        jogador_atual = self.get_jogador_atual()
        jogador_atual.add_carta_mao(carta)
        self.cartas_trem_compradas_no_turno += 1
        
        print(f"Você comprou uma carta: {carta.cor.value}")
        
        if self.cartas_trem_compradas_no_turno == 2:
            print("Você comprou 2 cartas. Fase de compra finalizada.")
            
        return True

    def comprar_carta_trem_oferta(self, posicao: int) -> bool:
        if self.cartas_trem_compradas_no_turno >= 2:
            print("Você já comprou suas 2 cartas de trem.")
            return False
            
        carta = self.mesa.pegar_oferta_trem(posicao)
        if not carta:
            return False 
            
        if carta.locomotiva():
            if self.cartas_trem_compradas_no_turno > 0:
                print("Você não pode pegar uma Locomotiva se já pegou outra carta.")
                self.mesa.ofertaTrem.insert(posicao, carta) 
                return False
            
            self.cartas_trem_compradas_no_turno = 2
            print("Você pegou uma Locomotiva. Fase de compra finalizada.")
        else:
            self.cartas_trem_compradas_no_turno += 1
            if self.cartas_trem_compradas_no_turno == 2:
                print("Você comprou 2 cartas. Fase de compra finalizada.")

        jogador_atual = self.get_jogador_atual()
        jogador_atual.add_carta_mao(carta)
        print(f"Você comprou da mesa: {carta.cor.value}")
        return True

    def reivindicar_carta_rota_oferta(self, posicao: int) -> bool:
        if self.rota_da_mesa_reivindicada_neste_turno:
            print("Você já reivindicou uma rota da mesa neste turno.")
            return False
        
        if not (0 <= posicao < len(self.mesa.get_ofertaRota())):
            print("Posição inválida na oferta de rota.")
            return False
        
        carta_rota = self.mesa.get_ofertaRota()[posicao]
        jogador_atual = self.get_jogador_atual()

        if not jogador_atual._reivindicacao_valida(carta_rota):
            print("Você não tem as cartas de trem necessárias para reivindicar esta rota.")
            return False
        
        print(f"Reivindicando Rota da Mesa: {carta_rota.valor} pts...")
        
        cartas_usadas, cartas_restantes = jogador_atual._remover_cartas_usadas(carta_rota)
        
        jogador_atual.cartasTrem = cartas_restantes 
        
        for carta in cartas_usadas:
            self.mesa.get_baralhoTrem().descartar(carta)
            
        self.mesa.pegar_oferta_rota(posicao) 
        
        jogador_atual.pontos += carta_rota.valor
        jogador_atual.rotas_completadas.append(carta_rota)
        
        self.rota_da_mesa_reivindicada_neste_turno = True
        
        print(f"Rota da mesa reivindicada! Você ganhou {carta_rota.valor} pontos.")
        print(f"Cartas usadas: {[c.cor.value for c in cartas_usadas]}")
        
        return True

    def comprar_cartas_rota(self) -> bool:
        print("Comprando cartas de rota... (Puxe 4, escolha pelo menos 1)")
        mesa = self.get_mesa()
        baralho_rota = mesa.get_baralhoRota()
        jogador_atual = self.get_jogador_atual()
        
        cartas_puxadas = [baralho_rota.pegar_carta_topo() for _ in range(4)]
        cartas_puxadas = [c for c in cartas_puxadas if c] 

        if not cartas_puxadas:
            print("Baralho de rotas vazio!")
            return False
            
        print("\nCartas de Rota disponíveis (escolha pelo menos 1):")
        for i, c in enumerate(cartas_puxadas, 1):
            cores = [c2.value for c2 in c.requisitos]
            requisitos = " e ".join(cores)
            bonus = f" (BÔNUS: {c.cidade_bonus.value})" if c.cidade_bonus else ""
            print(f"[{i}] - Rota de {c.valor} pts ({requisitos}){bonus}")

        escolhidas_idx = set()
        cartas_escolhidas = []
        
        cartas_para_devolver = list(cartas_puxadas)
        
        while True:
            try:
                if len(escolhidas_idx) >= 1:
                    print("(Digite '0' para parar de escolher)")
                
                prompt = f"\nEscolha a carta rota #{len(escolhidas_idx)+1} (1-{len(cartas_puxadas)}): "
                escolha_str = input(prompt)
                escolha = int(escolha_str)
                
                if escolha == 0:
                    if len(escolhidas_idx) >= 1:
                        break 
                    else:
                        print("Você deve escolher pelo menos 1 carta.")
                        continue
                
                idx = escolha - 1
                
                if not (0 <= idx < len(cartas_puxadas)):
                    print("Opção inválida.")
                elif idx in escolhidas_idx:
                    print("Você já escolheu essa carta.")
                else:
                    escolhidas_idx.add(idx)
                    carta_escolhida = cartas_puxadas[idx]
                    cartas_escolhidas.append(carta_escolhida)
                    
                    cartas_para_devolver.remove(carta_escolhida)
                    print(f"Adicionada: Rota de {carta_escolhida.valor} pontos")
                
                if len(cartas_escolhidas) == len(cartas_puxadas):
                    break

            except ValueError:
                print("Entrada inválida.")

        for carta in cartas_escolhidas:
            jogador_atual.add_carta_mao(carta)
            
        for carta in cartas_para_devolver:
            baralho_rota.colocar_no_fundo(carta) 
            
        print(f"Compra de rotas finalizada. {len(cartas_para_devolver)} carta(s) devolvida(s) ao fundo do baralho.")
        return True

    def reivindicar_rota_jogador(self, rota_num: int) -> bool:
        jogador_atual = self.get_jogador_atual()
        
        cartas_usadas = jogador_atual.reivindicar_rota(rota_num)
        
        if cartas_usadas:
            for carta in cartas_usadas:
                self.mesa.get_baralhoTrem().descartar(carta)
            return True
        else:
            return False