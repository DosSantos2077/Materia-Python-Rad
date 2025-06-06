import tkinter as tk
from tkinter import messagebox
import sqlite3
import registro
import main

def consultar(user_id,root):
    try:
        conn = sqlite3.connect("banco.db")  # Conecta ao banco de dados correto
        cursor = conn.cursor()

        # Consulta registros filtrando pelo campo correto: userId
        cursor.execute("SELECT data, id, desc, path, todo FROM registro WHERE userId = ?", (user_id,))
        resultados = cursor.fetchall()
        conn.close()

        if resultados:
            mensagem = "Registros encontrados:\n\n"
            for i, (data, id, desc, path, todo) in enumerate(resultados, 1):
                mensagem += f"{i}.\n Descriçao: {desc}\n Caminho: {path}\n Terminado {todo}\n ID: {id}\n Data:  {data}\n\n"
            text_widget = tk.Text(root)
            text_widget.pack(expand=True, fill='both')
            text_widget.insert(tk.END, mensagem)
        else:
            messagebox.showinfo("Sem Registros", "Nenhum registro encontrado para este usuário.")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao consultar: {str(e)}")

def janela_consulta(user_id):
    janela = tk.Toplevel()
    janela.title("Consultas")
    janela.geometry("400x500")

    consultar(user_id,janela)