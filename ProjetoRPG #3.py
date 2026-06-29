import random
import time
import threading
import os

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
    global nível

    print(f"{amarelo}Comerciante:{branco} Bem vindo a Loja da Guilda, temos essa {vermelho}Poção{branco} que custa R${pocao}!")
    loja = input('''Você quer Comprar? Y/N:
>> ''').strip().lower() in ["sim", "s", "y"]
    print(cl)

    if loja:
        if reais < pocao:
            print(f"{amarelo}Comerciante:{branco} Você não tem {amarelo}Dinheiro{branco} Suficiente!")
            print(cl)
            
        
        else:
            max_poc = nível * 2
            qtd = int(input(f'''{amarelo}Comerciante:{branco} Quantas {vermelho}Poções{branco} Você Deseja? (Máx: {max_poc})
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
                    max_poc = nível * 2
                    qtd = int(input(f'''{amarelo}Comerciante:{branco} Quantas {vermelho}Poções{branco} Você Deseja? (Máx: {max_poc})
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

def limpar():
    os.system("cls" if os.name == "nt" else "clear")

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
        print("\nVocê é Muito Novo(a) para Entrar na Guilda!")
        print(cl)
        continue
    
    elif idade > 40:
        print("\nVocê já está Muito Velho(a) para Entrar na Guilda")
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

    train = int(input('''Como qualquer Iniciante você decide Treinar, Mas por quantos Anos?
>> '''))
    if train >= 2 and train <= 16:
        anos = train
        for i in range(anos):
            barra = "■" * (i + 1)
            __builtins__.print(f"\rTreinando... [{barra:<{anos}}] {i+1}/{anos}",end="",flush=True)
            aumento = 6
            nível += aumento
            time.sleep(0.3)

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
        input("\nAperte ENTER Para Continuar: ")
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
            time.sleep(0.3)
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
        input("\nAperte ENTER Para Continuar: ")
        break

limpar()
qtd, reais = loja_inv(amarelo, branco, vermelho, pocao, reais, qtd)

# Definições da Batalha

def ataque_monstro(bosshp ,hp, nível):
    cnt = random.randint(1, 10)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    time.sleep(1.5)
    if bosshp > 0:
        if cnt >= 9:
            print()
            print(f"o {roxo}Dragão{branco} tentou Contra-Atacar mas Você Desviou!")
            input("\nAperte ENTER Para Continuar: ")

        elif cnt >= 6:
            print()
            dn = nível * 5
            hp = hp - dn
            print(f"o {roxo}Dragão{branco} Contra-Atacou e pegou de Raspão!")
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")

        elif cnt >= 3:
            print()
            print(f"o {roxo}Dragão{branco} Contra-Atacou e por Pouco não pega em Cheio!")
            dn = nível * 15
            hp = hp - dn
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            

        else:
            print()
            print(f"O {roxo}Dragão{branco} Decidiu Contra-Atacar e Pegou em Cheio!")
            dn = nível * 25
            hp = hp - dn
            print(f"Você Tomou {azul}{dn} de Dano{branco}")
            input("\nAperte ENTER Para Continuar: ")
            
    return hp

def ataque_corpo(bosshp, hp, nível, ataque_monstro):

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

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
        d20 = random.randint(1, 20)

        print(f'''Você jogou um D20 para Atacar!
O Número rolado foi: {d20}''')

        if d20 >= 14:
            dano = 10000
            bosshp = bosshp - dano
            print()
            print(f"Você deu Um SuperPulo e Cortou a Cabeça do {roxo}Dragão{branco}")
            print("Matando ele na Hora!!!")
            print()
            print(cl)

        elif d20 >= 10:
            dano = nível * 35
            bosshp = bosshp - dano
            print()
            print("Você Cortou a Barriga dele! o Corte foi Profundo!!!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif d20 >= 5:
            dano = nível * 25
            bosshp = bosshp - dano
            print()
            print("Você deu um Superpulo e Desferiu Vários Cortes em sequência no Rosto dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                    
        elif d20 == 1:
            dano = nível * 10
            bosshp = bosshp - dano
            print()
            print("Você Desferiu um corte na Perna dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp

def ataque_tiro(bosshp, hp, nível, ataque_monstro):
    sorte = random.randint(1, 100)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)
        
    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')

    if sorte <= 20:
        print()
        print("Você errou o Tiro!!!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)
            
    elif sorte >=21:
        d20 = random.randint(1, 20)

        print(f'''Você jogou um D20 para Atacar!
O Número rolado foi: {d20}''')

        if d20 >= 14:
            dano = 10000
            bosshp = bosshp - dano
            print()
            print(f"Você atirou uma Flecha que perfurou o Coração do {roxo}Dragão{branco}")
            print("Matando ele na Hora!!!")
            print()
            print(cl)

        elif d20 >= 10:
            dano = nível * 35
            bosshp = bosshp - dano
            print()
            print("Você atirou uma Flecha na Barriga dele! e ela entrou muito fundo!!!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                
        elif d20 >= 5:
            dano = nível * 25
            bosshp = bosshp - dano
            print()
            print("Você deu um tiro na cabeça dele, mas ele conseguiu desviar, o Tiro Acertou o rosto dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)
                    
        elif d20 == 1:
            dano = nível * 10
            bosshp = bosshp - dano
            print()
            print("Você atirou uma Flecha na Perna dele!")
            print(f"Causando {roxo}{dano} de Dano!{branco}")
            print()
            print(cl)

            hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp

def ataque_mago(bosshp, hp, nível, mana, ataque_monstro):
    sorte = random.randint(1, 100)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''Você rolou um D100!
Número: {sorte}''')

    print()
    print("Escolha sua magia:")
    magia = input('''1-Bola de Fogo / 2-Telecinese / 3-Congelamento
>> ''').strip()

    print("\nProcessando magia...")
    time.sleep(1)
    print(cl)

    # ❌ Falha geral do ataque
    if sorte <= 10:
        print("Você errou a magia!")
        hp = ataque_monstro(bosshp, hp, nível)
        return bosshp, hp, mana

    # 🎲 ataque normal
    d20 = random.randint(1, 20)
    print(f"Você rolou um D20: {d20}")

    # =========================
    # 🔮 TELECINESE
    # =========================
    if magia == "2":

        if mana < 700:
            print("Mana insuficiente para Telecinese!")
            hp = ataque_monstro(bosshp, hp, nível)
            return bosshp, hp, mana

        if d20 >= 14:
            dano = 10000
            gasto = nível * 10

            bosshp -= dano
            mana -= gasto

            print(f"Você esmagou o Dragão com telecinese!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        elif d20 >= 10:
            dano = nível * 35
            gasto = nível * 7

            bosshp -= dano
            mana -= gasto

            print(f"Você prensou o Dragão com pedras!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        else:
            print("Sua telecinese falhou!")

        hp = ataque_monstro(bosshp, hp, nível)

    # =========================
    # 🔥 BOLA DE FOGO
    # =========================
    elif magia == "1":

        if mana < 550:
            print("Mana insuficiente para Bola de Fogo!")
            hp = ataque_monstro(bosshp, hp, nível)
            return bosshp, hp, mana

        if d20 >= 10:
            dano = nível * 25
            gasto = int(nível * 5.5)

            bosshp -= dano
            mana -= gasto

            print(f"Bola de fogo acertou o Dragão!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        else:
            print("Sua bola de fogo falhou!")

        hp = ataque_monstro(bosshp, hp, nível)

    # =========================
    # ❄ CONGELAMENTO
    # =========================
    elif magia == "3":

        if mana < 400:
            print("Mana insuficiente para Congelamento!")
            hp = ataque_monstro(bosshp, hp, nível)
            return bosshp, hp, mana

        if d20 == 1:
            dano = nível * 10
            gasto = nível * 4

            bosshp -= dano
            mana -= gasto

            print("Você congelou o Dragão parcialmente!")
            print(f"Dano: {dano} | Mana: -{gasto}")

        else:
            print("O congelamento não foi eficaz!")

        hp = ataque_monstro(bosshp, hp, nível)

    # =========================
    # ❌ magia inválida
    # =========================
    else:
        print("Magia inválida!")
        hp = ataque_monstro(bosshp, hp, nível)

    return bosshp, hp, mana

def fuga_all(hp):
    sorte = random.randint(1, 100)

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
        
    if sorte <= 60:
        dano = 10000
        hp -= dano
        print()
        print(f"sua Tentativa de Fuga Falhou, o {roxo}Dragão{branco}te Matou!!!")
        print()
        
            
    elif sorte >=61:
        print()
        print(f"Você Fugiu do {roxo}Dragão {branco}com Sucesso!")
        print("Porém, O Vilarejo foi Destruído...")
        print(f"{vermelho}GAME OVER!{branco}")
        print()
        print(cl)

def ataque_bomba(bosshp, hp, nível, ataque_monstro):
    sorte = random.randint(1, 100)
    import time

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

    print(f'''você Rolou um D100!
o Número rolado Foi: {sorte}''')
        
    if sorte <= 30:

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
        d20 = random.randint(1, 20)

        print(f'''Você jogou um D20 para Atacar!
O Número rolado foi: {d20}''')

        if d20 <= 10:

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
                
        elif d20 >= 11:

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

    return bosshp, hp

def usar_pocao(bosshp, hp, nível, qtd, ataque_monstro):
    hp_max = nível * 50

    global azul, branco, vermelho, verde1, verde, cl, amarelo, roxo, cinza

    print("Validando Ação, Aguarde...")
    time.sleep(1)
    print(cl)

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
        porc = 0.10
        cura *= porc
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

    return qtd, hp

# Batalha contra o Dragão

bosshp = nível * 100
print(f"Oh Não, Apareceu um {roxo}Dragão {branco}e Ele está Atacando o Vilarejo!")
poc_tu = 0
input("\nAperte ENTER Para Continuar: ")

while bosshp > 0 and hp > 0:
    limpar()
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

        bosshp, hp = ataque_corpo(bosshp, hp, nível, ataque_monstro)

    elif luta == "1" and classe == "mago":
        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print()
        print("Um Mago não é tão bom em Combate Corpo a Corpo, Tente Usar Magias!!!")
        print()
        print(cl)

    elif luta == "1" and classe == "arqueiro":
        
        bosshp, hp = ataque_tiro(bosshp, hp, nível, ataque_monstro)

# Luta = Magia

    elif luta == "3" and classe == "mago":
        bosshp, hp, mana = ataque_mago(bosshp, hp, nível, mana, ataque_monstro)

    elif luta == "3" and classe != "mago":

        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print()
        print("Apenas Magos podem usar Magias!")
        print()
        print(cl)

# Luta = Fugir

    elif luta == "2":
        hp = fuga_all(hp)

# Luta = Bomba

    elif luta == "4":
        bosshp, hp = ataque_bomba(bosshp, hp, nível, ataque_monstro)

# Luta = Poção

    elif luta == "5":

        if poc_tu >= 3:
            print("\nVocê já usou o limite de 3 poções neste turno!")
            print(cl)
            hp = ataque_monstro(bosshp, hp, nível)
            poc_tu = 0
        else:
            qtd, hp = usar_pocao(bosshp, hp, nível, qtd, ataque_monstro)
            poc_tu += 1
        
#Luta = Sem Resposta

    elif luta == None:
        print("\nVocê demorou muito tempo para Responder!")
        print("Você foi Penalizado!")
        pena = hp * 0.10
        hp -= pena
        print(f"Você perdeu {pena} de Vida!")
        print()

# Ação Inválida

    else:
        print("Validando Ação, Aguarde...")
        time.sleep(1)
        print(cl)

        print()
        print(f"Ação Inválida! Tente Novamente!")
        print()
        print(cl)

        hp = ataque_monstro(bosshp, hp, nível)
        
# Final da Batalha
      
if bosshp <= 0:
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
    print({branco})
    print(cl)

elif hp <= 0:
    print()
    print("Você está Morto!!!")
    print(f"{vermelho}GAME OVER!{branco}")
    print()
    print(cl)