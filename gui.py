import tkinter as tk
from tkinter import ttk
from senha import gerar_senhas
from utils import validar_inteiro


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerador de Senhas")
        self.root.geometry("300x450")
        self._widgets()

    def _widgets(self):
        tk.Label(self.root, text="Quantidade de caracteres?").pack()
        self.entrada_caracteres = tk.Entry(self.root)
        self.entrada_caracteres.pack(pady=5)


        self.maiuscula_ = self._combo("Incluir maiúsculas?", "Sim")
        self.minuscula_ = self._combo("Incluir minúsculas?", "Sim")
        self.numero_ = self._combo("Incluir números?", "Sim")
        self.simbolos_ = self._combo("Incluir símbolos?", "Sim")


        tk.Label(self.root, text="Quantidade de senhas?").pack()
        self.entrada_qtd_senhas = tk.Entry(self.root)
        self.entrada_qtd_senhas.pack(pady=5)

        self.botao = tk.Button(self.root, text="Gerar Senha(s)", command=self.gerar)
        self.botao.pack()

        self.entrada_invalida = tk.Label(self.root, text="")
        self.entrada_invalida.pack()

        frame = tk.Frame(self.root)
        frame.pack(pady=10)

        self.resultado = tk.Text(frame, width=50, height=10, wrap="none")
        self.resultado.pack(side=tk.LEFT)

        scrollbar = tk.Scrollbar(frame, command=self.resultado.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.resultado.config(yscrollcommand=scrollbar.set)


    def _combo(self, label, default="Sim"):
        tk.Label(self.root, text=label).pack()
        combo = ttk.Combobox(self.root, values=["Sim", "Não"])
        combo.set(default)
        combo.pack(pady=5)
        return combo

    def gerar(self):
        self.entrada_invalida.config(text="")

        valido_caracteres, qtd_caracteres = validar_inteiro(self.entrada_caracteres.get(), minimo=8)
        valido_qtd, qtd_senhas = validar_inteiro(self.entrada_qtd_senhas.get(), minimo=1)

        if not valido_caracteres:
            self.entrada_invalida.config(text=qtd_caracteres)
            return
        if not valido_qtd:
            self.entrada_invalida.config(text=qtd_senhas)
            return

        incluir_maiusculas = self.maiuscula_.get() == "Sim"
        incluir_minusculas = self.minuscula_.get() == "Sim"
        incluir_numeros = self.numero_.get() == "Sim"
        incluir_simbolos = self.simbolos_.get() == "Sim"

        try:
            senhas = gerar_senhas(
                qtd_caracteres = qtd_caracteres,
                qtd_senhas = qtd_senhas,
                incluir_maiusculas = incluir_maiusculas,
                incluir_minusculas = incluir_minusculas,
                incluir_numeros = incluir_numeros,
                incluir_simbolos = incluir_simbolos,
            )
        except ValueError as e:
            self.entrada_invalida.config(text=f"⚠️ {str(e)}")
            return

        self.resultado.delete("1.0", tk.END)
        self.resultado.insert(tk.END, "\n".join(senhas))

