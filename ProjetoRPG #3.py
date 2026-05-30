import random
import time
import threading

def input(*args, **kwargs):
    texto = " ".join(map(str, args))

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.03)
    
    return __builtins__.input()

def print(*args, **kwargs):

    texto = " ".join(map(str, args))

    if texto.startswith(cl):
        __builtins__.print(texto, **kwargs)
        return

    end = kwargs.get("end", "\n")

    for letra in texto:
        __builtins__.print(letra, end="", flush=True)
        time.sleep(0.03)

    __builtins__.print(end=end)
    
def loja_inv(amarelo, branco, vermelho, pocao, reais, qtd):

    print(f"{amarelo}Comerciante:{branco} Bem vindo a Loja da Guilda, temos essa {vermelho}Poção{branco} que custa R${pocao}!")
    loja = input('''Você quer Comprar? Y/N:
>> ''').strip().lower() in ["sim", "s", "y"]
    print(cl)

    if loja:
        if reais < pocao:
            print(f"{amarelo}Comerciante:{branco} Você não tem {amarelo}Dinheiro{branco} Suficiente!")
            print(cl)
            
        
        else:
            qtd = int(input(f'''{amarelo}Comerciante:{branco} Quantas {vermelho}Poções{branco} Você Deseja?
>> '''))
            venda = qtd * pocao
            
            print(cl)
            
            if qtd <=0:
                print(f"{amarelo}Comerciante:{branco} Muito Engraçado... Saia da Minha Loja!!!")
                qtd = 0
                print(cl)
            
            elif reais < venda:
                while reais < venda:
                    print(f"Dinheiro Insuficiente! Tentando Comprar {vermelho}{qtd} Poções{branco}, mas Você só tem {amarelo}{reais} Reais!{branco}")
                    print()
                    qtd = int(input(f'''{amarelo}Comerciante:{branco} Quantas {vermelho}Poções{branco} Você Deseja?
>> '''))
                    venda = qtd * pocao
                    print(cl)

                    if reais >= venda:
                        reais -= venda
                        print(f"{amarelo}Comerciante:{branco} São Todas Suas Campeão!")
                        print(f"{cinza}Sistema:{branco}{vermelho} {qtd} Poções{branco} Adicionadas Ao Inventário")

                        if reais > 0:
                            print(f"{amarelo}Comerciante:{branco} Aqui está seu troco:",round(reais, 2))
                            print(cl)

                        else:
                            print(f"{amarelo}Comerciante:{branco} Você Torrou seu Dinheiro, Não tem Troco!")
                            print(cl)
                
            elif reais >= venda:
                reais -= venda
                print(f"{amarelo}Comerciante:{branco} São Todas Suas Campeão!")
                print(f"{cinza}Sistema:{branco}{vermelho} {qtd} Poções{branco} Adicionadas Ao Inventário")

                if reais > 0:
                    print(f"{amarelo}Comerciante:{branco} Aqui está seu troco:",round(reais, 2))
                    print(cl)

                else:
                    print(f"{amarelo}Comerciante:{branco} Você Torrou seu Dinheiro, Não tem Troco!")
                    print(cl)

            else:
                print("Resposta Inválida!")
                print(cl)   
                
    else:
        print(f"{amarelo}Comerciante:{branco} Volte Sempre!")
        print(cl)


    print("Este é Seu Inventário no Momento:")
    print(f"{vermelho}Poção: {qtd}{branco}") 
    if classe == "guerreiro":
        print("Espada de Ferro")
    elif classe == "executor":
        print("Machado de Batalha")
    elif classe == "mago":
        print("Cajado de Madeira")
    elif classe == "arqueiro":
        print("Arco de Madeira")
        print("Flechas Comuns")
        input("\nAperte ENTER Para Continuar: ")
    print(cl)

    return qtd, reais
qtd = 0
pocao = 50

cl = "-"*140

# Cores do Terminal

azul = "\033[34m"
branco = "\033[37m"
verde = "\033[32m"
amarelo = "\033[33m"
roxo = "\033[35m"
vermelho = "\033[31m"
verde1 = "\033[92m"
cinza = "\033[90m"

# Informações Iniciais

print(cl)
nome = input('''Qual é o Seu Nome?
>> ''')
print(cl)

while True:
    idade = int(input('''Quantos anos Você Tem?
>> '''))
    print(cl)

    if idade < 14:
        print("Você é Muito Novo(a) para Entrar na Guilda!")
        print(cl)
        continue
    
    elif idade > 40:
        print("Você já está Muito Velho(a) para Entrar na Guilda")
        print(cl)
        continue

    else:
        break

print("Escolha sua Classe, Por Favor!")
classe = input('''Mago / Executor / Guerreiro / Arqueiro
>> ''').lower()
print(cl)

while classe != "mago" and classe != "executor" and classe != "guerreiro" and classe != "arqueiro":
    print("Resposta Inválida! Tente Novamente!")
    classe = input('''Mago / Executor / Guerreiro / Arqueiro
>> ''').lower()
    print(cl)
    
print("Classe Escolhida:", classe.capitalize())

nível = 1
print(f"\nOlá {nome.capitalize()} Bem Vindo a Guilda dos Aventureiros, Você é um Novato(a) de nível:", nível)
print(cl)

print("Esses são seus atributos!")
input("\nAperte ENTER Para Continuar: ")
print(cl)

hp = nível * 50
mana = nível * 75
reais = nível * 100

print(f"{azul}Hp: {hp}")
print(f"{verde1}Mana: {mana}")
print(f"{amarelo}Dinheiro: {reais}{branco}")
print(f"Idade Atual: {idade}")
print(cl)

# Treinamento de 3 Anos
while True:

    train = int(input('''Como qualquer Iniciante Minimamente Inteligente, você decide Treinar, Mas por quantos Anos?
>> '''))
    if train >= 2 and train <= 16:
        anos = train
        for i in range(anos):
            barra = "■" * (i + 1)
            __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
            aumento = 6
            nível += aumento
            time.sleep(0.5)

        print("\nDurante seu Treinamento, Você Subiu de Nível, Parabéns!!!")
        print(f"{azul}Novo Nível: {nível}{branco}")
        print("Esses são seus novos atributos! ")
        input("\nAperte ENTER Para Continuar: ")
        print(cl)

        hp = nível * 50
        mana = nível * 75
        reais = nível * 100
        idade += anos

        print(f"{azul}Hp: {hp}")
        print(f"{verde1}Mana: {mana}")
        print(f"{amarelo}Dinheiro: {reais}{branco}")
        print(f"Idade Atual: {idade}")
        print(cl)
        time.sleep(2)
        break

    elif train <= 1:
        print("\nVocê precisa treinar por NO MÍNIMO, 2 Anos!")
        print()
        continue

    elif train >= 30:
        print("Você não precisa Treinar Tanto assim...")
        print()
        continue

    else:
        anos = train
        nível = 100
        for i in range(anos):
            barra = "■" * (i + 1)
            __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
            time.sleep(0.1)
        print("\nVocê treinou tanto, Que Alcançou o Nível 100(Máx)")
        print("Meus Parabéns!!!")
        print("Esses são seus novos atributos! ")
        input("\nAperte ENTER Para Continuar: ")
        print(cl)

        hp = nível * 50
        mana = nível * 75
        reais = nível * 100
        idade += anos

        print(f"{azul}Hp: {hp}")
        print(f"{verde1}Mana: {mana}")
        print(f"{amarelo}Dinheiro: {reais}{branco}")
        print(f"Idade Atual: {idade}")
        time.sleep(2)
        print(cl)
        break
    
qtd, reais = loja_inv(amarelo, branco, vermelho, pocao, reais, qtd)

def ataque_monstro(bosshp ,hp, nível):
    cnt = random.randint(1, 10)

    time.sleep(1.5)
    if bosshp > 0:
        if cnt >= 9:
            print()
            print(f"o {roxo}Dragão{branco} tentou Contra-Atacar mas Você Desviou!")
            input("\nAperte ENTER Para Continuar: ")
            print()
            print(cl)

        elif cnt >= 6:
            print()
            dn = nível * 5
            hp = hp - dn
            print(f"o {roxo}Dragão{branco} Contra-Atacou e pegou de Raspão!")
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            print()
            print(cl)

        elif cnt >= 3:
            print()
            print(f"o {roxo}Dragão{branco} Contra-Atacou e por Pouco não pega em Cheio!")
            dn = nível * 15
            hp = hp - dn
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            print()
            print(cl)

        else:
            print()
            print(f"O {roxo}Dragão{branco} Decidiu Contra-Atacar e Pegou em Cheio!")
            dn = nível * 25
            hp = hp - dn
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            print()
            print(cl)
    return hp

# Batalha contra o Dragão

bosshp = nível * 100
print(f"Oh Não, Apareceu um {roxo}Dragão {branco}e Ele está Atacando o Vilarejo!")

while bosshp > 0 and hp > 0:
    print(f"A Vida dele está em: {roxo}{bosshp}{branco}")
    print(f"Sua Vida está em {azul}{int(hp)}{branco}")
    print()

# Opções de Luta

    luta = None
    
    def ler_input():
        global luta
        luta = input(f'''Oque Você Fará? 1-Atacar / 2-Fugir / 3-Magia / 4-Bomba / 5-Poção {vermelho}(VOCÊ TEM 10 SEGUNDOS PARA RESPONDER){branco}
>> ''')
        
    thread = threading.Thread(target=ler_input)
    thread.daemon = True
    thread.start()
    thread.join(timeout=10)
    print()

# Luta = Atacar

    if luta == "1" and classe in ["guerreiro", "executor"]:
        sorte = random.randint(1, 100)

        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
            
        if sorte <= 20:
            print()
            print("Você errou o Ataque!!!")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif sorte >=21:
            atk = random.randint(1, 100)


            if atk >= 90:
                dano = 10000
                bosshp = bosshp - dano
                print()
                print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
                print("Matando ele na Hora!!!")
                print()
                print(cl)

            elif atk >= 60:
                dano = nível * 35
                bosshp = bosshp - dano
                print()
                print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)
                    
            elif atk >= 30:
                dano = nível * 25
                bosshp = bosshp - dano
                print()
                print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)
                        
            elif atk >= 1:
                dano = nível * 10
                bosshp = bosshp - dano
                print()
                print("Você Desferiu um corte na Perna dele!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)

    elif luta == "1" and classe == "mago":
        print()
        print("Um Mago não é tão bom em Combate Corpo a Corpo, Tente Usar Magias!!!")
        print()
        print(cl)

    elif luta == "1" and classe == "arqueiro":
        sorte = random.randint(1, 100)
            
        print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')

        if sorte <= 20:
            print()
            print("Você errou o Tiro!!!")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif sorte >=21:
            atk = random.randint(1, 100)

            if atk >= 90:
                dano = 10000
                bosshp = bosshp - dano
                print()
                print(f"Você atirou uma Flecha que perfurou o Coração do {roxo}Dragão{branco}")
                print("Matando ele na Hora!!!")
                print()
                print(cl)

            elif atk >= 60:
                dano = nível * 35
                bosshp = bosshp - dano
                print()
                print("Você atirou uma Flecha na Barriga dele! e ela entrou muito fundo!!!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)
                    
            elif atk >= 30:
                dano = nível * 25
                bosshp = bosshp - dano
                print()
                print("Você deu um tiro na cabeça dele, mas ele conseguiu desviar, o Tiro Acertou o rosto dele!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)
                        
            elif atk >= 1:
                dano = nível * 10
                bosshp = bosshp - dano
                print()
                print("Você atirou uma Flecha na Perna dele!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)


# Luta = Magia

    elif luta == "3" and classe == "mago":
        sorte = random.randint(1, 100)

        print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')

        print()
        print("Qual Magia Você Quer Usar?")
        magia = input('''1-Bola de Fogo / 2-Telecinese / 3-Congelamento
>> ''')
        print()
        print("Validando Magia, Aguarde...")
        time.sleep(1)
        print(cl)
            
        if sorte <= 10:
            print()
            print("Você Errou!!!")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif sorte >=11:
            mg = random.randint(1, 100)

            if mg >= 90 and mana >= 1000 and magia == "2":

                print()
                dano = 10000
                bosshp -= dano
                gasto = nível * 10
                mana -= gasto
                print("Você Esmagou o Crânio Dele!")
                print(f"Matando ele na hora e Gastando {verde1}{gasto} de Mana!{branco}")
                print()
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print(cl)

            elif mg >= 60 and mana >= 700 and magia == "2":
                dano = nível * 35
                bosshp -= dano
                gasto = nível * 7
                mana -= gasto
                print()
                print("Você Prensou ele com Duas Pedras!")
                print(f"Causando {roxo}{dano} de Dano!{branco} e Gastando {verde1}{gasto} de Mana!{branco}")
                print()
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)

            elif mg >= 30 and mana >= 550 and magia == "1":
                dano = nível * 25
                bosshp -= dano
                gasto = nível * 5.5
                mana -= gasto
                print()
                print("Você Lançou uma Bola de Fogo nele!")
                print(f"Causando {roxo}{dano} de Dano!{branco} e Gastando {verde1}{gasto} de Mana!{branco}")
                print()
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)

            elif mg >= 1 and mana >= 400 and magia == "3":
                dano = nível * 10
                bosshp -= dano
                gasto = nível * 4
                mana -= gasto
                print()
                print(f"Você Congelou ele, mas não foi tão Eficaz, Afinal, Ele é um {roxo}Dragão{branco} de Fogo!!!")
                print(f"Mas Causou {roxo}{dano} de Dano!{branco} e Gastou {verde1}{gasto} de Mana!{branco}")
                print()
                print(f"{verde1}Mana Restante: {mana}{branco}")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)

            elif mg >= 1 and mana <= 199:
                print()
                print(f"{verde1}Mana{branco} Insuficiente!")
                print()
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)

        elif sorte >=51 and mana <= 199:
            print()
            print(f"{verde1}Mana{branco} Insuficiente!")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

    elif luta == "3" and classe != "mago":
        print()
        print("Apenas Magos podem usar Magias!")
        print()
        print(cl)

# Luta = Fugir

    elif luta == "2":
        sorte = random.randint(1, 100)

        print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
            
        if sorte <= 60:
            print()
            print(f"sua Tentativa de Fuga Falhou, o {roxo}Dragão{branco}te Matou!!!")
            print(f"{vermelho}GAME OVER!{branco}")
            print()
            print(cl)
            break
                
        elif sorte >=61:
            print()
            print(f"Você Fugiu do {roxo}Dragão {branco}com Sucesso!")
            print("Porém, O Vilarejo foi Destruído...")
            print(f"{vermelho}GAME OVER!{branco}")
            print()
            print(cl)
            break

# Luta = Bomba

    elif luta == "4":
        sorte = random.randint(1, 100)

        print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
            
        if sorte <= 30:
            import time

            bomba = 5
            while bomba > 0:
                print(bomba)
                bomba -= 1
                time.sleep(0.3)
            print("BOOM!!!")
            print("Você Errou a Bomba!")
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
       
        elif sorte >=31:

            bomb = random.randint(1, 100)

            if bomb <= 40:
                import time

                bomba = 5
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.3)
                dano = nível * 50
                bosshp = bosshp - dano
                print("BOOM!!!")
                print(f"Na hora que o {roxo}Dragão {branco}Abriu a Boca, Você lançou a Bomba na Garganta Dele!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)
                    
            elif bomb >= 41:
                import time

                bomba = 5
                while bomba > 0:
                    print(bomba)
                    bomba -= 1
                    time.sleep(0.3)
                dano = nível * 30
                bosshp = bosshp - dano
                print("BOOM!!!")
                print(f"Você lançou a Bomba no {roxo}Dragão{branco}, Machucou Muito!")
                print(f"Causando {roxo}{dano} de Dano!{branco}")
                print(cl)

                hp = ataque_monstro(bosshp, hp, nível)

# Luta = Poção

    elif luta == "5":
        hp_max = nível * 50

        if qtd <= 0:
            print()
            print("Você Não tem Poções no Inventário!")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

        elif hp >= hp_max:
            print()
            print("Sua vida já está cheia! Não precisa usar Poção.")
            print()
            print(cl)

        else:
            cura = 200
            hp += cura

            if hp > hp_max:
                hp = hp_max

            qtd -= 1
            print()
            print(f"Você Bebeu uma {vermelho}Poção {branco}e Recuperou {int(cura)} de Vida!")
            print(f"{azul}Vida Atual: {int(hp)}{branco}")
            print(f"{vermelho}Poções Restantes: {qtd}{branco}")
            print()
            print(cl)

    elif luta == None:
        print("\nVocê demorou muito tempo para Responder!")
        print("Você foi Penalizado!")
        pena = hp * 0.10
        hp -= pena
        print(f"Você perdeu {hp} de Vida!")
        print()

# Ação Inválida

    else:
        print()
        print(f"Ação Inválida! Tente Novamente!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)
        
# Vitória

if bosshp <= 0 and hp <= 0:
    print()
    print("O Dragão Morreu mas ele conseguiu Te Matar junto com Ele!")
    print(f"{vermelho}GAME OVER???{branco}")
    print()
    print(cl)
      
elif bosshp <= 0:
    print()
    print(f"O {roxo}Dragão {branco}está Morto, Você salvou o Vilarejo!!!")
    print()
    print(f"{verde}Povo do Vilarejo:{branco} MUITO OBRIGADO {nome.upper()} VOCÊ NOS SALVOU, PEGUE ISSO COMO RECOMPENSA")
    input("\nAperte ENTER Para Continuar: ")
        
    win = 10000
    reais += win
    print()

    print(f"{amarelo}{win} Reais{branco} Adicionados ao Banco")
    print()

    print(f"Seu saldo Agora é:{amarelo}", round(reais, 2), "Reais")
    print()
    print(f"{branco}-"*140)

elif hp <= 0:
    print()
    print("Você está Morto!!!")
    print(f"{vermelho}GAME OVER!{branco}")
    print()
    print(cl)