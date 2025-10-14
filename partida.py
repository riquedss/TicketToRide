from typing import List
from jogador import Jogador
from mesa import Mesa
from carta import CartaTrem

class Partida:
    def __init__(self): 
        #Define a quantidade de jogadores
        print("BEM VINDO AO ESTACAO TERMINAL")
        print("Entre com a quantidade de jogadores (2-4): ")
        num_jogadores = int(input().strip())
        if num_jogadores < 2 or num_jogadores > 4:
            print("Número inválido de jogadores. Encerrando o jogo.")
            exit(1)
        jogadores = List[Jogador]

        jogadores = [Jogador(i+1) for i in range(num_jogadores)]
        mesa = Mesa()  # Baralhos serão inicializados posteriormente

        self.jogadores = jogadores
        self.mesa = mesa
        self.turnoAtual = 1
        self.jogadorAtual = 1

        self.cartas_selecionas_turno: List[CartaTrem] = []

        print("partida inciada")
    
    def get_mesa(self):
        return self.mesa
    
    def get_jogadores(self):
        return self.jogadores

    def get_jogador_atual(self):
        return self.jogadorAtual
    
    def set_jogador_atual(self, numJogador):
        self.jogadorAtual = numJogador

    def iniciar(self):
        mesa = self.get_mesa()
        jogadores = self.get_jogadores()

        cartasLocomotivas = []
        for i, j in enumerate(jogadores,1):
            cartasLocomotivas.append(mesa.get_baralhoTrem().pegar_carta_topo())

        mesa.get_baralhoRota().embaralhar()
        mesa.get_baralhoTrem().embaralhar()

        for i, j in enumerate(jogadores,1):
            cartasMaoTrem = []
            cartasMaoRota = []
            cartasMaoTrem.append(cartasLocomotivas.pop())
            for _ in range(5):
                cartasMaoTrem.append(mesa.get_baralhoTrem().pegar_carta_topo())
            j.set_cartas_trem(cartasMaoTrem)
            for _ in range(3):
                cartasMaoRota.append(mesa.get_baralhoRota().pegar_carta_topo())
                j.set_cartas_rota(cartasMaoRota)

        #Iniciando as ofertas na mesa
        mesa.set_ofertaTrem()
        mesa.set_ofertaRota()
        

        #Mostrando as catas da mesa 
        mesa.mostrar_mesa()

    def exibir_acoes(self):
        print("\nO que você deseja fazer?" \
        "\n1 - Comprar cartas" \
        "\n2 - Exibir cartas da mesa" \
        "\n3 - Exibir minhas cartas" \
        "\n4 - Passar turno")
        return int(input().strip())
    
    def registrar_carta_escolhida(self, carta):
        self.cartas_selecionas_turno.append(carta)
    
    def qtd_cartas_selecionadas_turno(self):
        return len(self.cartas_selecionas_turno)

    def passar_turno(self):
        jogadores = self.get_jogadores()
        num_jogador_atual = self.jogadorAtual

        self.add_cartas_mao_jogador(jogadores[num_jogador_atual - 1])
        self.cartas_selecionas_turno.clear()

        self.turnoAtual += 1
        if(num_jogador_atual == len(jogadores)):
            self.jogadorAtual = 1 
        else:
            self.jogadorAtual += 1
    
    def add_cartas_mao_jogador(self, jogador_atual):
        for carta in self.cartas_selecionas_turno:
            jogador_atual.add_carta_mao(carta)
        
        




