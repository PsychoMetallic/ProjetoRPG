import random
import time
import os

energia = 100
turnos = 0
hora = 0
porta_esquerda = porta_direita = False
jogador_vivo = True

animatronics = {
    "Foxy": "Palco",
    "Bonnie": "Palco",
    "Chica": "Palco"
}

caminhos = {
    "Foxy": ["Palco", "Corredor Esquerdo", "Porta Esquerda"],
    "Bonnie": ["Palco", "Corredor Esquerdo", "Porta Esquerda"],
    "Chica": ["Palco", "Corredor Direito", "Porta Direita"]
}

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

def tp(texto, velocidade=0.03):
    for letra in texto:
        print(letra, end="", flush=True)
        time.sleep(velocidade)
    print()

def status():
    print("\n" + "-" * 40)
    print(f"HORA: {hora}AM")
    print(f"ENERGIA: {energia}%")
    print(f"Porta esquerda: {'FECHADA' if porta_esquerda else 'ABERTA'}")
    print(f"Porta direita: {'FECHADA' if porta_direita else 'ABERTA'}")
    print("-" * 40)

def mostrar_cameras():
    global energia
    if energia <= 0:
        return

    energia -= 5
    tp("\nAbrindo câmeras...")

    print("\n📷 CÂMERAS")
    print("-" * 30)

    for nome, local in animatronics.items():
        print(f"{nome}: {local}")

    print("-" * 30)
    input("\nPressione ENTER para fechar as câmeras...")

def mover_animatronics():
    for nome, caminho in caminhos.items():
        pos = caminho.index(animatronics[nome])

        if "Porta" in animatronics[nome]:
            porta = porta_esquerda if "Esquerda" in animatronics[nome] else porta_direita
            if porta:
                animatronics[nome] = "Palco"
            continue

        if random.randint(1, 100) <= 45 and pos < len(caminho) - 1:
            animatronics[nome] = caminho[pos + 1]

def verificar_ataque():
    for nome, lado in [("Foxy", "esquerda"), ("Bonnie", "esquerda"), ("Chica", "direita")]:
        if animatronics[nome] == f"Porta {lado.capitalize()}":
            if (lado == "esquerda" and not porta_esquerda) or (lado == "direita" and not porta_direita):
                jumpscare(nome)
            else:
                animatronics[nome] = "Palco"

def jumpscare(nome):
    global jogador_vivo

    limpar()
    tp("...")
    time.sleep(1)
    tp(f"{nome} entrou na sala!")
    time.sleep(1)

    print("""
██╗    ██╗ █████╗ ███████╗████████╗███████╗██████╗ 
██║    ██║██╔══██╗██╔════╝╚══██╔══╝██╔════╝██╔══██╗
██║ █╗ ██║███████║███████╗   ██║   █████╗  ██║  ██║
██║███╗██║██╔══██║╚════██║   ██║   ██╔══╝  ██║  ██║
╚███╔███╔╝██║  ██║███████║   ██║   ███████╗██████╔╝
 ╚══╝╚══╝ ╚═╝  ╚═╝╚══════╝   ╚═╝   ╚══════╝╚═════╝ 
""")

    jogador_vivo = False

def gastar_energia():
    global energia
    energia -= 2 + (4 if porta_esquerda else 0) + (4 if porta_direita else 0)

def menu():
    print("""
🐻 NOITE NO TERMINAL 🐻

Você é o guarda de uma pizzaria.
Seu objetivo é sobreviver até 6AM.

Comandos:
1 - Ver câmeras
2 - Fechar/Abrir porta esquerda
3 - Fechar/Abrir porta direita
4 - Esperar
""")

def jogar():
    global energia, hora, porta_esquerda, porta_direita, jogador_vivo, turnos

    limpar()
    menu()
    input("Pressione ENTER para começar...")

    while jogador_vivo and hora < 6:
        limpar()
        status()

        print("""
O que você deseja fazer?

1 - Ver câmeras
2 - Alternar porta esquerda
3 - Alternar porta direita
4 - Esperar
""")

        escolha = input("Escolha: ")

        if escolha == "1":
            mostrar_cameras()

        elif escolha == "2":
            porta_esquerda = not porta_esquerda
            energia -= 3
            print("Porta esquerda alterada!")

        elif escolha == "3":
            porta_direita = not porta_direita
            energia -= 3
            print("Porta direita alterada!")

        elif escolha == "4":
            print("Você esperou...")

        else:
            print("Comando inválido!")

        verificar_ataque()

        time.sleep(1)

        mover_animatronics()
        gastar_energia()

        turnos += 1

        if energia <= 0:
            energia = 0
            limpar()
            tp("A energia acabou...")
            time.sleep(1)
            tp("As portas se abriram sozinhas...")
            time.sleep(1)
            jumpscare("Freddy")
            break

        if turnos >= 2:
            hora += 1.5
            turnos = 0

    if jogador_vivo and hora >= 6:
        limpar()

        print("""
 ██████╗  █████╗ ███╗   ██╗██╗  ██╗ ██████╗ ██╗   ██╗
██╔════╝ ██╔══██╗████╗  ██║██║  ██║██╔═══██╗██║   ██║
██║  ███╗███████║██╔██╗ ██║███████║██║   ██║██║   ██║
██║   ██║██╔══██║██║╚██╗██║██╔══██║██║   ██║██║   ██║
╚██████╔╝██║  ██║██║ ╚████║██║  ██║╚██████╔╝╚██████╔╝
 ╚═════╝ ╚═╝  ╚═╝╚═╝   ╚═══╝╚═╝  ╚═╝ ╚═════╝  ╚═════╝
""")

        print("Você sobreviveu até 6AM! 🎉")


jogar()