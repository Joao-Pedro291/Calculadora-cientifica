import tkinter as tk
from tkinter import simpledialog
import math
import random
 
janela = tk.Tk()
janela.title("Calc")
janela.configure(bg="black")
 
caixaCalc = tk.Entry(janela, font=("Arial", 20), justify="right", width=20, bd=5, relief="sunken")
caixaCalc.insert(0, "0")
caixaCalc.grid(row=0, column=0, columnspan=6, pady=15, padx=5)
 
frame_cientifico = tk.Frame(janela, bg="black")
frame_cientifico.grid(row=1, column=0, columnspan=6)
frame_normal = tk.Frame(janela, bg="black")
frame_normal.grid(row=2, column=0, columnspan=6)
 
shift_ativo = False
ultimo_resultado = 0
shift_labels = {
    "1": "s-sum",
    "2": "s-var",
    "0": "rnd",
    ".": "Ran#",
    "=": "%"
}
botoes_shift = {}
 
def ativar_shift():
    global shift_ativo
    shift_ativo = not shift_ativo
    for key, botao in botoes_shift.items():
        botao.config(text=shift_labels[key] if shift_ativo else key)
 
def adicionar_texto(texto):
    atual = caixaCalc.get()
    if atual == "0":
        caixaCalc.delete(0, tk.END)
    caixaCalc.insert(tk.END, texto)
 
def calcular():
    global ultimo_resultado
    expressao = caixaCalc.get()
    try:
        expressao = expressao.replace("×", "*").replace("÷", "/")
        if "*10**(" in expressao and not expressao.endswith(")"):
            expressao += ")"
        resultado = eval(expressao)
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, str(resultado))
        ultimo_resultado = resultado
    except:
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, "Erro")
 
def deletar():
    atual = caixaCalc.get()
    if len(atual) > 1:
        caixaCalc.delete(len(atual)-1, tk.END)
    else:
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, "0")
 
def limpar():
    caixaCalc.delete(0, tk.END)
    caixaCalc.insert(0, "0")
 
def processar_shift(label):
    global shift_ativo, ultimo_resultado
    if label == "π":
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, str(math.pi))
    elif label == "rnd":
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, str(random.randint(0,100)))
    elif label == "Ran#":
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, str(random.random()))
    elif label == "drg":
        caixaCalc.delete(0, tk.END)
        caixaCalc.insert(0, str(ultimo_resultado))
    elif label == "s-sum":
        entrada = simpledialog.askstring("s-sum", "Digite números separados por vírgula:")
        try:
            numeros = list(map(float, entrada.split(',')))
            soma = sum(numeros)
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(soma))
            ultimo_resultado = soma
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "s-var":
        entrada = simpledialog.askstring("s-var", "Digite números separados por vírgula:")
        try:
            numeros = list(map(float, entrada.split(',')))
            media = sum(numeros)/len(numeros)
            variancia = sum((x-media)**2 for x in numeros)/len(numeros)
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(variancia))
            ultimo_resultado = variancia
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "%":
        calcular()
    shift_ativo = False
    for key, botao in botoes_shift.items():
        botao.config(text=key)
 
def processar_botao(label):
    global shift_ativo, ultimo_resultado
 
    if label == "EXP":
        caixaCalc.insert(tk.END, "*10**(")
    elif label == "Ans":
        caixaCalc.insert(tk.END, str(ultimo_resultado))
    elif shift_ativo and label in shift_labels.values():
        processar_shift(label)
    elif label == "=":
        calcular()
    elif label == "DEL":
        deletar()
    elif label == "AC":
        limpar()
    elif label == "x^2":
        try:
            valor = float(caixaCalc.get())
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(valor**2))
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "x^3":
        try:
            valor = float(caixaCalc.get())
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(valor**3))
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "√":
        try:
            valor = float(caixaCalc.get())
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(math.sqrt(valor)))
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "x^-1":
        try:
            valor = float(caixaCalc.get())
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(1/valor))
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "log":
        try:
            valor = float(caixaCalc.get())
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(math.log10(valor)))
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    elif label == "ln":
        try:
            valor = float(caixaCalc.get())
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, str(math.log(valor)))
        except:
            caixaCalc.delete(0, tk.END)
            caixaCalc.insert(0, "Erro")
    else:
        adicionar_texto(label)
 
def criar_botao(frame, texto, linha, coluna, cor="lightgray", fg="black",
                largura=6, altura=2, colspan=1, rowspan=1, shiftable=False):
    botao = tk.Button(
        frame,
        text=texto,
        font=("Arial", 12, "bold"),
        fg=fg,
        bg=cor,
        width=largura,
        height=altura,
        relief="raised",
        bd=2,
        command=lambda t=texto: processar_botao(t)
    )
    botao.grid(row=linha, column=coluna, columnspan=colspan, rowspan=rowspan, padx=3, pady=3, sticky="nsew")
    if shiftable:
        botoes_shift[texto] = botao
    if texto == "SHIFT":
        botao.config(command=ativar_shift)
    return botao
 
criar_botao(frame_cientifico, "SHIFT", 0, 0, fg="orange")
criar_botao(frame_cientifico, "ALPHA", 0, 1, fg="red")
criar_botao(frame_cientifico, "REPLAY", 0, 2, colspan=2)
criar_botao(frame_cientifico, "MODE\nCLR", 0, 4)
criar_botao(frame_cientifico, "ON", 0, 5)
criar_botao(frame_cientifico, "x^-1", 1, 0)
criar_botao(frame_cientifico, "nPr", 1, 1)
criar_botao(frame_cientifico, "Rec(", 1, 3)
criar_botao(frame_cientifico, "Pol(", 1, 4)
criar_botao(frame_cientifico, "√", 1, 5)
criar_botao(frame_cientifico, "a b/c", 2, 0)
criar_botao(frame_cientifico, "x^2", 2, 1)
criar_botao(frame_cientifico, "x^3", 2, 2)
criar_botao(frame_cientifico, "^", 2, 3)
criar_botao(frame_cientifico, "log", 2, 4)
criar_botao(frame_cientifico, "ln", 2, 5)
 
for i in range(6):
    frame_cientifico.grid_columnconfigure(i, weight=1)
 
criar_botao(frame_normal, "7", 0, 0)
criar_botao(frame_normal, "8", 0, 1)
criar_botao(frame_normal, "9", 0, 2)
criar_botao(frame_normal, "DEL", 0, 3, cor="lightcoral")
criar_botao(frame_normal, "AC", 0, 4, cor="lightcoral")
criar_botao(frame_normal, "4", 1, 0)
criar_botao(frame_normal, "5", 1, 1)
criar_botao(frame_normal, "6", 1, 2)
criar_botao(frame_normal, "×", 1, 3)
criar_botao(frame_normal, "÷", 1, 4)
criar_botao(frame_normal, "1", 2, 0, shiftable=True)
criar_botao(frame_normal, "2", 2, 1, shiftable=True)
criar_botao(frame_normal, "3", 2, 2)
criar_botao(frame_normal, "+", 2, 3)
criar_botao(frame_normal, "-", 2, 4)
criar_botao(frame_normal, "0", 3, 0, shiftable=True)
criar_botao(frame_normal, ".", 3, 1, shiftable=True)
criar_botao(frame_normal, "EXP", 3, 2)
criar_botao(frame_normal, "Ans", 3, 3)
criar_botao(frame_normal, "=", 3, 4, cor="lightblue", shiftable=True)
 
for i in range(5):
    frame_normal.grid_columnconfigure(i, weight=1)
 
janela.mainloop()