import random
import tkinter as tk
from tkinter import messagebox, simpledialog
from tkinter import ttk


class RPGGuildaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Guilda dos Aventureiros - RPG")
        self.root.geometry("900x620")
        self.root.minsize(800, 560)

        self.nome = ""
        self.idade = 0
        self.classe = ""
        self.nivel = 1
        self.hp = 50
        self.mana = 75
        self.reais = 100
        self.qtd_pocao = 0
        self.pocao_preco = 50
        self.bosshp = 0
        self.hp_max = self.hp
        self.bosshp_max = 0
        self.estado = "inicio"

        self.criar_tela()
        self.tela_inicio()

    def criar_tela(self):
        self.root.configure(bg="#151515")

        titulo = tk.Label(
            self.root,
            text="⚔️ Guilda dos Aventureiros 🐉",
            font=("Arial", 22, "bold"),
            bg="#151515",
            fg="#f1c40f",
        )
        titulo.pack(pady=10)

        self.status_frame = tk.Frame(self.root, bg="#202020", bd=2, relief="ridge")
        self.status_frame.pack(fill="x", padx=15, pady=5)

        self.status_label = tk.Label(
            self.status_frame,
            text="Status aparecerá aqui",
            font=("Consolas", 12),
            bg="#202020",
            fg="white",
            justify="left",
        )
        self.status_label.pack(padx=10, pady=8, anchor="w")

        self.barras_frame = tk.Frame(self.status_frame, bg="#202020")
        self.barras_frame.pack(fill="x", padx=10, pady=(0, 10))

        self.player_barra = self.criar_barra_vida(self.barras_frame, "⚔️ Jogador", "#c0392b")
        self.boss_barra = self.criar_barra_vida(self.barras_frame, "🐉 Dragão", "#8e44ad")

        self.texto = tk.Text(
            self.root,
            height=18,
            font=("Consolas", 12),
            bg="#101010",
            fg="#eeeeee",
            insertbackground="white",
            wrap="word",
            state="disabled",
        )
        self.texto.pack(fill="both", expand=True, padx=15, pady=10)

        self.botoes_frame = tk.Frame(self.root, bg="#151515")
        self.botoes_frame.pack(fill="x", padx=15, pady=10)

    def escrever(self, mensagem):
        self.texto.config(state="normal")
        self.texto.insert("end", mensagem + "\n")
        self.texto.see("end")
        self.texto.config(state="disabled")

    def limpar_texto(self):
        self.texto.config(state="normal")
        self.texto.delete("1.0", "end")
        self.texto.config(state="disabled")

    def limpar_botoes(self):
        for widget in self.botoes_frame.winfo_children():
            widget.destroy()

    def botao(self, texto, comando):
        btn = tk.Button(
            self.botoes_frame,
            text=texto,
            command=comando,
            font=("Arial", 12, "bold"),
            bg="#333333",
            fg="white",
            activebackground="#555555",
            activeforeground="white",
            width=18,
            height=2,
        )
        btn.pack(side="left", padx=5, pady=5)
        return btn

    def criar_barra_vida(self, parent, titulo, cor):
        frame = tk.Frame(parent, bg="#202020")
        frame.pack(fill="x", pady=3)

        label = tk.Label(
            frame,
            text=f"{titulo}: 0/0",
            font=("Consolas", 11, "bold"),
            bg="#202020",
            fg="white",
            anchor="w",
        )
        label.pack(fill="x")

        canvas = tk.Canvas(frame, height=22, bg="#101010", highlightthickness=1, highlightbackground="#444444")
        canvas.pack(fill="x")

        barra = {"label": label, "canvas": canvas, "cor": cor, "titulo": titulo}
        canvas.bind("<Configure>", lambda event: self.atualizar_status())
        return barra

    def atualizar_barra_vida(self, barra, atual, maximo):
        canvas = barra["canvas"]
        canvas.delete("all")

        maximo = max(1, int(maximo))
        atual = max(0, min(int(atual), maximo))
        proporcao = atual / maximo

        largura = max(canvas.winfo_width(), 1)
        altura = max(canvas.winfo_height(), 22)
        preenchido = int(largura * proporcao)

        canvas.create_rectangle(0, 0, largura, altura, fill="#2b2b2b", width=0)
        canvas.create_rectangle(0, 0, preenchido, altura, fill=barra["cor"], width=0)
        canvas.create_text(
            largura // 2,
            altura // 2,
            text=f"{atual}/{maximo}",
            fill="white",
            font=("Consolas", 10, "bold"),
        )

        barra["label"].config(text=f"{barra['titulo']}: {atual}/{maximo}")

    def atualizar_status(self):
        self.status_label.config(
            text=(
                f"👤 Nome: {self.nome or '-'} | Classe: {self.classe.capitalize() or '-'} | Idade: {self.idade}\n"
                f"⭐ Nível: {self.nivel} | 🔮 Mana: {int(self.mana)} | 💰 Dinheiro: R${round(self.reais, 2)} | 🧪 Poções: {self.qtd_pocao}"
            )
        )

        self.atualizar_barra_vida(self.player_barra, self.hp, self.hp_max)
        self.atualizar_barra_vida(self.boss_barra, self.bosshp, self.bosshp_max if self.bosshp_max > 0 else 1)

    def tela_inicio(self):
        self.limpar_texto()
        self.limpar_botoes()
        self.escrever("Bem-vindo à Guilda dos Aventureiros!")
        self.escrever("Clique em começar para criar seu personagem.")
        self.botao("Começar", self.criar_personagem)
        self.atualizar_status()

    def criar_personagem(self):
        nome = simpledialog.askstring("Nome", "Qual é o seu nome?")
        if not nome:
            return

        idade = simpledialog.askinteger("Idade", "Quantos anos você tem?", minvalue=1, maxvalue=120)
        if idade is None:
            return

        if idade < 14:
            messagebox.showwarning("Guilda", "Você é muito novo(a) para entrar na Guilda!")
            return
        if idade > 40:
            messagebox.showwarning("Guilda", "Você já está muito velho(a) para entrar na Guilda!")
            return

        self.nome = nome.strip().capitalize()
        self.idade = idade
        self.escolher_classe()

    def escolher_classe(self):
        self.limpar_texto()
        self.limpar_botoes()
        self.escrever(f"Olá, {self.nome}! Agora escolha sua classe:")
        self.botao("Mago", lambda: self.definir_classe("mago"))
        self.botao("Executor", lambda: self.definir_classe("executor"))
        self.botao("Guerreiro", lambda: self.definir_classe("guerreiro"))
        self.botao("Arqueiro", lambda: self.definir_classe("arqueiro"))

    def definir_classe(self, classe):
        self.classe = classe
        self.nivel = 1
        self.hp = self.nivel * 50
        self.hp_max = self.hp
        self.mana = self.nivel * 75
        self.reais = self.nivel * 100
        self.limpar_texto()
        self.escrever(f"Classe escolhida: {classe.capitalize()}!")
        self.escrever(f"Bem-vindo(a), {self.nome}, novato(a) de nível {self.nivel}.")
        self.escrever("Seus atributos iniciais foram definidos.")
        self.atualizar_status()
        self.tela_treino()

    def tela_treino(self):
        self.limpar_botoes()
        self.escrever("\nAntes da aventura começar, você precisa treinar.")
        self.escrever("Escolha quantos anos deseja treinar:")
        self.botao("2 anos", lambda: self.treinar(2))
        self.botao("5 anos", lambda: self.treinar(5))
        self.botao("10 anos", lambda: self.treinar(10))
        self.botao("16 anos", lambda: self.treinar(16))
        self.botao("Outro valor", self.treino_personalizado)

    def treino_personalizado(self):
        anos = simpledialog.askinteger("Treino", "Treinar por quantos anos?", minvalue=1, maxvalue=100)
        if anos is not None:
            self.treinar(anos)

    def treinar(self, anos):
        if anos <= 1:
            messagebox.showwarning("Treino", "Você precisa treinar por no mínimo 2 anos!")
            return
        if anos >= 30:
            self.nivel = 100
            self.escrever("\nVocê treinou tanto que alcançou o nível 100, o nível máximo!")
        elif 2 <= anos <= 16:
            self.nivel += anos * 6
            self.escrever(f"\nVocê treinou por {anos} anos e ficou muito mais forte!")
        else:
            self.nivel = 100
            self.escrever("\nVocê treinou demais e alcançou o nível máximo!")

        self.idade += anos
        self.hp = self.nivel * 50
        self.hp_max = self.hp
        self.mana = self.nivel * 75
        self.reais = self.nivel * 100
        self.atualizar_status()
        self.tela_loja()

    def tela_loja(self):
        self.limpar_botoes()
        self.escrever("\n🧪 Comerciante: Bem-vindo à Loja da Guilda!")
        self.escrever(f"Cada poção custa R${self.pocao_preco}.")
        self.botao("Comprar poções", self.comprar_pocao)
        self.botao("Continuar", self.iniciar_batalha)

    def comprar_pocao(self):
        qtd = simpledialog.askinteger("Loja", "Quantas poções deseja comprar?", minvalue=0, maxvalue=999)
        if qtd is None:
            return
        if qtd <= 0:
            self.escrever("Comerciante: Muito engraçado... saia da minha loja!")
            return

        custo = qtd * self.pocao_preco
        if self.reais < custo:
            messagebox.showwarning("Loja", f"Dinheiro insuficiente! Você tem R${round(self.reais, 2)}.")
            return

        self.reais -= custo
        self.qtd_pocao += qtd
        self.escrever(f"Você comprou {qtd} poção/poções por R${custo}.")
        self.atualizar_status()

    def iniciar_batalha(self):
        self.limpar_texto()
        self.limpar_botoes()
        self.bosshp = self.nivel * 100
        self.bosshp_max = self.bosshp
        self.escrever("🐉 Oh não! Um Dragão apareceu e está atacando o vilarejo!")
        self.atualizar_status()
        self.tela_batalha()

    def tela_batalha(self):
        self.limpar_botoes()
        if self.verificar_fim():
            return
        self.escrever("\nO que você fará?")
        self.botao("Atacar", self.acao_atacar)
        self.botao("Fugir", self.acao_fugir)
        self.botao("Magia", self.acao_magia)
        self.botao("Bomba", self.acao_bomba)
        self.botao("Poção", self.acao_pocao)
        self.atualizar_status()

    def contra_ataque_dragao(self):
        if self.bosshp <= 0:
            return

        cnt = random.randint(1, 10)
        if cnt >= 9:
            self.escrever("O Dragão tentou contra-atacar, mas você desviou!")
        elif cnt >= 6:
            dano = self.nivel * 5
            self.hp -= dano
            self.escrever(f"O Dragão acertou de raspão! Você tomou {dano} de dano.")
        elif cnt >= 3:
            dano = self.nivel * 15
            self.hp -= dano
            self.escrever(f"O Dragão quase acertou em cheio! Você tomou {dano} de dano.")
        else:
            dano = self.nivel * 25
            self.hp -= dano
            self.escrever(f"O Dragão acertou em cheio! Você tomou {dano} de dano.")

    def rolar_d20(self):
        d20 = random.randint(1, 20)
        self.escrever(f"Você rolou um D20: {d20}")
        return d20

    def acao_atacar(self):
        if self.classe == "mago":
            self.escrever("Um mago não é tão bom no combate corpo a corpo. Tente usar magias!")
            self.contra_ataque_dragao()
            self.tela_batalha()
            return

        d20 = self.rolar_d20()

        if d20 == 20:
            dano = 10000
            self.escrever("Ataque crítico! Você acertou um golpe mortal no Dragão!")
        elif d20 >= 15:
            dano = self.nivel * 35
            self.escrever(f"Você acertou um golpe profundo, causando {dano} de dano!")
        elif d20 >= 10:
            dano = self.nivel * 25
            self.escrever(f"Você acertou vários golpes rápidos, causando {dano} de dano!")
        elif d20 >= 5:
            dano = self.nivel * 10
            self.escrever(f"Você acertou a perna dele, causando {dano} de dano!")
        else:
            self.escrever("Você errou o ataque!")
            self.contra_ataque_dragao()
            self.tela_batalha()
            return

        self.bosshp -= dano
        self.contra_ataque_dragao()
        self.tela_batalha()

    def acao_magia(self):
        if self.classe != "mago":
            self.escrever("Apenas magos podem usar magias!")
            self.contra_ataque_dragao()
            self.tela_batalha()
            return

        self.limpar_botoes()
        self.escrever("Escolha sua magia:")
        self.botao("Bola de Fogo", lambda: self.usar_magia("bola"))
        self.botao("Telecinese", lambda: self.usar_magia("telecinese"))
        self.botao("Congelamento", lambda: self.usar_magia("gelo"))
        self.botao("Voltar", self.tela_batalha)

    def usar_magia(self, magia):
        custos = {"bola": self.nivel * 5.5, "telecinese": self.nivel * 7, "gelo": self.nivel * 4}
        nomes = {"bola": "Bola de Fogo", "telecinese": "Telecinese", "gelo": "Congelamento"}
        custo = custos[magia]

        if self.mana < custo:
            self.escrever("Mana insuficiente!")
            self.contra_ataque_dragao()
            self.tela_batalha()
            return

        d20 = self.rolar_d20()
        self.mana -= custo

        if d20 <= 4:
            self.escrever("Você errou a magia!")
            self.contra_ataque_dragao()
            self.tela_batalha()
            return
        elif magia == "telecinese" and d20 == 20:
            dano = 10000
            self.escrever("Você esmagou o Dragão com telecinese. Foi um golpe mortal!")
        elif d20 >= 15:
            dano = self.nivel * 35
            self.escrever(f"{nomes[magia]} causou {dano} de dano!")
        elif d20 >= 10:
            dano = self.nivel * 25
            self.escrever(f"{nomes[magia]} acertou o Dragão e causou {dano} de dano!")
        else:
            dano = self.nivel * 10
            self.escrever(f"{nomes[magia]} teve pouco efeito e causou {dano} de dano!")

        self.escrever(f"Mana gasta: {int(custo)}")
        self.bosshp -= dano
        self.contra_ataque_dragao()
        self.tela_batalha()

    def acao_bomba(self):
        d20 = self.rolar_d20()

        if d20 <= 4:
            self.escrever("BOOM! Você errou a bomba!")
            self.contra_ataque_dragao()
            self.tela_batalha()
            return
        elif d20 >= 15:
            dano = self.nivel * 50
            self.escrever(f"A bomba explodiu na garganta do Dragão! Dano: {dano}")
        else:
            dano = self.nivel * 30
            self.escrever(f"A bomba explodiu perto do Dragão! Dano: {dano}")

        self.bosshp -= dano
        self.contra_ataque_dragao()
        self.tela_batalha()

    def acao_pocao(self):
        hp_max = self.hp_max
        if self.qtd_pocao <= 0:
            self.escrever("Você não tem poções no inventário!")
            self.contra_ataque_dragao()
        elif self.hp >= hp_max:
            self.escrever("Sua vida já está cheia!")
        else:
            cura = 200
            self.hp = min(hp_max, self.hp + cura)
            self.qtd_pocao -= 1
            self.escrever(f"Você usou uma poção e recuperou {cura} de vida!")
        self.tela_batalha()

    def acao_fugir(self):
        d20 = self.rolar_d20()
        if d20 <= 12:
            self.hp = 0
            self.escrever("Sua tentativa de fuga falhou. O Dragão te derrotou!")
        else:
            self.escrever("Você fugiu com sucesso, mas o vilarejo foi destruído...")
            self.hp = 0
        self.tela_batalha()

    def verificar_fim(self):
        self.atualizar_status()
        if self.bosshp <= 0 and self.hp <= 0:
            self.escrever("\nO Dragão morreu, mas conseguiu te derrotar junto. GAME OVER???")
        elif self.bosshp <= 0:
            win = 10000
            self.reais += win
            self.escrever("\n🎉 O Dragão está morto! Você salvou o vilarejo!")
            self.escrever(f"O povo te recompensou com R${win}!")
            self.atualizar_status()
        elif self.hp <= 0:
            self.escrever("\n💀 Você está morto. GAME OVER!")
        else:
            return False

        self.limpar_botoes()
        self.botao("Jogar novamente", self.reiniciar)
        self.botao("Sair", self.root.destroy)
        return True

    def reiniciar(self):
        self.nome = ""
        self.idade = 0
        self.classe = ""
        self.nivel = 1
        self.hp = 50
        self.hp_max = 50
        self.mana = 75
        self.reais = 100
        self.qtd_pocao = 0
        self.bosshp = 0
        self.bosshp_max = 0
        self.tela_inicio()


if __name__ == "__main__":
    root = tk.Tk()
    app = RPGGuildaGUI(root)
    root.mainloop()
