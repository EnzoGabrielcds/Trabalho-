import tkinter as tk
from tkinter import messagebox

# Função para calcular despesas e prever economia
def calcular_economia():
    try:
        despesas = float(entry_despesas.get())
        receita = float(entry_receita.get())
        economia = receita - despesas
        label_resultado.config(text=f"Economia Mensal: R$ {economia:.2f}")
    except ValueError:
        messagebox.showerror("Erro", "Insira valores numéricos válidos.")

# Criando a interface
app = tk.Tk()
app.title("Gestão de Despesas - Enzodoairmaxtn")
app.geometry("400x300")
app.configure(bg="red")

# Labels e Entradas
tk.Label(app, text="Total de Despesas (R$):", bg="red", fg="white").pack(pady=5)
entry_despesas = tk.Entry(app)
entry_despesas.pack(pady=5)

tk.Label(app, text="Receita Mensal (R$):", bg="red", fg="white").pack(pady=5)
entry_receita = tk.Entry(app)
entry_receita.pack(pady=5)

# Botão para cálculo
tk.Button(app, text="Calcular Economia", command=calcular_economia, bg="white", fg="red").pack(pady=10)

# Resultado
label_resultado = tk.Label(app, text="", bg="red", fg="white", font=("Arial", 12))
label_resultado.pack(pady=5)

app.mainloop()

