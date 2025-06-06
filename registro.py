import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3
from datetime import date

def janela_registro(user_id,usuario):
    janela = tk.Toplevel()
    janela.title("Novo Registro")
    janela.geometry("350x350")
    janela.configure(bg="lightblue")

    tk.Label(janela, text="Descrição:").pack(pady=5)
    entry_descricao = tk.Entry(janela, width=40)
    entry_descricao.pack(pady=5)

    

    tk.Label(janela, text="Trabalhando (Sim ou Não):").pack(pady=5)
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
        data = date.today()
        todo = combo_todo.get()
        path = caminho_path.get()

        if not descricao or not data:
            messagebox.showwarning("Aviso", "Preencha todos os campos obrigatórios.")
            return

        

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()
            cursor.execute("""
                INSERT INTO registro (userId, desc, data, todo, path)
                VALUES (?, ?, ?, ?, ?)
            """, (user_id, descricao, data, todo, path))
            conn.commit()
            conn.close()

            messagebox.showinfo("Sucesso", "Registro salvo com sucesso!")
            with open("relatorio.txt", "a") as arquivo:
                arquivo.write(f"Usuario de ID: {user_id} adicionou um registro em {data}\n")

            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao salvar registro: {str(e)}")

    btn_salvar = tk.Button(janela, text="Salvar Registro", command=salvar_registro)
    btn_salvar.pack(pady=20)
