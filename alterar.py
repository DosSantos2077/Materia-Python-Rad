import tkinter as tk
from tkinter import messagebox, ttk, filedialog
import sqlite3
from datetime import date

def janela_alterar(user_id,usuario):
    janela = tk.Toplevel()
    janela.title("Alterar Registro")
    janela.geometry("350x450")
    janela.configure(bg="lightblue")

    tk.Label(janela, text="ID do registro que será alterado:").pack(pady=5)
    entry_id = tk.Entry(janela, width=40)
    entry_id.pack(pady=5)

    entry_path = tk.StringVar()

    def alterar_registroCaminho():
        id = entry_id.get()
        path = entry_path.get()
        data = date.today()
        if not id :
            messagebox.showwarning( "Preencha o campo.")
            return

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE registro SET path = ?
                WHERE id = ? AND userId = ?
            """, (path,id, user_id))

            if cursor.rowcount == 0:
                messagebox.showwarning("Aviso", "Nenhum registro encontrado com esse ID para este usuário.")
                conn.close()
            else:
                conn.commit()
                messagebox.showinfo("Sucesso", "Registro alterado com sucesso.")
                conn.close()

                with open("relatorio.txt", "a") as arquivo:
                    arquivo.write(f"Usuario de ID: {user_id} alterou o caminho de um registro em {data.today()}\n")

            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar registro: {str(e)}")


    def alterar_registroTodo():
        id = entry_id.get()
        todo = combo_todo.get()
        data = date.today()
        if not id :
            messagebox.showwarning( "Preencha o campo.")
            return

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE registro SET todo = ?
                WHERE id = ? AND userId = ?
            """, (todo,id, user_id))

            if cursor.rowcount == 0:
                messagebox.showwarning("Aviso", "Nenhum registro encontrado com esse ID para este usuário.")
                conn.close()
            else:
                conn.commit()
                messagebox.showinfo("Sucesso", "Registro alterado com sucesso.")
                conn.close()

                with open("relatorio.txt", "a") as arquivo:
                    arquivo.write(f"Usuario de ID: {user_id} alterou o estatus de um registro em {data.today()}\n")

            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar registro: {str(e)}")


    def alterar_registroDesc():
        id = entry_id.get()
        desc = entry_descricao.get()
        data = date.today()
        if not id :
            messagebox.showwarning( "Preencha o campo.")
            return

        try:
            conn = sqlite3.connect("banco.db")
            cursor = conn.cursor()

            cursor.execute("""
                UPDATE registro SET desc = ?
                WHERE id = ? AND userId = ?
            """, (desc,id, user_id))

            if cursor.rowcount == 0:
                messagebox.showwarning("Aviso", "Nenhum registro encontrado com esse ID para este usuário.")
                conn.close()
            else:
                conn.commit()
                messagebox.showinfo("Sucesso", "Registro alterado com sucesso.")
                conn.close()

                with open("relatorio.txt", "a") as arquivo:
                    arquivo.write(f"Usuario de ID: {user_id} alterou a descrição de um registro em {data.today()}\n")

            
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao alterar registro: {str(e)}")                

    def selecionar_arquivo():
        caminho = filedialog.askopenfilename(title="Selecionar caminho")
        if caminho:
            entry_path.set(caminho)

    tk.Label(janela, text="Trabalhando (Sim ou Não):").pack(pady=5)
    combo_todo = ttk.Combobox(janela, values=["Sim", "Não"], state="readonly", width=10)
    combo_todo.pack(pady=5)
    combo_todo.current(0)   

    btn_alterarTodo = tk.Button(janela, text="Alterar estatus", command=alterar_registroTodo)
    btn_alterarTodo.pack(pady=20)     

    tk.Button(janela, text="Selecionar caminho", command=selecionar_arquivo).pack(pady=10)
    tk.Label(janela, textvariable=entry_path, wraplength=300).pack(pady=5)        

    btn_alterar = tk.Button(janela, text="Alterar caminho", command=alterar_registroCaminho)
    btn_alterar.pack(pady=20)
 
    tk.Label(janela, text="Descrição:").pack(pady=5)
    entry_descricao = tk.Entry(janela, width=40)
    entry_descricao.pack(pady=5)

    btn_alterarDesc = tk.Button(janela, text="Alterar descrição", command=alterar_registroDesc)
    btn_alterarDesc.pack(pady=20)

    

    

    