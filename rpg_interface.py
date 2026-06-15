import random
import time
import threading
import tkinter as tk
from tkinter import ttk

# ==============================
# UI helpers
# ==============================

def typewriter_append(widget: tk.Text, text: str, delay=8):
    """Append text char-by-char. delay is in ms."""
    def run():
        widget.after(0, lambda: widget.configure(state="normal"))
        for ch in text:
            widget.after(0, lambda c=ch: widget.insert("end", c))
            time.sleep(delay / 1000)
        widget.after(0, lambda: widget.see("end"))
        widget.after(0, lambda: widget.configure(state="disabled"))
    threading.Thread(target=run, daemon=True).start()


class RPGState:
    def __init__(self):
        self.nome = ""
        self.classe = ""
        self.idade = 0
        self.nivel = 1
        self.hp = 0
        self.mana = 0
        self.reais = 0
        self.qtd_pocao = 0
        self.pocao_preco = 50

        # Dragon
        self.bosshp = 0
        self.max_hp = 0

    def recalc_stats(self):
        self.hp = self.nivel * 50
        self.max_hp = self.hp
        self.mana = self.nivel * 75
        self.reais = self.nivel * 100


# ==============================
# Game logic (ported from the console version)
# ==============================

class GameLogic:
    def __init__(self, state: RPGState, log_callback):
        self.s = state
        self.log = log_callback
        self.cl = "-" * 70

        # Colors are just strings for UI emphasis.
        self.azul = "[AZUL]"
        self.branco = "[BRANCO]"
        self.roxo = "[ROXO]"
        self.vermelho = "[VERMELHO]"
        self.amarelo = "[AMARELO]"
        self.verde = "[VERDE]"
        self.verde1 = "[VERDE1]"
        self.cinza = "[CINZA]"

    def println(self, msg: str):
        self.log(msg + "\n")

    def p_wait(self, sec=0.4):
        # keep it light; GUI already has pacing.
        time.sleep(sec)

    def ataque_monstro(self, bosshp, hp, nivel):
        cnt = random.randint(1, 10)
        if bosshp > 0:
            if cnt >= 9:
                self.println(f"{self.roxo}Dragão{self.branco} tentou contra-atacar mas você desviou!")
            elif cnt >= 6:
                dn = nivel * 5
                hp -= dn
                self.println(f"{self.roxo}Dragão{self.branco} contra-atacou de raspão! Você tomou {self.azul}{dn} de dano{self.branco}.")
            elif cnt >= 3:
                dn = nivel * 15
                hp -= dn
                self.println(f"{self.roxo}Dragão{self.branco} quase pegou em cheio! Você tomou {self.azul}{dn} de dano{self.branco}.")
            else:
                dn = nivel * 25
                hp -= dn
                self.println(f"{self.roxo}Dragão{self.branco} pegou em cheio! Você tomou {self.azul}{dn} de dano{self.branco}.")
        return hp

    def ataque_corpo(self, bosshp, hp, nivel):
        self.println("Validando ação...")
        sorte = random.randint(1, 100)
        self.println(f"Você rolou um D100. Número: {sorte}")

        if sorte <= 20:
            self.println("Você errou o ataque!")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        else:
            d20 = random.randint(1, 20)
            self.println(f"Você jogou um D20 para atacar. Número: {d20}")

            if d20 >= 14:
                dano = 10000
                bosshp -= dano
                self.println(f"Superpulo! Você cortou a cabeça do {self.roxo}Dragão{self.branco}. Matando na hora!")

            elif d20 >= 10:
                dano = nivel * 35
                bosshp -= dano
                self.println("Você cortou a barriga! Corte profundo!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

            elif d20 >= 5:
                dano = nivel * 25
                bosshp -= dano
                self.println("Superpulo + cortes no rosto!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

            elif d20 == 1:
                dano = nivel * 10
                bosshp -= dano
                self.println("Corte na perna!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

            else:
                # d20 == 2..4, little effect
                dano = nivel * 10
                bosshp -= dano
                self.println("Ataque fraco!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

        return bosshp, hp

    def ataque_tiro(self, bosshp, hp, nivel):
        self.println("Validando ação...")
        sorte = random.randint(1, 100)
        self.println(f"Você rolou um D100. Número: {sorte}")

        if sorte <= 20:
            self.println("Você errou o tiro!")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        else:
            d20 = random.randint(1, 20)
            self.println(f"Você jogou um D20 para atirar. Número: {d20}")

            if d20 >= 14:
                dano = 10000
                bosshp -= dano
                self.println(f"Você atirou uma flecha no coração do {self.roxo}Dragão{self.branco}. Matando na hora!")

            elif d20 >= 10:
                dano = nivel * 35
                bosshp -= dano
                self.println("Você acertou a barriga! A flecha entrou fundo!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

            elif d20 >= 5:
                dano = nivel * 25
                bosshp -= dano
                self.println("Tiro na cabeça! Ele desviou um pouco, mas você acertou o rosto!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

            elif d20 == 1:
                dano = nivel * 10
                bosshp -= dano
                self.println("Você acertou a perna!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

            else:
                dano = nivel * 10
                bosshp -= dano
                self.println("Tiro fraco!")
                self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
                hp = self.ataque_monstro(bosshp, hp, nivel)

        return bosshp, hp

    def ataque_mago(self, bosshp, hp, nivel, mana):
        self.println("Validando ação...")
        sorte = random.randint(1, 100)
        self.println(f"Você rolou um D100. Número: {sorte}")

        if sorte <= 10:
            self.println("Você errou o feitiço!")
            hp = self.ataque_monstro(bosshp, hp, nivel)
            return bosshp, hp, mana

        d20 = random.randint(1, 20)
        self.println(f"D20 para atacar. Número: {d20}")

        # magic selection will be passed externally (via self.selected_magic)
        magic = getattr(self, "selected_magic", "1")

        def need(m_needed):
            return mana >= m_needed

        # Telecinese (2)
        if d20 >= 14 and magic == "2" and need(nivel * 10):
            dano = 10000
            bosshp -= dano
            gasto = nivel * 10
            mana -= gasto
            self.println("Você esmagou o crânio do Dragão!")
            self.println(f"Gastando {self.verde1}{gasto} de mana!{self.branco}")
            self.println(f"Mana restante: {mana}{self.branco}")

        elif d20 >= 10 and magic == "2" and need(nivel * 7):
            dano = nivel * 35
            bosshp -= dano
            gasto = nivel * 7
            mana -= gasto
            self.println("Telecinese potente: duas pedras prensando!")
            self.println(f"Causando {self.roxo}{dano} de dano!{self.branco} e gastando {self.verde1}{gasto} de mana!{self.branco}")
            self.println(f"Mana restante: {mana}{self.branco}")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        elif d20 >= 5 and magic == "1" and need(int(nivel * 5.5)):
            dano = nivel * 25
            bosshp -= dano
            gasto = int(nivel * 5.5)
            mana -= gasto
            self.println("Bola de fogo!")
            self.println(f"Causando {self.roxo}{dano} de dano!{self.branco} e gastando {self.verde1}{gasto} de mana!{self.branco}")
            self.println(f"Mana restante: {mana}{self.branco}")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        elif d20 == 1 and magic == "3" and need(nivel * 4):
            dano = nivel * 10
            bosshp -= dano
            gasto = nivel * 4
            mana -= gasto
            self.println(f"Congelamento! Mas o Dragão é de fogo... mesmo assim acertou.")
            self.println(f"Causando {self.roxo}{dano} de dano!{self.branco} e gastando {self.verde1}{gasto} de mana!{self.branco}")
            self.println(f"Mana restante: {mana}{self.branco}")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        else:
            # Not enough mana or mismatch
            if mana <= 199:
                self.println(f"{self.verde1}Mana insuficiente!{self.branco}")
            else:
                self.println("O feitiço não encontrou o ponto certo...")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        return bosshp, hp, mana

    def fuga_all(self, hp):
        sorte = random.randint(1, 100)
        self.println(f"Você rolou um D100 para fugir. Número: {sorte}")
        if sorte <= 60:
            dano = 10000
            hp -= dano
            self.println(f"Falha! O {self.roxo}Dragão{self.branco} te matou!")
        else:
            self.println(f"Você fugiu do {self.roxo}Dragão{self.branco} com sucesso!")
            self.println("Porém, o vilarejo foi destruído... GAME OVER!")
            hp = -1
        return hp

    def ataque_bomba(self, bosshp, hp, nivel):
        sorte = random.randint(1, 100)
        self.println(f"Você rolou um D100 para bombear. Número: {sorte}")
        if sorte <= 30:
            self.println("Você errou a bomba...")
            hp = self.ataque_monstro(bosshp, hp, nivel)
            return bosshp, hp

        d20 = random.randint(1, 20)
        self.println(f"D20 de resultado. Número: {d20}")

        bomba = 5
        for _ in range(bomba):
            self.println(f"Contagem: {bomba}")
            time.sleep(0.15)
            bomba -= 1
        self.println("BOOM!!!")

        if d20 <= 10:
            dano = nivel * 50
            bosshp -= dano
            self.println(f"Na hora que o {self.roxo}Dragão{self.branco} abriu a boca, você lançou a bomba na garganta! ")
            self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
            hp = hp  # monstro responde via função logo abaixo
            hp = self.ataque_monstro(bosshp, hp, nivel)
        else:
            dano = nivel * 30
            bosshp -= dano
            self.println(f"Você lançou a bomba no {self.roxo}Dragão{self.branco}, machucou muito!")
            self.println(f"Causando {self.roxo}{dano} de dano!{self.branco}")
            hp = self.ataque_monstro(bosshp, hp, nivel)

        return bosshp, hp

    def usar_pocao(self, bosshp, hp, nivel, qtd):
        hp_max = nivel * 50
        if qtd <= 0:
            self.println("Você não tem poções no inventário!")
            hp = self.ataque_monstro(bosshp, hp, nivel)
            return qtd, hp

        if hp >= hp_max:
            self.println("Sua vida já está cheia! Não precisa usar poção.")
            return qtd, hp

        cura = 200
        hp += cura
        if hp > hp_max:
            hp = hp_max
        qtd -= 1
        self.println(f"Você bebeu uma {self.vermelho}Poção{self.branco} e recuperou {int(cura)} de vida!")
        self.println(f"Vida atual: {int(hp)}{self.branco}")
        self.println(f"Poções restantes: {qtd}{self.branco}")
        return qtd, hp


# ==============================
# Tkinter UI
# ==============================

class RPGApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("RPG da Guilda - Interface Temática")
        self.geometry("1100x700")
        self.minsize(980, 650)

        self.state = RPGState()
        self.logic = GameLogic(self.state, self._append_log)

        self._build_styles()
        self._build_frames()
        self._build_screens()

        self.show_screen("start")

    def _build_styles(self):
        self.configure(bg="#0b1020")
        style = ttk.Style(self)
        try:
            style.theme_use("clam")
        except Exception:
            pass
        style.configure("TButton", font=("Segoe UI", 11))
        style.configure("TLabel", font=("Segoe UI", 11))

    def _build_frames(self):
        self.root_top = tk.Frame(self, bg="#0b1020")
        self.root_top.pack(fill="x", padx=10, pady=10)

        self.title_label = tk.Label(
            self.root_top,
            text="⚔️  Guilda dos Aventureiros  🐉",
            fg="#e6e6e6",
            bg="#0b1020",
            font=("Segoe UI", 18, "bold"),
        )
        self.title_label.pack(side="left")

        self.hud_frame = tk.Frame(self.root_top, bg="#0b1020")
        self.hud_frame.pack(side="right")

        self.var_hp = tk.StringVar(value="HP: -")
        self.var_mana = tk.StringVar(value="Mana: -")
        self.var_reais = tk.StringVar(value="Reais: -")
        self.var_level = tk.StringVar(value="Nível: -")

        tk.Label(self.hud_frame, textvariable=self.var_level, fg="#c9d4ff", bg="#0b1020", font=("Segoe UI", 12, "bold")).grid(row=0, column=0, sticky="e")
        tk.Label(self.hud_frame, textvariable=self.var_hp, fg="#ff6b6b", bg="#0b1020", font=("Segoe UI", 12, "bold")).grid(row=1, column=0, sticky="e")
        tk.Label(self.hud_frame, textvariable=self.var_mana, fg="#5eead4", bg="#0b1020", font=("Segoe UI", 12, "bold")).grid(row=2, column=0, sticky="e")
        tk.Label(self.hud_frame, textvariable=self.var_reais, fg="#ffd166", bg="#0b1020", font=("Segoe UI", 12, "bold")).grid(row=3, column=0, sticky="e")

        self.main = tk.Frame(self, bg="#0b1020")
        self.main.pack(fill="both", expand=True, padx=10, pady=0)

        self.left_panel = tk.Frame(self.main, bg="#0b1020")
        self.left_panel.pack(side="left", fill="y", padx=(0, 10))

        self.right_panel = tk.Frame(self.main, bg="#0b1020")
        self.right_panel.pack(side="right", fill="both", expand=True)

        # Log
        self.log = tk.Text(self.right_panel, height=24, bg="#050815", fg="#eaeaea", insertbackground="#ffffff", font=("Consolas", 11))
        self.log.configure(state="disabled")
        self.log.pack(fill="both", expand=True)

    def _build_screens(self):
        self.screens = {}

        # Start screen
        scr_start = tk.Frame(self.main, bg="#0b1020")
        self.screens["start"] = scr_start

        tk.Label(scr_start, text="Seu Nome", fg="#ffffff", bg="#0b1020", font=("Segoe UI", 12, "bold")).pack(pady=(30, 5))
        self.ent_nome = tk.Entry(scr_start, width=30, font=("Segoe UI", 12))
        self.ent_nome.pack(pady=5)

        tk.Label(scr_start, text="Idade (14 a 40)", fg="#ffffff", bg="#0b1020", font=("Segoe UI", 12, "bold")).pack(pady=(20, 5))
        self.ent_idade = tk.Entry(scr_start, width=30, font=("Segoe UI", 12))
        self.ent_idade.pack(pady=5)

        tk.Label(scr_start, text="Escolha sua Classe", fg="#ffffff", bg="#0b1020", font=("Segoe UI", 12, "bold")).pack(pady=(20, 5))

        self.var_classe = tk.StringVar(value="mago")
        for cls in ["mago", "executor", "guerreiro", "arqueiro"]:
            rb = tk.Radiobutton(scr_start, text=cls.capitalize(), variable=self.var_classe, value=cls, bg="#0b1020", fg="#ffffff", selectcolor="#0b1020")
            rb.pack(anchor="w", padx=200)

        tk.Button(scr_start, text="Entrar na Guilda", command=self.start_game, bg="#6d28d9", fg="#ffffff", activebackground="#7c3aed", padx=20, pady=10).pack(pady=30)

        # Training screen
        scr_train = tk.Frame(self.main, bg="#0b1020")
        self.screens["train"] = scr_train

        tk.Label(scr_train, text="Treinamento", fg="#ffffff", bg="#0b1020", font=("Segoe UI", 16, "bold")).pack(pady=(30, 10))
        tk.Label(scr_train, text="Treine por quantos anos? (2 a 16)", fg="#c9d4ff", bg="#0b1020", font=("Segoe UI", 12)).pack(pady=5)

        self.ent_train = tk.Entry(scr_train, width=10, font=("Segoe UI", 12))
        self.ent_train.pack(pady=12)

        tk.Button(scr_train, text="Começar Treino", command=self.do_training, bg="#2563eb", fg="#ffffff", activebackground="#3b82f6", padx=20, pady=10).pack(pady=20)

        # Shop screen
        scr_shop = tk.Frame(self.main, bg="#0b1020")
        self.screens["shop"] = scr_shop

        tk.Label(scr_shop, text="Loja da Guilda", fg="#ffffff", bg="#0b1020", font=("Segoe UI", 16, "bold")).pack(pady=(20, 10))

        self.var_buy = tk.StringVar(value="sim")
        tk.Label(scr_shop, text="Você quer comprar poções?", fg="#c9d4ff", bg="#0b1020", font=("Segoe UI", 12)).pack(pady=5)
        rb1 = tk.Radiobutton(scr_shop, text="Sim", variable=self.var_buy, value="sim", bg="#0b1020", fg="#ffffff", selectcolor="#0b1020")
        rb2 = tk.Radiobutton(scr_shop, text="Não", variable=self.var_buy, value="nao", bg="#0b1020", fg="#ffffff", selectcolor="#0b1020")
        rb1.pack(anchor="w", padx=260)
        rb2.pack(anchor="w", padx=260)

        tk.Label(scr_shop, text="Quantidade de poções", fg="#c9d4ff", bg="#0b1020", font=("Segoe UI", 12)).pack(pady=15)
        self.ent_qtd_pocao = tk.Entry(scr_shop, width=10, font=("Segoe UI", 12))
        self.ent_qtd_pocao.insert(0, "0")
        self.ent_qtd_pocao.pack(pady=5)

        tk.Button(scr_shop, text="Finalizar Compra", command=self.do_shop, bg="#059669", fg="#ffffff", activebackground="#10b981", padx=20, pady=10).pack(pady=20)

        # Battle screen
        scr_battle = tk.Frame(self.main, bg="#0b1020")
        self.screens["battle"] = scr_battle

        tk.Label(scr_battle, text="Batalha Contra o Dragão", fg="#ffffff", bg="#0b1020", font=("Segoe UI", 16, "bold")).pack(pady=(20, 10))

        self.var_dragon_hp = tk.StringVar(value="Vida do Dragão: -")
        tk.Label(scr_battle, textvariable=self.var_dragon_hp, fg="#ff9f1c", bg="#0b1020", font=("Segoe UI", 12, "bold")).pack(pady=6)

        # Magic selection
        self.magic_choice = tk.StringVar(value="1")
        self.magic_frame = tk.Frame(scr_battle, bg="#0b1020")
        tk.Label(self.magic_frame, text="Magia (apenas Mago)", fg="#c9d4ff", bg="#0b1020", font=("Segoe UI", 11, "bold")).pack(anchor="w")
        rb_1 = tk.Radiobutton(self.magic_frame, text="1 - Bola de Fogo", variable=self.magic_choice, value="1", bg="#0b1020", fg="#ffffff", selectcolor="#0b1020")
        rb_2 = tk.Radiobutton(self.magic_frame, text="2 - Telecinese", variable=self.magic_choice, value="2", bg="#0b1020", fg="#ffffff", selectcolor="#0b1020")
        rb_3 = tk.Radiobutton(self.magic_frame, text="3 - Congelamento", variable=self.magic_choice, value="3", bg="#0b1020", fg="#ffffff", selectcolor="#0b1020")
        rb_1.pack(anchor="w")
        rb_2.pack(anchor="w")
        rb_3.pack(anchor="w")

        self.magic_frame.pack(pady=8)

        # Buttons
        btns = tk.Frame(scr_battle, bg="#0b1020")
        btns.pack(pady=14)

        tk.Button(btns, text="1 - Ataque", width=16, command=self.action_attack, bg="#7c3aed", fg="#ffffff", activebackground="#8b5cf6").grid(row=0, column=0, padx=6, pady=6)
        tk.Button(btns, text="2 - Fugir", width=16, command=self.action_flee, bg="#ef4444", fg="#ffffff", activebackground="#f87171").grid(row=0, column=1, padx=6, pady=6)
        tk.Button(btns, text="3 - Magia", width=16, command=self.action_magic, bg="#2563eb", fg="#ffffff", activebackground="#3b82f6").grid(row=0, column=2, padx=6, pady=6)
        tk.Button(btns, text="4 - Bomba", width=16, command=self.action_bomb, bg="#f59e0b", fg="#1f2937", activebackground="#fbbf24").grid(row=1, column=0, padx=6, pady=6)
        tk.Button(btns, text="5 - Poção", width=16, command=self.action_potion, bg="#22c55e", fg="#ffffff", activebackground="#34d399").grid(row=1, column=1, padx=6, pady=6)

        self.var_pocao = tk.StringVar(value="Poções: 0")
        tk.Label(scr_battle, textvariable=self.var_pocao, fg="#86efac", bg="#0b1020", font=("Segoe UI", 12, "bold")).pack(pady=6)

        self.btn_disable_all = []
        for child in btns.winfo_children():
            self.btn_disable_all.append(child)

        tk.Button(scr_battle, text="Reiniciar", command=self.reset_all, bg="#111827", fg="#ffffff", activebackground="#1f2937", padx=20, pady=8).pack(pady=16)

    def _append_log(self, text: str):
        # Use typewriter feel but without per-char for huge output; here we just append quickly.
        self.log.configure(state="normal")
        self.log.insert("end", text)
        self.log.see("end")
        self.log.configure(state="disabled")

    def show_screen(self, name: str):
        # Remove previous
        for k, scr in self.screens.items():
            scr.pack_forget()
        self.screens[name].pack(side="left", fill="both", expand=True)

    def reset_all(self):
        self.state = RPGState()
        self.logic = GameLogic(self.state, self._append_log)
        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")
        self.show_screen("start")
        self.var_hp.set("HP: -")
        self.var_mana.set("Mana: -")
        self.var_reais.set("Reais: -")
        self.var_level.set("Nível: -")
        self.var_dragon_hp.set("Vida do Dragão: -")
        self.var_pocao.set("Poções: 0")

    # ==============================
    # Flow actions
    # ==============================

    def start_game(self):
        nome = self.ent_nome.get().strip()
        if not nome:
            self._append_log("Informe seu nome.\n")
            return

        try:
            idade = int(self.ent_idade.get().strip())
        except Exception:
            self._append_log("Idade inválida.\n")
            return

        if idade < 14:
            self._append_log("Você é muito novo(a) para entrar na Guilda!\n")
            return
        if idade > 40:
            self._append_log("Você já está muito velho(a) para entrar na Guilda!\n")
            return

        classe = self.var_classe.get().strip().lower()

        self.state.nome = nome
        self.state.idade = idade
        self.state.classe = classe
        self.state.nivel = 1
        self.state.qtd_pocao = 0
        self.state.recalc_stats()

        self.var_level.set(f"Nível: {self.state.nivel}")
        self.var_hp.set(f"HP: {self.state.hp}")
        self.var_mana.set(f"Mana: {self.state.mana}")
        self.var_reais.set(f"Reais: {round(self.state.reais,2)}")

        self.log.configure(state="normal")
        self.log.delete("1.0", "end")
        self.log.configure(state="disabled")

        self._append_log(f"Bem-vindo, {self.state.nome.capitalize()}! Você entrou na Guilda.\n")
        self._append_log(f"Classe: {self.state.classe.capitalize()}\n")
        self._append_log(f"Atributos iniciais -> HP: {self.state.hp}, Mana: {self.state.mana}, Reais: {round(self.state.reais,2)}\n\n")

        self.show_screen("train")

    def do_training(self):
        try:
            train_years = int(self.ent_train.get().strip())
        except Exception:
            self._append_log("Informe um número válido de anos.\n")
            return

        if train_years < 2:
            self._append_log("Treine por no mínimo 2 anos!\n")
            return
        if train_years > 16:
            # match original flavor: if >= 30, set max level. Here we cap to 100 with same spirit.
            if train_years >= 30:
                self._append_log("Você treinou demais... alcançou o nível 100 (máx)!\n")
                self.state.nivel = 100
            else:
                self._append_log("Você não precisa treinar tanto assim (resultado reduzido).\n")
                self.state.nivel = min(100, self.state.nivel + 6 * 2)
        else:
            for _ in range(train_years):
                self.state.nivel += 6
                time.sleep(0.15)
            self._append_log("Treino concluído! Você subiu de nível.\n")

        self.state.recalc_stats()
        self.state.idade += train_years

        self.var_level.set(f"Nível: {self.state.nivel}")
        self.var_hp.set(f"HP: {self.state.hp}")
        self.var_mana.set(f"Mana: {self.state.mana}")
        self.var_reais.set(f"Reais: {round(self.state.reais,2)}")

        self._append_log(f"Novo nível: {self.state.nivel}\n")
        self._append_log(f"HP: {self.state.hp} | Mana: {self.state.mana} | Reais: {round(self.state.reais,2)}\n\n")

        self.show_screen("shop")

    def do_shop(self):
        want = self.var_buy.get().strip().lower() == "sim"
        try:
            qtd = int(self.ent_qtd_pocao.get().strip())
        except Exception:
            qtd = 0

        pocao = self.logic.pocao_preco if hasattr(self.logic, "pocao_preco") else 50
        pocao = 50

        if qtd < 0:
            qtd = 0

        if not want:
            self._append_log("Você não comprou nada na loja.\n")
        else:
            if self.state.reais < pocao:
                self._append_log("Você não tem dinheiro suficiente para comprar poções.\n")
            else:
                qtd_to_buy = qtd
                if qtd_to_buy <= 0:
                    qtd_to_buy = 0
                # If not enough money, buy as much as possible.
                max_affordable = int(self.state.reais // pocao)
                if qtd_to_buy > max_affordable:
                    qtd_to_buy = max_affordable
                total = qtd_to_buy * pocao
                self.state.reais -= total
                self.state.qtd_pocao += qtd_to_buy

                self._append_log(f"Compra concluída! {qtd_to_buy} poções adicionadas ao inventário.\n")
                self._append_log(f"Custo total: {total} Reais | Troco: {round(self.state.reais,2)}\n")

        self.var_reais.set(f"Reais: {round(self.state.reais,2)}")
        self.var_pocao.set(f"Poções: {self.state.qtd_pocao}")

        self.start_battle()

    def start_battle(self):
        self.state.bosshp = self.state.nivel * 100
        self.state.max_hp = self.state.nivel * 50

        self.var_dragon_hp.set(f"Vida do Dragão: {self.state.bosshp}")
        self._append_log(f"Oh não... apareceu um {self.logic.roxo}Dragão{self.logic.branco} e ele está atacando o vilarejo!\n\n")

        self.show_screen("battle")
        self.update_hud()

    def update_hud(self):
        self.var_hp.set(f"HP: {int(self.state.hp)}")
        self.var_mana.set(f"Mana: {int(self.state.mana)}")
        self.var_reais.set(f"Reais: {round(self.state.reais,2)}")
        self.var_level.set(f"Nível: {self.state.nivel}")
        self.var_dragon_hp.set(f"Vida do Dragão: {int(self.state.bosshp)}")
        self.var_pocao.set(f"Poções: {int(self.state.qtd_pocao)}")

    def _disable_actions(self, disabled=True):
        st = "disabled" if disabled else "normal"
        for b in self.btn_disable_all:
            b.configure(state=st)

    def _check_end(self):
        if self.state.bosshp <= 0 and self.state.hp <= 0:
            self._append_log("\nO Dragão morreu mas conseguiu te matar junto com ele! GAME OVER.\n")
            self._disable_actions(True)
            return True
        if self.state.bosshp <= 0:
            win = 10000
            self.state.reais += win
            self._append_log(f"\nVocê venceu! O Dragão está morto.\nRecompensa: {win} Reais\nSaldo: {round(self.state.reais,2)}\n")
            self._disable_actions(True)
            return True
        if self.state.hp <= 0:
            self._append_log("\nVocê está morto... GAME OVER!\n")
            self._disable_actions(True)
            return True
        return False

    # ==============================
    # Battle actions
    # ==============================

    def action_attack(self):
        if self._disable_if_not_battle():
            return

        if self.state.classe not in ["guerreiro", "executor", "arqueiro", "mago"]:
            self._append_log("Classe desconhecida.\n")
            return

        if self.state.classe in ["guerreiro", "executor"]:
            self.state.bosshp, self.state.hp = self.logic.ataque_corpo(self.state.bosshp, self.state.hp, self.state.nivel)
        elif self.state.classe == "arqueiro":
            self.state.bosshp, self.state.hp = self.logic.ataque_tiro(self.state.bosshp, self.state.hp, self.state.nivel)
        else:
            self._append_log("Um Mago não é tão bom no corpo a corpo. Use Magias!\n")
        self.update_hud()
        self._check_end()

    def action_flee(self):
        if self._disable_if_not_battle():
            return
        self.state.hp = self.logic.fuga_all(self.state.hp)
        self.update_hud()
        self._check_end()

    def action_magic(self):
        if self._disable_if_not_battle():
            return
        if self.state.classe != "mago":
            self._append_log("Apenas Magos podem usar Magias!\n")
            return

        self.logic.selected_magic = self.magic_choice.get()
        self.state.bosshp, self.state.hp, self.state.mana = self.logic.ataque_mago(
            self.state.bosshp, self.state.hp, self.state.nivel, self.state.mana
        )
        self.update_hud()
        self._check_end()

    def action_bomb(self):
        if self._disable_if_not_battle():
            return
        self.state.bosshp, self.state.hp = self.logic.ataque_bomba(self.state.bosshp, self.state.hp, self.state.nivel)
        self.update_hud()
        self._check_end()

    def action_potion(self):
        if self._disable_if_not_battle():
            return
        self.state.qtd_pocao, self.state.hp = self.logic.usar_pocao(
            self.state.bosshp, self.state.hp, self.state.nivel, self.state.qtd_pocao
        )
        self.update_hud()
        self._check_end()

    def _disable_if_not_battle(self):
        if self.screens["battle"].winfo_ismapped() is False:
            self._append_log("Você ainda não começou a batalha.\n")
            return True
        if self.state.bosshp <= 0 or self.state.hp <= 0:
            return True
        return False


if __name__ == "__main__":
    app = RPGApp()
    app.mainloop()

