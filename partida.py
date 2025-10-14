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
        self.turnoAtual = 0

        print("partida inciada")
    
    def get_mesa(self):
        return self.mesa

    def iniciar(self):
        mesa = self.get_mesa()
        #Iniciando as ofertas na mesa
        mesa.set_ofertaTrem()
        mesa.set_ofertaRota()

        #Mostrando as catas da mesa 
        mesa.mostrar_mesa()
        print("Jogo iniciado!")

    def passar_turno(self):
        self.turnoAtual = (self.turnoAtual + 1) % len(self.jogadores)
        print(f"Turno de {self.jogadores[self.turnoAtual].nome}")



