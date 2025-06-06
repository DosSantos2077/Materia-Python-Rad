import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3
from datetime import date

def janela_deletar(user_id,usuario):
    janela = tk.Toplevel()
    janela.title("deletar registro")
    janela.geometry("500x450")
    janela.configure(bg="lightblue")

    tk.Label(janela, text="ID do registro:").pack(pady=5)
    entry_id = tk.Entry(janela, width=40)
    entry_id.pack(pady=5)


    def deletar_registro():
        id = entry_id.get()
        
        data = date.today()
        if not id :
            messagebox.showwarning( "Preencha todos os campos obrigatórios.")
            return

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()

            cursor.execute("""
                DELETE FROM registro
                WHERE id = ? AND userId = ?
            """, (id, user_id))

            if cursor.rowcount == 0:
                messagebox.showwarning("Aviso", "Nenhum registro encontrado com esse ID para este usuário.")
                conn.close()
            else:
                conn.commit()
                messagebox.showinfo("Sucesso", "Registro deletado com sucesso.")
                conn.close()

                with open("relatorio.txt", "a") as arquivo:
                    arquivo.write(f"Usuario de ID: {user_id} deletou um registro em {data.today()}\n")

            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao deletar registro: {str(e)}")

    btn_deletar = tk.Button(janela, text="Deletar", command=deletar_registro)
    btn_deletar.pack(pady=20)