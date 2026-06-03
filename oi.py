import time
import random
classe = "Executor"
nível = 100
bosshp = 10000000
hp = 100

def ataque_monstro(hp, bosshp):
    cnt = random.randint(1, 10)

    print(hp)
    print(bosshp)

    if cnt >= 9:
        print()
        print(f"o {roxo}Dragão{branco} tentou Contra-Atacar mas Você Desviou!")
        print()

    elif cnt >= 6:
        print()
        dn = nível * 5
        hp -= dn
        print(f"o {roxo}Dragão{branco} Contra-Atacou e pegou de Raspão!")
        print()

    elif cnt >= 3:
        print()
        print(f"o {roxo}Dragão{branco} Contra-Atacou e por Pouco não pega em Cheio!")
        dn = nível * 15
        hp -= dn
        print()

    else:
        print()
        print(f"O {roxo}Dragão{branco} Decidiu Contra-Atacar e Pegou em Cheio!")
        dn = nível * 25
        hp -= dn

    return hp, bosshp

# Cores do Terminal

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"
verde1 = "\033[92m"




while bosshp > 0:
    print(f"A Vida dele está em: {roxo}{bosshp}")
    print(f"Sua Vida está em {azul}{hp}{branco}")
    print()

# Opções de Luta

    luta = input("Oque Você Fará? 1-Atacar / 2-Fugir / 3-Magia / 4-Bomba: ")
    print()
    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print("-"*150)

# Luta = Atacar

    if luta == "1":
        sorte = random.randint(1, 100)
            
        if sorte <= 20:
            print()
            print("Você errou o Ataque!!!")
            print()
            print("-"*150)
                
        elif sorte >=21:
            d20 = random.randint(1, 100)

            if atk >= 90:
                dano = 10000
                bosshp = bosshp - dano
                print()
                print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
                print("Matando ele na Hora!!!")
                print()
                print("-"*150)
                

            elif atk >= 60:
                dano = nível * 35
                bosshp = bosshp - dano
                print()
                print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)

                hp, bosshp = ataque_monstro(hp, bosshp)
                    
            elif atk >= 30:
                dano = nível * 25
                bosshp = bosshp - dano
                print()
                print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)

                ataque_monstro(hp, bosshp)
                        
            elif atk >= 1:
                dano = nível * 10
                bosshp = bosshp - dano
                print()
                print("Você Desferiu um corte na Perna dele!")
                print(f"Causando {roxo}{dano}{branco} de Dano!")
                print()
                print("-"*150)

                ataque_monstro(hp, bosshp)
