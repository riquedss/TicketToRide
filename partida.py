from typing import List
from jogador import Jogador
from mesa import Mesa

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
        #Iniciando as ofertas na mesa
        mesa.set_ofertaTrem()
        mesa.set_ofertaRota()

        #Mostrando as catas da mesa 
        mesa.mostrar_mesa()
        print("Jogo iniciado!")

    def exibir_acoes(self):
        print("\nO que você deseja fazer?" \
        "\n1 - Comprar cartas" \
        "\n2 - Passar turno")
        return int(input().strip())
        

    def passar_turno(self):
        self.turnoAtual += 1
        if(self.get_jogador_atual() == len(self.get_jogadores())):
            self.jogadorAtual = 1 
        else:
            self.jogadorAtual += 1
        
        




