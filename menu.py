import tkinter as tk
from tkinter import messagebox
import sqlite3
import registro
import main
import consulta
import deletar
import alterar

def menu(user_id, usuario):
    janela = tk.Tk()
    janela.title("Sistema Principal")
    janela.geometry("180x300")
    janela.configure(bg="lightblue")

    label_id = tk.Label(janela, text=f"ID do usuário: {user_id}")
    label_id.grid(row=0, column=0, padx=10, pady=10)

    

    btn_consultar = tk.Button(janela, text="Consultar Registros",
                              command=lambda: consulta.janela_consulta(user_id))
    btn_consultar.grid(row=1, column=0, padx=10, pady=20)

    btn_novo = tk.Button(janela, text="Novo Registro",
                         command=lambda: registro.janela_registro(user_id,usuario))
    btn_novo.grid(row=2, column=0, padx=10, pady=10)

    btn_del = tk.Button(janela, text="deletar registro",
                         command=lambda: deletar.janela_deletar(user_id,usuario))
    btn_del.grid(row=4, column=0, padx=10, pady=10)

    btn_alt = tk.Button(janela, text="alterar registro",
                         command=lambda: alterar.janela_alterar(user_id,usuario))
    btn_alt.grid(row=3, column=0, padx=10, pady=10)

    janela.mainloop()
