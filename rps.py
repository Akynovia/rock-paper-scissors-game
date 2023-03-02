import random
import time

def clear():
    print('\033[H\033[J')

def animacao_mao(jogada):
    if jogada == 'pedra':
        print('    _______\n---\'   ____)\n      (_____)\n      (_____) \n      (____)\n---.__(___)')
    elif jogada == 'papel':
        print('    _______\n---\'   ____)____\n          ______)\n          _______) \n         _______)\n---.__________)')
    elif jogada == 'tesoura':
        print('    _______\n---\'   ____)____\n          ______)\n       __________) \n      (____)\n---.__(___)')

def menu():
    clear()
    print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
    print("Escolha uma opção:")
    print("1. Jogar")
    print("2. Ver ranking")
    print("3. Sair")

    opcao = input("> ")

    if opcao == '1':
        jogar()
    elif opcao == '2':
        ver_ranking()
    elif opcao == '3':
        exit()
    else:
        print("Opção inválida. Tente novamente.")
        time.sleep(1)
        menu()

def jogar():
    clear()
    nome_jogador = input("Digite seu nome: ")

    jogadas_possiveis = ['pedra', 'papel', 'tesoura']
    pontos_jogador = 0
    pontos_computador = 0
    rodada = 1

    while True:
        clear()
        print(f"Rodada {rodada}")
        print(f"{nome_jogador}: {pontos_jogador} pontos")
        print(f"Computador: {pontos_computador} pontos\n")

        jogada_jogador = input("Escolha sua jogada (pedra, papel ou tesoura): ")

        if jogada_jogador not in jogadas_possiveis:
            print("Jogada inválida. Tente novamente.")
            time.sleep(1)
            continue

        jogada_computador = random.choice(jogadas_possiveis)

        clear()
        print(f"{nome_jogador} jogou:")
        animacao_mao(jogada_jogador)
        time.sleep(1)
        print(f"\nComputador jogou:")
        animacao_mao(jogada_computador)
        time.sleep(1)

        if jogada_jogador == jogada_computador:
            print("Empate!")
        elif (jogada_jogador == 'pedra' and jogada_computador == 'tesoura') or \
             (jogada_jogador == 'papel' and jogada_computador == 'pedra') or \
             (jogada_jogador == 'tesoura' and jogada_computador == 'papel'):
            print(f"{nome_jogador} venceu!")
            pontos_jogador += 1
        else:
            print("Computador venceu!")
            pontos_computador += 1

        rodada += 1
        time.sleep(2)

        if rodada > 5:
            finalizar_jogo(nome_jogador, pontos_jogador
