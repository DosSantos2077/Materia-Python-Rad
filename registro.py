import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3

def abrir_janela_registro(user_id):
    janela = tk.Toplevel()
    janela.title("Novo Registro")
    janela.geometry("350x350")

    tk.Label(janela, text="Descrição:").pack(pady=5)
    entry_descricao = tk.Entry(janela, width=40)
    entry_descricao.pack(pady=5)

    tk.Label(janela, text="Data (AAAA-MM-DD):").pack(pady=5)
    entry_data = tk.Entry(janela, width=40)
    entry_data.pack(pady=5)

    tk.Label(janela, text="Todo (Sim ou Não):").pack(pady=5)
    combo_todo = ttk.Combobox(janela, values=["Sim", "Não"], state="readonly", width=10)
    combo_todo.pack(pady=5)
    combo_todo.current(0)

    caminho_path = tk.StringVar()

    def selecionar_arquivo():
        caminho = filedialog.askopenfilename(title="Selecionar arquivo")
        if caminho:
            caminho_path.set(caminho)

    tk.Button(janela, text="Selecionar Arquivo", command=selecionar_arquivo).pack(pady=10)
    tk.Label(janela, textvariable=caminho_path, wraplength=300).pack(pady=5)

    def salvar_registro():
        descricao = entry_descricao.get()
        data = entry_data.get()
        todo_valor = combo_todo.get()
        path = caminho_path.get()

        if not descricao or not data:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
            return

        todo_inteiro = 1 if todo_valor == "Sim" else 0

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO registro (userId, desc, data, todo, path)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, descricao, data, todo_inteiro, path))
            conn.commit()
            conn.close()

            messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar registro: {str(e)}")

    btn_salvar = tk.Button(janela, text="Salvar Registro", command=salvar_registro)
    btn_salvar.pack(pady=20)
